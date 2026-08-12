# vrchatapi.InventoryApi

All URIs are relative to *https://api.vrchat.cloud/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**consume_own_inventory_item**](InventoryApi.md#consume_own_inventory_item) | **PUT** /inventory/{inventoryItemId}/consume | Consume Own Inventory Item
[**delete_own_inventory_item**](InventoryApi.md#delete_own_inventory_item) | **DELETE** /inventory/{inventoryItemId} | Delete Own Inventory Item
[**equip_own_inventory_item**](InventoryApi.md#equip_own_inventory_item) | **PUT** /inventory/{inventoryItemId}/equip | Equip Own Inventory Item
[**get_inventory**](InventoryApi.md#get_inventory) | **GET** /inventory | Get Inventory
[**get_inventory_collections**](InventoryApi.md#get_inventory_collections) | **GET** /inventory/collections | List Inventory Collections
[**get_inventory_drops**](InventoryApi.md#get_inventory_drops) | **GET** /inventory/drops | List Inventory Drops
[**get_inventory_template**](InventoryApi.md#get_inventory_template) | **GET** /inventory/template/{inventoryTemplateId} | Get Inventory Template
[**get_own_inventory_item**](InventoryApi.md#get_own_inventory_item) | **GET** /inventory/{inventoryItemId} | Get Own Inventory Item
[**get_user_inventory_item**](InventoryApi.md#get_user_inventory_item) | **GET** /user/{userId}/inventory/{inventoryItemId} | Get User Inventory Item
[**redeem_reward**](InventoryApi.md#redeem_reward) | **POST** /reward/redeem | Redeem Reward
[**share_inventory_item_direct**](InventoryApi.md#share_inventory_item_direct) | **POST** /inventory/cloning/direct | Share Inventory Item Direct
[**share_inventory_item_pedestal**](InventoryApi.md#share_inventory_item_pedestal) | **GET** /inventory/cloning/pedestal | Share Inventory Item by Pedestal
[**spawn_inventory_item**](InventoryApi.md#spawn_inventory_item) | **GET** /inventory/spawn | Spawn Inventory Item
[**unequip_own_inventory_slot**](InventoryApi.md#unequip_own_inventory_slot) | **DELETE** /inventory/{inventoryItemId}/equip | Unequip Own Inventory Slot
[**update_own_inventory_item**](InventoryApi.md#update_own_inventory_item) | **PUT** /inventory/{inventoryItemId} | Update Own Inventory Item


# **consume_own_inventory_item**
> InventoryConsumptionResults consume_own_inventory_item(inventory_item_id)

Consume Own Inventory Item

Returns the modified InventoryItem object as held by the currently logged in user.

### Example

* Api Key Authentication (authCookie):

```python
import vrchatapi
from vrchatapi.models.inventory_consumption_results import InventoryConsumptionResults
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
    api_instance = vrchatapi.InventoryApi(api_client)
    inventory_item_id = 'inventory_item_id_example' # str | Must be a valid inventory item ID.

    try:
        # Consume Own Inventory Item
        api_response = await api_instance.consume_own_inventory_item(inventory_item_id)
        print("The response of InventoryApi->consume_own_inventory_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->consume_own_inventory_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_item_id** | **str**| Must be a valid inventory item ID. | 

### Return type

[**InventoryConsumptionResults**](InventoryConsumptionResults.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an InventoryConsumptionResults object. |  -  |
**400** | Error response when trying to consume an InventoryItem lacking the consumable flag. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_own_inventory_item**
> SuccessFlag delete_own_inventory_item(inventory_item_id)

Delete Own Inventory Item

Deletes an InventoryItem from the inventory of the currently logged in user.

### Example

* Api Key Authentication (authCookie):

```python
import vrchatapi
from vrchatapi.models.success_flag import SuccessFlag
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
    api_instance = vrchatapi.InventoryApi(api_client)
    inventory_item_id = 'inventory_item_id_example' # str | Must be a valid inventory item ID.

    try:
        # Delete Own Inventory Item
        api_response = await api_instance.delete_own_inventory_item(inventory_item_id)
        print("The response of InventoryApi->delete_own_inventory_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->delete_own_inventory_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_item_id** | **str**| Must be a valid inventory item ID. | 

### Return type

[**SuccessFlag**](SuccessFlag.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an SuccessFlag object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **equip_own_inventory_item**
> InventoryItem equip_own_inventory_item(inventory_item_id, equip_inventory_item_request=equip_inventory_item_request)

Equip Own Inventory Item

Returns the modified InventoryItem object as held by the currently logged in user.

### Example

* Api Key Authentication (authCookie):

```python
import vrchatapi
from vrchatapi.models.equip_inventory_item_request import EquipInventoryItemRequest
from vrchatapi.models.inventory_item import InventoryItem
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
    api_instance = vrchatapi.InventoryApi(api_client)
    inventory_item_id = 'inventory_item_id_example' # str | Must be a valid inventory item ID.
    equip_inventory_item_request = vrchatapi.EquipInventoryItemRequest() # EquipInventoryItemRequest |  (optional)

    try:
        # Equip Own Inventory Item
        api_response = await api_instance.equip_own_inventory_item(inventory_item_id, equip_inventory_item_request=equip_inventory_item_request)
        print("The response of InventoryApi->equip_own_inventory_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->equip_own_inventory_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_item_id** | **str**| Must be a valid inventory item ID. | 
 **equip_inventory_item_request** | [**EquipInventoryItemRequest**](EquipInventoryItemRequest.md)|  | [optional] 

### Return type

[**InventoryItem**](InventoryItem.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an InventoryItem object. |  -  |
**400** | Error response when trying to equip an InventoryItem lacking the equippable flag. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory**
> Inventory get_inventory(n=n, offset=offset, holder_id=holder_id, equip_slot=equip_slot, order=order, tags=tags, types=types, flags=flags, not_types=not_types, not_flags=not_flags, archived=archived)

Get Inventory

Returns an Inventory object.

### Example

* Api Key Authentication (authCookie):

```python
import vrchatapi
from vrchatapi.models.inventory import Inventory
from vrchatapi.models.inventory_equip_slot import InventoryEquipSlot
from vrchatapi.models.inventory_flag import InventoryFlag
from vrchatapi.models.inventory_item_type import InventoryItemType
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
    api_instance = vrchatapi.InventoryApi(api_client)
    n = 60 # int | The number of objects to return. (optional) (default to 60)
    offset = 56 # int | A zero-based offset from the default object sorting from where search results start. (optional)
    holder_id = 'holder_id_example' # str | The UserID of the owner of the inventory; defaults to the currently authenticated user. (optional)
    equip_slot = '' # InventoryEquipSlot | Filter for inventory retrieval. (optional) (default to '')
    order = 'order_example' # str | Sort order for inventory retrieval. (optional)
    tags = 'tags_example' # str | Filter tags for inventory retrieval (comma-separated). (optional)
    types = 'bundle' # InventoryItemType | Filter for inventory retrieval. (optional) (default to 'bundle')
    flags = 'instantiatable' # InventoryFlag | Filter flags for inventory retrieval (comma-separated). (optional) (default to 'instantiatable')
    not_types = 'bundle' # InventoryItemType | Filter out types for inventory retrieval (comma-separated). (optional) (default to 'bundle')
    not_flags = 'instantiatable' # InventoryFlag | Filter out flags for inventory retrieval (comma-separated). (optional) (default to 'instantiatable')
    archived = True # bool | Filter archived status for inventory retrieval. (optional)

    try:
        # Get Inventory
        api_response = await api_instance.get_inventory(n=n, offset=offset, holder_id=holder_id, equip_slot=equip_slot, order=order, tags=tags, types=types, flags=flags, not_types=not_types, not_flags=not_flags, archived=archived)
        print("The response of InventoryApi->get_inventory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->get_inventory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **n** | **int**| The number of objects to return. | [optional] [default to 60]
 **offset** | **int**| A zero-based offset from the default object sorting from where search results start. | [optional] 
 **holder_id** | **str**| The UserID of the owner of the inventory; defaults to the currently authenticated user. | [optional] 
 **equip_slot** | [**InventoryEquipSlot**](.md)| Filter for inventory retrieval. | [optional] [default to &#39;&#39;]
 **order** | **str**| Sort order for inventory retrieval. | [optional] 
 **tags** | **str**| Filter tags for inventory retrieval (comma-separated). | [optional] 
 **types** | [**InventoryItemType**](.md)| Filter for inventory retrieval. | [optional] [default to &#39;bundle&#39;]
 **flags** | [**InventoryFlag**](.md)| Filter flags for inventory retrieval (comma-separated). | [optional] [default to &#39;instantiatable&#39;]
 **not_types** | [**InventoryItemType**](.md)| Filter out types for inventory retrieval (comma-separated). | [optional] [default to &#39;bundle&#39;]
 **not_flags** | [**InventoryFlag**](.md)| Filter out flags for inventory retrieval (comma-separated). | [optional] [default to &#39;instantiatable&#39;]
 **archived** | **bool**| Filter archived status for inventory retrieval. | [optional] 

### Return type

[**Inventory**](Inventory.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an Inventory object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |
**403** | Error response due to missing permissions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory_collections**
> List[str] get_inventory_collections()

List Inventory Collections

Returns a list of collection names.

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
    api_instance = vrchatapi.InventoryApi(api_client)

    try:
        # List Inventory Collections
        api_response = await api_instance.get_inventory_collections()
        print("The response of InventoryApi->get_inventory_collections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->get_inventory_collections: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[str]**

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of strings. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory_drops**
> List[InventoryDrop] get_inventory_drops(active=active)

List Inventory Drops

Returns a list of InventoryDrop objects.

### Example

* Api Key Authentication (authCookie):

```python
import vrchatapi
from vrchatapi.models.inventory_drop import InventoryDrop
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
    api_instance = vrchatapi.InventoryApi(api_client)
    active = True # bool | Filter for users' listings and inventory bundles. (optional)

    try:
        # List Inventory Drops
        api_response = await api_instance.get_inventory_drops(active=active)
        print("The response of InventoryApi->get_inventory_drops:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->get_inventory_drops: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **bool**| Filter for users&#39; listings and inventory bundles. | [optional] 

### Return type

[**List[InventoryDrop]**](InventoryDrop.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of InventoryDrop objects. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory_template**
> InventoryTemplate get_inventory_template(inventory_template_id)

Get Inventory Template

Returns an InventoryTemplate object.

### Example

* Api Key Authentication (authCookie):

```python
import vrchatapi
from vrchatapi.models.inventory_template import InventoryTemplate
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
    api_instance = vrchatapi.InventoryApi(api_client)
    inventory_template_id = 'inventory_template_id_example' # str | Must be a valid inventory template ID.

    try:
        # Get Inventory Template
        api_response = await api_instance.get_inventory_template(inventory_template_id)
        print("The response of InventoryApi->get_inventory_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->get_inventory_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_template_id** | **str**| Must be a valid inventory template ID. | 

### Return type

[**InventoryTemplate**](InventoryTemplate.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an InventoryTemplate object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_own_inventory_item**
> InventoryItem get_own_inventory_item(inventory_item_id)

Get Own Inventory Item

Returns an InventoryItem object held by the currently logged in user.

### Example

* Api Key Authentication (authCookie):

```python
import vrchatapi
from vrchatapi.models.inventory_item import InventoryItem
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
    api_instance = vrchatapi.InventoryApi(api_client)
    inventory_item_id = 'inventory_item_id_example' # str | Must be a valid inventory item ID.

    try:
        # Get Own Inventory Item
        api_response = await api_instance.get_own_inventory_item(inventory_item_id)
        print("The response of InventoryApi->get_own_inventory_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->get_own_inventory_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_item_id** | **str**| Must be a valid inventory item ID. | 

### Return type

[**InventoryItem**](InventoryItem.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an InventoryItem object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_inventory_item**
> InventoryItem get_user_inventory_item(user_id, inventory_item_id)

Get User Inventory Item

Returns an InventoryItem object held by the given user.

### Example

* Api Key Authentication (authCookie):

```python
import vrchatapi
from vrchatapi.models.inventory_item import InventoryItem
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
    api_instance = vrchatapi.InventoryApi(api_client)
    user_id = 'user_id_example' # str | Must be a valid user ID.
    inventory_item_id = 'inventory_item_id_example' # str | Must be a valid inventory item ID.

    try:
        # Get User Inventory Item
        api_response = await api_instance.get_user_inventory_item(user_id, inventory_item_id)
        print("The response of InventoryApi->get_user_inventory_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->get_user_inventory_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Must be a valid user ID. | 
 **inventory_item_id** | **str**| Must be a valid inventory item ID. | 

### Return type

[**InventoryItem**](InventoryItem.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an InventoryItem object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redeem_reward**
> List[RewardRedemptionResult] redeem_reward(reward_redemption_request)

Redeem Reward

Redeem a reward for the currently logged in user.

### Example

* Api Key Authentication (authCookie):

```python
import vrchatapi
from vrchatapi.models.reward_redemption_request import RewardRedemptionRequest
from vrchatapi.models.reward_redemption_result import RewardRedemptionResult
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
    api_instance = vrchatapi.InventoryApi(api_client)
    reward_redemption_request = vrchatapi.RewardRedemptionRequest() # RewardRedemptionRequest | 

    try:
        # Redeem Reward
        api_response = await api_instance.redeem_reward(reward_redemption_request)
        print("The response of InventoryApi->redeem_reward:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->redeem_reward: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reward_redemption_request** | [**RewardRedemptionRequest**](RewardRedemptionRequest.md)|  | 

### Return type

[**List[RewardRedemptionResult]**](RewardRedemptionResult.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single RewardRedemptionResult object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **share_inventory_item_direct**
> OkStatus share_inventory_item_direct(item_id, duration, share_inventory_item_direct_request)

Share Inventory Item Direct

Share content directly with other users.

### Example

* Api Key Authentication (authCookie):

```python
import vrchatapi
from vrchatapi.models.ok_status import OkStatus
from vrchatapi.models.share_inventory_item_direct_request import ShareInventoryItemDirectRequest
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
    api_instance = vrchatapi.InventoryApi(api_client)
    item_id = 'item_id_example' # str | Id for inventory item sharing.
    duration = 90 # int | The duration before the sharing pedestal despawns. (default to 90)
    share_inventory_item_direct_request = vrchatapi.ShareInventoryItemDirectRequest() # ShareInventoryItemDirectRequest | 

    try:
        # Share Inventory Item Direct
        api_response = await api_instance.share_inventory_item_direct(item_id, duration, share_inventory_item_direct_request)
        print("The response of InventoryApi->share_inventory_item_direct:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->share_inventory_item_direct: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Id for inventory item sharing. | 
 **duration** | **int**| The duration before the sharing pedestal despawns. | [default to 90]
 **share_inventory_item_direct_request** | [**ShareInventoryItemDirectRequest**](ShareInventoryItemDirectRequest.md)|  | 

### Return type

[**OkStatus**](OkStatus.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an OkStatus object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **share_inventory_item_pedestal**
> InventorySpawn share_inventory_item_pedestal(item_id, duration)

Share Inventory Item by Pedestal

Returns an InventorySpawn object.

### Example

* Api Key Authentication (authCookie):

```python
import vrchatapi
from vrchatapi.models.inventory_spawn import InventorySpawn
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
    api_instance = vrchatapi.InventoryApi(api_client)
    item_id = 'item_id_example' # str | Id for inventory item sharing.
    duration = 90 # int | The duration before the sharing pedestal despawns. (default to 90)

    try:
        # Share Inventory Item by Pedestal
        api_response = await api_instance.share_inventory_item_pedestal(item_id, duration)
        print("The response of InventoryApi->share_inventory_item_pedestal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->share_inventory_item_pedestal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| Id for inventory item sharing. | 
 **duration** | **int**| The duration before the sharing pedestal despawns. | [default to 90]

### Return type

[**InventorySpawn**](InventorySpawn.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an InventorySpawn object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spawn_inventory_item**
> InventorySpawn spawn_inventory_item(id)

Spawn Inventory Item

Returns an InventorySpawn object.

### Example

* Api Key Authentication (authCookie):

```python
import vrchatapi
from vrchatapi.models.inventory_spawn import InventorySpawn
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
    api_instance = vrchatapi.InventoryApi(api_client)
    id = 'id_example' # str | Id for inventory item spawning.

    try:
        # Spawn Inventory Item
        api_response = await api_instance.spawn_inventory_item(id)
        print("The response of InventoryApi->spawn_inventory_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->spawn_inventory_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id for inventory item spawning. | 

### Return type

[**InventorySpawn**](InventorySpawn.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an InventorySpawn object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unequip_own_inventory_slot**
> str unequip_own_inventory_slot(inventory_item_id)

Unequip Own Inventory Slot

Unequips the InventoryItem in the given slot of the inventory of the currently logged in user.

### Example

* Api Key Authentication (authCookie):

```python
import vrchatapi
from vrchatapi.models.inventory_equip_slot import InventoryEquipSlot
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
    api_instance = vrchatapi.InventoryApi(api_client)
    inventory_item_id = '' # InventoryEquipSlot | Selector for inventory slot management. (default to '')

    try:
        # Unequip Own Inventory Slot
        api_response = await api_instance.unequip_own_inventory_slot(inventory_item_id)
        print("The response of InventoryApi->unequip_own_inventory_slot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->unequip_own_inventory_slot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_item_id** | [**InventoryEquipSlot**](.md)| Selector for inventory slot management. | [default to &#39;&#39;]

### Return type

**str**

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a string. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_own_inventory_item**
> InventoryItem update_own_inventory_item(inventory_item_id, update_inventory_item_request=update_inventory_item_request)

Update Own Inventory Item

Returns the modified InventoryItem object as held by the currently logged in user.

### Example

* Api Key Authentication (authCookie):

```python
import vrchatapi
from vrchatapi.models.inventory_item import InventoryItem
from vrchatapi.models.update_inventory_item_request import UpdateInventoryItemRequest
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
    api_instance = vrchatapi.InventoryApi(api_client)
    inventory_item_id = 'inventory_item_id_example' # str | Must be a valid inventory item ID.
    update_inventory_item_request = vrchatapi.UpdateInventoryItemRequest() # UpdateInventoryItemRequest |  (optional)

    try:
        # Update Own Inventory Item
        api_response = await api_instance.update_own_inventory_item(inventory_item_id, update_inventory_item_request=update_inventory_item_request)
        print("The response of InventoryApi->update_own_inventory_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->update_own_inventory_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_item_id** | **str**| Must be a valid inventory item ID. | 
 **update_inventory_item_request** | [**UpdateInventoryItemRequest**](UpdateInventoryItemRequest.md)|  | [optional] 

### Return type

[**InventoryItem**](InventoryItem.md)

### Authorization

[authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an InventoryItem object. |  -  |
**401** | Error response due to missing auth cookie. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

