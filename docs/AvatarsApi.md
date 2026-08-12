# vrchatapi.AvatarsApi

All URIs are relative to *https://api.vrchat.cloud/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_avatar**](AvatarsApi.md#create_avatar) | **POST** /avatars | Create Avatar
[**delete_avatar**](AvatarsApi.md#delete_avatar) | **DELETE** /avatars/{avatarId} | Delete Avatar
[**delete_impostor**](AvatarsApi.md#delete_impostor) | **DELETE** /avatars/{avatarId}/impostor | Delete generated Impostor
[**enqueue_impostor**](AvatarsApi.md#enqueue_impostor) | **POST** /avatars/{avatarId}/impostor/enqueue | Enqueue Impostor generation
[**get_avatar**](AvatarsApi.md#get_avatar) | **GET** /avatars/{avatarId} | Get Avatar
[**get_avatar_styles**](AvatarsApi.md#get_avatar_styles) | **GET** /avatarStyles | Get Avatar Styles
[**get_favorited_avatars**](AvatarsApi.md#get_favorited_avatars) | **GET** /avatars/favorites | List Favorited Avatars
[**get_impostor_queue_stats**](AvatarsApi.md#get_impostor_queue_stats) | **GET** /avatars/impostor/queue/stats | Get Impostor Queue Stats
[**get_licensed_avatars**](AvatarsApi.md#get_licensed_avatars) | **GET** /avatars/licensed | List Licensed Avatars
[**get_own_avatar**](AvatarsApi.md#get_own_avatar) | **GET** /users/{userId}/avatar | Get Own Avatar
[**search_avatars**](AvatarsApi.md#search_avatars) | **GET** /avatars | Search Avatars
[**select_avatar**](AvatarsApi.md#select_avatar) | **PUT** /avatars/{avatarId}/select | Select Avatar
[**select_fallback_avatar**](AvatarsApi.md#select_fallback_avatar) | **PUT** /avatars/{avatarId}/selectFallback | Select Fallback Avatar
[**update_avatar**](AvatarsApi.md#update_avatar) | **PUT** /avatars/{avatarId} | Update Avatar


# **create_avatar**
> Avatar create_avatar(create_avatar_request=create_avatar_request)

Create Avatar

Create an avatar. It's possible to optionally specify a ID if you want a custom one. Attempting to create an Avatar with an already claimed ID will result in a DB error.

### Example

* Api Key Authentication (authCookie):

```python
import vrchatapi
from vrchatapi.models.avatar import Avatar
from vrchatapi.models.create_avatar_request import CreateAvatarRequest
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
    api_instance = vrchatapi.AvatarsApi(api_client)
    create_avatar_request = vrchatapi.CreateAvatarRequest() # CreateAvatarRequest |  (optional)

    try:
        # Create Avatar
        api_response = await api_instance.create_avatar(create_avatar_request=create_avatar_request)
        print("The response of AvatarsApi->create_avatar:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvatarsApi->create_avatar: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_avatar_request** | [**CreateAvatarRequest**](CreateAvatarRequest.md)|  | [optional] 

### Return type

[**Avatar**](Avatar.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single Avatar object. |  -  |
**400** | Error response due to missing permissions. |  -  |
**401** | Error response when set featured to true without being an admin. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_avatar**
> Avatar delete_avatar(avatar_id)

Delete Avatar

Delete an avatar. Notice an avatar is never fully "deleted", only its ReleaseStatus is set to "hidden" and the linked Files are deleted. The AvatarID is permanently reserved.

### Example

* Api Key Authentication (authCookie):

```python
import vrchatapi
from vrchatapi.models.avatar import Avatar
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
    api_instance = vrchatapi.AvatarsApi(api_client)
    avatar_id = 'avatar_id_example' # str | Must be a valid avatar ID.

    try:
        # Delete Avatar
        api_response = await api_instance.delete_avatar(avatar_id)
        print("The response of AvatarsApi->delete_avatar:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvatarsApi->delete_avatar: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avatar_id** | **str**| Must be a valid avatar ID. | 

### Return type

[**Avatar**](Avatar.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single Avatar object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to show information about a non-existent avatar. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_impostor**
> delete_impostor(avatar_id)

Delete generated Impostor

Delete generated Impostor for that avatar.

### Example

* Api Key Authentication (authCookie):

```python
import vrchatapi
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
    api_instance = vrchatapi.AvatarsApi(api_client)
    avatar_id = 'avatar_id_example' # str | Must be a valid avatar ID.

    try:
        # Delete generated Impostor
        await api_instance.delete_impostor(avatar_id)
    except Exception as e:
        print("Exception when calling AvatarsApi->delete_impostor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avatar_id** | **str**| Must be a valid avatar ID. | 

### Return type

void (empty response body)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Impostors generated for that avatar are deleted. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to show information about a non-existent avatar. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enqueue_impostor**
> ServiceStatus enqueue_impostor(avatar_id)

Enqueue Impostor generation

Enqueue Impostor generation for that avatar.

### Example

* Api Key Authentication (authCookie):

```python
import vrchatapi
from vrchatapi.models.service_status import ServiceStatus
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
    api_instance = vrchatapi.AvatarsApi(api_client)
    avatar_id = 'avatar_id_example' # str | Must be a valid avatar ID.

    try:
        # Enqueue Impostor generation
        api_response = await api_instance.enqueue_impostor(avatar_id)
        print("The response of AvatarsApi->enqueue_impostor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvatarsApi->enqueue_impostor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avatar_id** | **str**| Must be a valid avatar ID. | 

### Return type

[**ServiceStatus**](ServiceStatus.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Service Status. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to show information about a non-existent avatar. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_avatar**
> Avatar get_avatar(avatar_id)

Get Avatar

Get information about a specific Avatar.

### Example

* Api Key Authentication (authCookie):

```python
import vrchatapi
from vrchatapi.models.avatar import Avatar
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
    api_instance = vrchatapi.AvatarsApi(api_client)
    avatar_id = 'avatar_id_example' # str | Must be a valid avatar ID.

    try:
        # Get Avatar
        api_response = await api_instance.get_avatar(avatar_id)
        print("The response of AvatarsApi->get_avatar:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvatarsApi->get_avatar: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avatar_id** | **str**| Must be a valid avatar ID. | 

### Return type

[**Avatar**](Avatar.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single Avatar object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to show information about a non-existent avatar. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_avatar_styles**
> List[AvatarStyle] get_avatar_styles()

Get Avatar Styles

List avatar styles.

### Example


```python
import vrchatapi
from vrchatapi.models.avatar_style import AvatarStyle
from vrchatapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.vrchat.cloud/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://api.vrchat.cloud/api/1"
)


# Enter a context with an instance of the API client
async with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vrchatapi.AvatarsApi(api_client)

    try:
        # Get Avatar Styles
        api_response = await api_instance.get_avatar_styles()
        print("The response of AvatarsApi->get_avatar_styles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvatarsApi->get_avatar_styles: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AvatarStyle]**](AvatarStyle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of AvatarStyle objects. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_favorited_avatars**
> List[Avatar] get_favorited_avatars(featured=featured, sort=sort, n=n, order=order, offset=offset, search=search, tag=tag, notag=notag, release_status=release_status, max_unity_version=max_unity_version, min_unity_version=min_unity_version, platform=platform, user_id=user_id)

List Favorited Avatars

Search and list favorited avatars by query filters.

### Example

* Api Key Authentication (authCookie):

```python
import vrchatapi
from vrchatapi.models.avatar import Avatar
from vrchatapi.models.order_option import OrderOption
from vrchatapi.models.release_status import ReleaseStatus
from vrchatapi.models.sort_option import SortOption
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
    api_instance = vrchatapi.AvatarsApi(api_client)
    featured = True # bool | Filters on featured results. (optional)
    sort = 'popularity' # SortOption | The sort order of the results. (optional) (default to 'popularity')
    n = 60 # int | The number of objects to return. (optional) (default to 60)
    order = 'descending' # OrderOption | Result ordering (optional) (default to 'descending')
    offset = 56 # int | A zero-based offset from the default object sorting from where search results start. (optional)
    search = 'search_example' # str | Filters by world name. (optional)
    tag = 'tag_example' # str | Tags to include (comma-separated). Any of the tags needs to be present. (optional)
    notag = 'notag_example' # str | Tags to exclude (comma-separated). (optional)
    release_status = 'public' # ReleaseStatus | Filter by ReleaseStatus. (optional) (default to 'public')
    max_unity_version = 'max_unity_version_example' # str | The maximum Unity version supported by the asset. (optional)
    min_unity_version = 'min_unity_version_example' # str | The minimum Unity version supported by the asset. (optional)
    platform = 'platform_example' # str | The platform the asset supports. (optional)
    user_id = 'user_id_example' # str | Target user to see information on, admin-only. (optional)

    try:
        # List Favorited Avatars
        api_response = await api_instance.get_favorited_avatars(featured=featured, sort=sort, n=n, order=order, offset=offset, search=search, tag=tag, notag=notag, release_status=release_status, max_unity_version=max_unity_version, min_unity_version=min_unity_version, platform=platform, user_id=user_id)
        print("The response of AvatarsApi->get_favorited_avatars:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvatarsApi->get_favorited_avatars: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featured** | **bool**| Filters on featured results. | [optional] 
 **sort** | [**SortOption**](.md)| The sort order of the results. | [optional] [default to &#39;popularity&#39;]
 **n** | **int**| The number of objects to return. | [optional] [default to 60]
 **order** | [**OrderOption**](.md)| Result ordering | [optional] [default to &#39;descending&#39;]
 **offset** | **int**| A zero-based offset from the default object sorting from where search results start. | [optional] 
 **search** | **str**| Filters by world name. | [optional] 
 **tag** | **str**| Tags to include (comma-separated). Any of the tags needs to be present. | [optional] 
 **notag** | **str**| Tags to exclude (comma-separated). | [optional] 
 **release_status** | [**ReleaseStatus**](.md)| Filter by ReleaseStatus. | [optional] [default to &#39;public&#39;]
 **max_unity_version** | **str**| The maximum Unity version supported by the asset. | [optional] 
 **min_unity_version** | **str**| The minimum Unity version supported by the asset. | [optional] 
 **platform** | **str**| The platform the asset supports. | [optional] 
 **user_id** | **str**| Target user to see information on, admin-only. | [optional] 

### Return type

[**List[Avatar]**](Avatar.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of Avatar objects. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**403** | Error response when trying to see favorited avatars of another user without sufficient admin permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_impostor_queue_stats**
> ServiceQueueStats get_impostor_queue_stats()

Get Impostor Queue Stats

Gets service stats for queued impostor.

### Example

* Api Key Authentication (authCookie):

```python
import vrchatapi
from vrchatapi.models.service_queue_stats import ServiceQueueStats
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
    api_instance = vrchatapi.AvatarsApi(api_client)

    try:
        # Get Impostor Queue Stats
        api_response = await api_instance.get_impostor_queue_stats()
        print("The response of AvatarsApi->get_impostor_queue_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvatarsApi->get_impostor_queue_stats: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ServiceQueueStats**](ServiceQueueStats.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Service Queue Stats. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_licensed_avatars**
> List[Avatar] get_licensed_avatars(n=n, offset=offset)

List Licensed Avatars

List licensed avatars.

### Example

* Api Key Authentication (authCookie):

```python
import vrchatapi
from vrchatapi.models.avatar import Avatar
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
    api_instance = vrchatapi.AvatarsApi(api_client)
    n = 60 # int | The number of objects to return. (optional) (default to 60)
    offset = 56 # int | A zero-based offset from the default object sorting from where search results start. (optional)

    try:
        # List Licensed Avatars
        api_response = await api_instance.get_licensed_avatars(n=n, offset=offset)
        print("The response of AvatarsApi->get_licensed_avatars:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvatarsApi->get_licensed_avatars: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **n** | **int**| The number of objects to return. | [optional] [default to 60]
 **offset** | **int**| A zero-based offset from the default object sorting from where search results start. | [optional] 

### Return type

[**List[Avatar]**](Avatar.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of Avatar objects. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_own_avatar**
> Avatar get_own_avatar(user_id)

Get Own Avatar

Get the current avatar for the user. This will return an error for any other user than the one logged in.

### Example

* Api Key Authentication (authCookie):

```python
import vrchatapi
from vrchatapi.models.avatar import Avatar
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
    api_instance = vrchatapi.AvatarsApi(api_client)
    user_id = 'user_id_example' # str | Must be a valid user ID.

    try:
        # Get Own Avatar
        api_response = await api_instance.get_own_avatar(user_id)
        print("The response of AvatarsApi->get_own_avatar:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvatarsApi->get_own_avatar: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Must be a valid user ID. | 

### Return type

[**Avatar**](Avatar.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single Avatar object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**403** | Error response when trying to see another users current avatar without sufficient admin permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_avatars**
> List[Avatar] search_avatars(featured=featured, sort=sort, user=user, user_id=user_id, n=n, order=order, offset=offset, tag=tag, notag=notag, release_status=release_status, max_unity_version=max_unity_version, min_unity_version=min_unity_version, platform=platform, is_internal_variant=is_internal_variant)

Search Avatars

Search and list avatars by query filters. You can only search your own or featured avatars. It is not possible as a normal user to search other peoples avatars.

### Example

* Api Key Authentication (authCookie):

```python
import vrchatapi
from vrchatapi.models.avatar import Avatar
from vrchatapi.models.order_option import OrderOption
from vrchatapi.models.release_status import ReleaseStatus
from vrchatapi.models.sort_option import SortOption
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
    api_instance = vrchatapi.AvatarsApi(api_client)
    featured = True # bool | Filters on featured results. (optional)
    sort = 'popularity' # SortOption | The sort order of the results. (optional) (default to 'popularity')
    user = 'user_example' # str | Set to `me` for searching own avatars. (optional)
    user_id = 'user_id_example' # str | Filter by UserID. (optional)
    n = 60 # int | The number of objects to return. (optional) (default to 60)
    order = 'descending' # OrderOption | Result ordering (optional) (default to 'descending')
    offset = 56 # int | A zero-based offset from the default object sorting from where search results start. (optional)
    tag = 'tag_example' # str | Tags to include (comma-separated). Any of the tags needs to be present. (optional)
    notag = 'notag_example' # str | Tags to exclude (comma-separated). (optional)
    release_status = 'public' # ReleaseStatus | Filter by ReleaseStatus. (optional) (default to 'public')
    max_unity_version = 'max_unity_version_example' # str | The maximum Unity version supported by the asset. (optional)
    min_unity_version = 'min_unity_version_example' # str | The minimum Unity version supported by the asset. (optional)
    platform = 'platform_example' # str | The platform the asset supports. (optional)
    is_internal_variant = false # bool | Not quite sure what this actually does (exists on the website but doesn't seem to be used) (optional)

    try:
        # Search Avatars
        api_response = await api_instance.search_avatars(featured=featured, sort=sort, user=user, user_id=user_id, n=n, order=order, offset=offset, tag=tag, notag=notag, release_status=release_status, max_unity_version=max_unity_version, min_unity_version=min_unity_version, platform=platform, is_internal_variant=is_internal_variant)
        print("The response of AvatarsApi->search_avatars:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvatarsApi->search_avatars: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **featured** | **bool**| Filters on featured results. | [optional] 
 **sort** | [**SortOption**](.md)| The sort order of the results. | [optional] [default to &#39;popularity&#39;]
 **user** | **str**| Set to &#x60;me&#x60; for searching own avatars. | [optional] 
 **user_id** | **str**| Filter by UserID. | [optional] 
 **n** | **int**| The number of objects to return. | [optional] [default to 60]
 **order** | [**OrderOption**](.md)| Result ordering | [optional] [default to &#39;descending&#39;]
 **offset** | **int**| A zero-based offset from the default object sorting from where search results start. | [optional] 
 **tag** | **str**| Tags to include (comma-separated). Any of the tags needs to be present. | [optional] 
 **notag** | **str**| Tags to exclude (comma-separated). | [optional] 
 **release_status** | [**ReleaseStatus**](.md)| Filter by ReleaseStatus. | [optional] [default to &#39;public&#39;]
 **max_unity_version** | **str**| The maximum Unity version supported by the asset. | [optional] 
 **min_unity_version** | **str**| The minimum Unity version supported by the asset. | [optional] 
 **platform** | **str**| The platform the asset supports. | [optional] 
 **is_internal_variant** | **bool**| Not quite sure what this actually does (exists on the website but doesn&#39;t seem to be used) | [optional] 

### Return type

[**List[Avatar]**](Avatar.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of Avatar objects. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **select_avatar**
> CurrentUser select_avatar(avatar_id)

Select Avatar

Switches into that avatar.

### Example

* Api Key Authentication (authCookie):

```python
import vrchatapi
from vrchatapi.models.current_user import CurrentUser
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
    api_instance = vrchatapi.AvatarsApi(api_client)
    avatar_id = 'avatar_id_example' # str | Must be a valid avatar ID.

    try:
        # Select Avatar
        api_response = await api_instance.select_avatar(avatar_id)
        print("The response of AvatarsApi->select_avatar:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvatarsApi->select_avatar: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avatar_id** | **str**| Must be a valid avatar ID. | 

### Return type

[**CurrentUser**](CurrentUser.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single CurrentUser object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to show information about a non-existent avatar. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **select_fallback_avatar**
> CurrentUser select_fallback_avatar(avatar_id)

Select Fallback Avatar

Switches into that avatar as your fallback avatar.

### Example

* Api Key Authentication (authCookie):

```python
import vrchatapi
from vrchatapi.models.current_user import CurrentUser
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
    api_instance = vrchatapi.AvatarsApi(api_client)
    avatar_id = 'avatar_id_example' # str | Must be a valid avatar ID.

    try:
        # Select Fallback Avatar
        api_response = await api_instance.select_fallback_avatar(avatar_id)
        print("The response of AvatarsApi->select_fallback_avatar:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvatarsApi->select_fallback_avatar: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avatar_id** | **str**| Must be a valid avatar ID. | 

### Return type

[**CurrentUser**](CurrentUser.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single CurrentUser object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**403** | Error response when trying to select a fallback avatar that is missing the fallback tag. |  -  |
**404** | Error response when trying to show information about a non-existent avatar. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_avatar**
> Avatar update_avatar(avatar_id, update_avatar_request=update_avatar_request)

Update Avatar

Update information about a specific avatar.

### Example

* Api Key Authentication (authCookie):

```python
import vrchatapi
from vrchatapi.models.avatar import Avatar
from vrchatapi.models.update_avatar_request import UpdateAvatarRequest
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
    api_instance = vrchatapi.AvatarsApi(api_client)
    avatar_id = 'avatar_id_example' # str | Must be a valid avatar ID.
    update_avatar_request = vrchatapi.UpdateAvatarRequest() # UpdateAvatarRequest |  (optional)

    try:
        # Update Avatar
        api_response = await api_instance.update_avatar(avatar_id, update_avatar_request=update_avatar_request)
        print("The response of AvatarsApi->update_avatar:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AvatarsApi->update_avatar: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avatar_id** | **str**| Must be a valid avatar ID. | 
 **update_avatar_request** | [**UpdateAvatarRequest**](UpdateAvatarRequest.md)|  | [optional] 

### Return type

[**Avatar**](Avatar.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single Avatar object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**404** | Error response when trying to show information about a non-existent avatar. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

