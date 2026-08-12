# Store


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] 
**description** | **str** |  | 
**display_name** | **str** |  | 
**group_id** | **str** |  | [optional] 
**id** | **str** |  | 
**listing_ids** | **List[str]** | Only for store type world and group | [optional] 
**listings** | [**List[ProductListing]**](ProductListing.md) | Only for store type world and group | [optional] 
**seller_display_name** | **str** |  | 
**seller_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**shelf_ids** | **List[str]** | Only for store type house | [optional] 
**shelves** | [**List[StoreShelf]**](StoreShelf.md) | Only for store type house | [optional] 
**store_context** | [**StoreContext**](StoreContext.md) |  | [optional] 
**store_id** | **str** |  | 
**store_status** | **str** |  | [optional] 
**store_type** | [**StoreType**](StoreType.md) |  | [default to StoreType.GROUP]
**tags** | **List[str]** |  | 
**updated** | **datetime** |  | [optional] 
**world_id** | **str** | WorldID be \&quot;offline\&quot; on User profiles if you are not friends with that user. | [optional] 

## Example

```python
from vrchatapi.models.store import Store

# TODO update the JSON string below
json = "{}"
# create an instance of Store from a JSON string
store_instance = Store.from_json(json)
# print the JSON string representation of the object
print(Store.to_json())

# convert the object into a dict
store_dict = store_instance.to_dict()
# create an instance of Store from a dict
store_from_dict = Store.from_dict(store_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


