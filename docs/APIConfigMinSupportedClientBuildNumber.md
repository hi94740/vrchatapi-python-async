# APIConfigMinSupportedClientBuildNumber

Minimum supported client build number for various platforms

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_store** | [**PlatformBuildInfo**](PlatformBuildInfo.md) |  | 
**default** | [**PlatformBuildInfo**](PlatformBuildInfo.md) |  | 
**firebase** | [**PlatformBuildInfo**](PlatformBuildInfo.md) |  | 
**firebasei_os** | [**PlatformBuildInfo**](PlatformBuildInfo.md) |  | 
**google_play** | [**PlatformBuildInfo**](PlatformBuildInfo.md) |  | 
**pc** | [**PlatformBuildInfo**](PlatformBuildInfo.md) |  | 
**pico_store** | [**PlatformBuildInfo**](PlatformBuildInfo.md) |  | 
**quest_app_lab** | [**PlatformBuildInfo**](PlatformBuildInfo.md) |  | 
**quest_store** | [**PlatformBuildInfo**](PlatformBuildInfo.md) |  | 
**test_flight** | [**PlatformBuildInfo**](PlatformBuildInfo.md) |  | 
**xr_elite** | [**PlatformBuildInfo**](PlatformBuildInfo.md) |  | 

## Example

```python
from vrchatapi.models.api_config_min_supported_client_build_number import APIConfigMinSupportedClientBuildNumber

# TODO update the JSON string below
json = "{}"
# create an instance of APIConfigMinSupportedClientBuildNumber from a JSON string
api_config_min_supported_client_build_number_instance = APIConfigMinSupportedClientBuildNumber.from_json(json)
# print the JSON string representation of the object
print(APIConfigMinSupportedClientBuildNumber.to_json())

# convert the object into a dict
api_config_min_supported_client_build_number_dict = api_config_min_supported_client_build_number_instance.to_dict()
# create an instance of APIConfigMinSupportedClientBuildNumber from a dict
api_config_min_supported_client_build_number_from_dict = APIConfigMinSupportedClientBuildNumber.from_dict(api_config_min_supported_client_build_number_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


