#!/usr/bin/env bash
set -euo pipefail

# Generates the async VRChat API Python SDK from the OpenAPI specification.
#
# Usage: generate.sh [--no-patch] [<version>] [openapi.yaml]
#   --no-patch      Stop right after generation + post-processing, BEFORE
#                   applying patches/ and the model post-processor. This is the
#                   pristine baseline the `patch` steps operate on — use it when
#                   upstream spec/generator changes force you to rewrite patches.
#   <version>       SDK version written to setup.py and vrchatapi/__init__.py
#                   (e.g. 1.20.8). Optional: when omitted it is read from the
#                   spec's `info.version` (needs `yq`), with `-nightly.` -> `.dev`
#                   like the CI workflow does.
#   [openapi.yaml]  Optional path to a pre-bundled single-file OpenAPI spec.
#                   When omitted, the latest spec is fetched from
#                   https://github.com/vrchatapi/specification (main branch)
#                   and bundled with `redocly`.
#
# Requirements:
#   - openapi-generator CLI (version pinned in openapitools.json, needs Java 11+)
#   - git and redocly (only when fetching the spec from the specification repo)
#   - yq (only when <version> is omitted)
#   - patch, perl, python3 (python3 for tools/make_models_lenient.py)

# ---- Package metadata (single source of truth) -----------------------------
PACKAGE_NAME="vrchatapi"            # import package name
PROJECT_NAME="vrchatapi-async"      # distribution name on PyPI
DESCRIPTION="VRChat API Library for Python (async version)"
KEYWORDS='["vrchat", "vrchatapi", "vrc"]'
AUTHOR="hi94740"
AUTHOR_EMAIL="hi94740@qq.com"
PACKAGE_URL="https://github.com/hi94740/vrchatapi-python-async"  # set to this repo's URL

# ---- Argument parsing -------------------------------------------------------
NO_PATCH=0
VERSION=""
SPEC_FILE=""
for arg in "$@"; do
  case "${arg}" in
    --no-patch) NO_PATCH=1 ;;
    -*) echo "Unknown option: ${arg}" >&2; exit 1 ;;
    *)
      # A positional argument that is an existing .yaml/.yml path is the spec
      # file; anything else is treated as <version> (order-independent enough
      # for the common `generate.sh [--no-patch] [<version>] [openapi.yaml]`).
      if [ -z "${SPEC_FILE}" ] && [ -f "${arg}" ]; then
        case "${arg}" in
          *.yaml|*.yml) SPEC_FILE="${arg}"; continue ;;
        esac
      fi
      if [ -z "${VERSION}" ]; then
        VERSION="${arg}"
      else
        echo "Too many arguments: ${arg}" >&2
        exit 1
      fi
      ;;
  esac
done

WORK_DIR="$(mktemp -d)"
trap 'rm -rf "${WORK_DIR}"' EXIT

if [ -n "${SPEC_FILE}" ]
then
  cp "${SPEC_FILE}" "${WORK_DIR}/openapi.yaml"
else
  git clone --depth 1 https://github.com/vrchatapi/specification.git "${WORK_DIR}/specification" >/dev/null 2>&1
  (cd "${WORK_DIR}/specification" && redocly bundle legacy-yaml >/dev/null)
  cp "${WORK_DIR}/specification/dist/openapi-legacy.yaml" "${WORK_DIR}/openapi.yaml"
fi

# Version defaults to the spec's `info.version`; PyPI wants `.dev` where the
# specification says `-nightly.` (same normalization as the CI workflow).
if [ -z "${VERSION}" ]; then
  if ! command -v yq >/dev/null 2>&1; then
    echo "yq is required to read <version> from the spec; pass <version> explicitly or install yq." >&2
    exit 1
  fi
  VERSION="$(yq -r '.info.version' "${WORK_DIR}/openapi.yaml")"
  if [ -z "${VERSION}" ] || [ "${VERSION}" = "null" ]; then
    echo "Could not read info.version from the spec; pass <version> explicitly." >&2
    exit 1
  fi
fi
VERSION="${VERSION/-nightly./.dev}"

# Robustly remove previous generated output. On macOS `rm -rf` can race with
# Finder recreating .DS_Store inside the directories ("Directory not empty").
if ! rm -rf vrchatapi docs 2>/dev/null; then
  sleep 1
  rm -rf vrchatapi docs
fi

openapi-generator generate \
-g python \
--library=asyncio \
--additional-properties=packageName=${PACKAGE_NAME},projectName=${PROJECT_NAME},packageUrl=${PACKAGE_URL},compatibleWithPythonLegacy=true \
-o . \
-i "${WORK_DIR}/openapi.yaml" \
--http-user-agent="vrchatapi-py"

# Stamp version and fix metadata (Echo to trim whitespace)
perl -pi -e "s/VERSION = \"1.0.0\"/VERSION = \"$VERSION\"/" ./setup.py
perl -pi -e "s/__version__ = \"1.0.0\"/__version__ = \"$VERSION\"/" ./vrchatapi/__init__.py
perl -pi -e "s/description=\"VRChat API Documentation\"/description=\"$DESCRIPTION\"/" ./setup.py
perl -pi -e "s/keywords=\[\"OpenAPI\", \"OpenAPI-Generator\", \"VRChat API Documentation\"\]/keywords=$KEYWORDS/" ./setup.py
# author/author_email come from the spec's info.contact by default; override
# them here so they stay stable regardless of upstream spec changes.
perl -pi -e "s/author=\"[^\"]*\"/author=\"$AUTHOR\"/" ./setup.py
# @ would be treated as array interpolation inside double-quoted perl
# replacement strings, so escape it before substituting.
perl -pi -e "s/author_email=\"[^\"]*\"/author_email=\"${AUTHOR_EMAIL//@/\\@}\"/" ./setup.py
# Declare the supported Python floor (matches the CI test matrix 3.10-3.14).
perl -pi -e 's/^    install_requires=REQUIRES,$/    install_requires=REQUIRES,\n    python_requires=">=3.10",/' ./setup.py

# Fix long_description error during pypi upload
perl -pi -e 's/.*VRChat API Banner.*/abcdefvrc/g' ./setup.py
perl -pi -e 'if (/abcdefvrc/) { local $/; open(my $fh, "<", "README.md") or die $!; my $content = <$fh>; close $fh; $_ = $content; }' ./setup.py
perl -pi -e 's/abcdefvrc//g' ./setup.py

# Remove messily pasted markdown at top of every file
find vrchatapi -type f -exec perl -ni -e 'print unless /VRChat API Banner/' {} \;

# Keep hand-maintained files from being overwritten on regeneration
for entry in README.md test/ .travis.yml .gitignore pyproject.toml .github/workflows/python.yml git_push.sh vrchatapi/websocket.py; do
  grep -qxF "$entry" .openapi-generator-ignore || echo "$entry" >> .openapi-generator-ignore
done

# Restore the hand-written WebSocket (Pipeline) client. The generator does not
# emit it, so it is copied from the canonical hand-maintained source after the
# generated tree is produced. The copy-back runs even with --no-patch so the
# pristine baseline is a faithful picture of the full pipeline output.
cp websocket/websocket.py vrchatapi/websocket.py

# Stop here for the pristine baseline: exactly the state the `patch` steps
# below operate on. Useful for rewriting patches when upstream changes.
if [ "${NO_PATCH}" -eq 1 ]; then
  echo "Skipping patches/ and model post-processing (--no-patch): pristine baseline generated."
  exit 0
fi

# Enable Global cookies (aiohttp) and async rest fixes
patch ./vrchatapi/rest.py < ./patches/rest_async.patch

# Build the SSL context lazily to keep disk I/O off consumers' event loops
patch ./vrchatapi/rest.py < ./patches/lazy_ssl.patch

# Make 2fa required error readable
patch ./vrchatapi/api_client.py < ./patches/2fa_verify_readable.patch

# Move generated file I/O off the event loop and await serialization helpers
patch ./vrchatapi/api_client.py < ./patches/async_file_io.patch
python3 ./tools/make_api_methods_async.py vrchatapi/api

# Add common symbols to safe path parameter symbols
patch ./vrchatapi/configuration.py < ./patches/safe_param_symbols.patch

# Add URL encoding to basic auth parameters
patch ./vrchatapi/configuration.py < ./patches/encode_basic_auth.patch

# Fix invalid enum identifier produced from the spec's full-width '+' in image/svg+xml
patch ./vrchatapi/models/mime_type.py < ./patches/mime_type_fix.patch

# Remove backup files created by `patch` when hunks apply at an offset
find vrchatapi -type f -name '*.orig' -delete

# Make generated models tolerant of null/missing fields like python-legacy
python3 ./tools/make_models_lenient.py vrchatapi/models

# Test dependencies
printf 'pytest-asyncio >= 0.23.0\n' >> ./test-requirements.txt
