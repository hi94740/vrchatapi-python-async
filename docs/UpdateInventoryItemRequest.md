# UpdateInventoryItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_archived** | **bool** |  | [optional] 
**is_seen** | **bool** |  | [optional] 
**user_attributes** | [**InventoryUserAttributes**](InventoryUserAttributes.md) |  | [optional] 

## Example

```python
from vrchatapi.models.update_inventory_item_request import UpdateInventoryItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInventoryItemRequest from a JSON string
update_inventory_item_request_instance = UpdateInventoryItemRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateInventoryItemRequest.to_json())

# convert the object into a dict
update_inventory_item_request_dict = update_inventory_item_request_instance.to_dict()
# create an instance of UpdateInventoryItemRequest from a dict
update_inventory_item_request_from_dict = UpdateInventoryItemRequest.from_dict(update_inventory_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


