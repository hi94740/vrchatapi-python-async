# StoreShelf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**highlight_listing** | [**ProductListing**](ProductListing.md) |  | [optional] 
**highlight_listing_id** | **str** |  | [optional] 
**id** | **str** |  | 
**listing_ids** | **List[str]** |  | 
**listings** | [**List[ProductListing]**](ProductListing.md) |  | [optional] 
**shelf_description** | **str** |  | 
**shelf_layout** | **str** |  | 
**shelf_title** | **str** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from vrchatapi.models.store_shelf import StoreShelf

# TODO update the JSON string below
json = "{}"
# create an instance of StoreShelf from a JSON string
store_shelf_instance = StoreShelf.from_json(json)
# print the JSON string representation of the object
print(StoreShelf.to_json())

# convert the object into a dict
store_shelf_dict = store_shelf_instance.to_dict()
# create an instance of StoreShelf from a dict
store_shelf_from_dict = StoreShelf.from_dict(store_shelf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


