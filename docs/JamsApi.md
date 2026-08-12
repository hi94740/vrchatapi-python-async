# vrchatapi.JamsApi

All URIs are relative to *https://api.vrchat.cloud/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_jam_submission**](JamsApi.md#delete_jam_submission) | **DELETE** /jams/{jamId}/submissions/{jamSubmissionId} | Delete Jam Submission
[**get_jam**](JamsApi.md#get_jam) | **GET** /jams/{jamId} | Show jam information
[**get_jam_submissions**](JamsApi.md#get_jam_submissions) | **GET** /jams/{jamId}/submissions | Show jam submissions
[**get_jams**](JamsApi.md#get_jams) | **GET** /jams | Show jams list
[**submit_jam_content**](JamsApi.md#submit_jam_content) | **POST** /jams/{jamId}/submissions | Submit Jam Content


# **delete_jam_submission**
> Success delete_jam_submission(jam_id, jam_submission_id)

Delete Jam Submission

Withdraws a content submission from a jam.

### Example

* Api Key Authentication (authCookie):

```python
import vrchatapi
from vrchatapi.models.success import Success
from vrchatapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.vrchat.cloud/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://api.vrchat.cloud/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authCookie
configuration.api_key['authCookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authCookie'] = 'Bearer'

# Enter a context with an instance of the API client
async with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vrchatapi.JamsApi(api_client)
    jam_id = 'jam_id_example' # str | Must be a valid jam ID.
    jam_submission_id = 'jam_submission_id_example' # str | Must be a valid jam submission ID.

    try:
        # Delete Jam Submission
        api_response = await api_instance.delete_jam_submission(jam_id, jam_submission_id)
        print("The response of JamsApi->delete_jam_submission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JamsApi->delete_jam_submission: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jam_id** | **str**| Must be a valid jam ID. | 
 **jam_submission_id** | **str**| Must be a valid jam submission ID. | 

### Return type

[**Success**](Success.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an Success object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**403** | Error response due to missing permissions. |  -  |
**404** | Error response when trying to show information about a non-existent jam. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jam**
> Jam get_jam(jam_id)

Show jam information

Returns a jam.

### Example

* Api Key Authentication (authCookie):

```python
import vrchatapi
from vrchatapi.models.jam import Jam
from vrchatapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.vrchat.cloud/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://api.vrchat.cloud/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authCookie
configuration.api_key['authCookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authCookie'] = 'Bearer'

# Enter a context with an instance of the API client
async with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vrchatapi.JamsApi(api_client)
    jam_id = 'jam_id_example' # str | Must be a valid jam ID.

    try:
        # Show jam information
        api_response = await api_instance.get_jam(jam_id)
        print("The response of JamsApi->get_jam:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JamsApi->get_jam: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jam_id** | **str**| Must be a valid jam ID. | 

### Return type

[**Jam**](Jam.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Jam object. |  -  |
**404** | Error response when trying to show information about a non-existent jam. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jam_submissions**
> List[JamSubmission] get_jam_submissions(jam_id, content_id=content_id, submitter_id=submitter_id)

Show jam submissions

Returns all submissions of a jam. Can filter by contentId (for world or avatar jams) or submitterId (for a participant).

### Example

* Api Key Authentication (authCookie):

```python
import vrchatapi
from vrchatapi.models.jam_submission import JamSubmission
from vrchatapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.vrchat.cloud/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://api.vrchat.cloud/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authCookie
configuration.api_key['authCookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authCookie'] = 'Bearer'

# Enter a context with an instance of the API client
async with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vrchatapi.JamsApi(api_client)
    jam_id = 'jam_id_example' # str | Must be a valid jam ID.
    content_id = 'content_id_example' # str | Filter for particular content submitted, e.g., a groupId, userId, avatarId, etc. (optional)
    submitter_id = 'submitter_id_example' # str | Must be a valid user ID. (optional)

    try:
        # Show jam submissions
        api_response = await api_instance.get_jam_submissions(jam_id, content_id=content_id, submitter_id=submitter_id)
        print("The response of JamsApi->get_jam_submissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JamsApi->get_jam_submissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jam_id** | **str**| Must be a valid jam ID. | 
 **content_id** | **str**| Filter for particular content submitted, e.g., a groupId, userId, avatarId, etc. | [optional] 
 **submitter_id** | **str**| Must be a valid user ID. | [optional] 

### Return type

[**List[JamSubmission]**](JamSubmission.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of JamSubmission objects. |  -  |
**404** | Error response when trying to show information about a non-existent jam. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jams**
> List[Jam] get_jams(type=type)

Show jams list

Lists World Jams or Avatar Jams, both currently running and ones that have ended.

`isActive` is used to select only active or already ended jams.

`type` is used to select only world or avatar jams, and can only take `world` or `avatar`.
``

### Example

* Api Key Authentication (authCookie):

```python
import vrchatapi
from vrchatapi.models.jam import Jam
from vrchatapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.vrchat.cloud/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://api.vrchat.cloud/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authCookie
configuration.api_key['authCookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authCookie'] = 'Bearer'

# Enter a context with an instance of the API client
async with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vrchatapi.JamsApi(api_client)
    type = 'avatar' # str | Only show jams of this type (`avatar` or `world`). (optional)

    try:
        # Show jams list
        api_response = await api_instance.get_jams(type=type)
        print("The response of JamsApi->get_jams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JamsApi->get_jams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Only show jams of this type (&#x60;avatar&#x60; or &#x60;world&#x60;). | [optional] 

### Return type

[**List[Jam]**](Jam.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of Jam objects. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_jam_content**
> JamSubmission submit_jam_content(jam_id, create_jam_submission_request=create_jam_submission_request)

Submit Jam Content

Submits content to a jam. The content must have been uploaded by the submitter, and both the content upload and jam submission must be made within the jam's designated times.

### Example

* Api Key Authentication (authCookie):

```python
import vrchatapi
from vrchatapi.models.create_jam_submission_request import CreateJamSubmissionRequest
from vrchatapi.models.jam_submission import JamSubmission
from vrchatapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.vrchat.cloud/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://api.vrchat.cloud/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authCookie
configuration.api_key['authCookie'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authCookie'] = 'Bearer'

# Enter a context with an instance of the API client
async with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vrchatapi.JamsApi(api_client)
    jam_id = 'jam_id_example' # str | Must be a valid jam ID.
    create_jam_submission_request = vrchatapi.CreateJamSubmissionRequest() # CreateJamSubmissionRequest |  (optional)

    try:
        # Submit Jam Content
        api_response = await api_instance.submit_jam_content(jam_id, create_jam_submission_request=create_jam_submission_request)
        print("The response of JamsApi->submit_jam_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JamsApi->submit_jam_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jam_id** | **str**| Must be a valid jam ID. | 
 **create_jam_submission_request** | [**CreateJamSubmissionRequest**](CreateJamSubmissionRequest.md)|  | [optional] 

### Return type

[**JamSubmission**](JamSubmission.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single JamSubmission object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to show information about a non-existent jam. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

