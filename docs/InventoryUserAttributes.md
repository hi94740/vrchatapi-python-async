# InventoryUserAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_color** | **str** |  | [optional] 
**secondary_color** | **str** |  | [optional] 
**trail_color** | **str** |  | [optional] 

## Example

```python
from vrchatapi.models.inventory_user_attributes import InventoryUserAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryUserAttributes from a JSON string
inventory_user_attributes_instance = InventoryUserAttributes.from_json(json)
# print the JSON string representation of the object
print(InventoryUserAttributes.to_json())

# convert the object into a dict
inventory_user_attributes_dict = inventory_user_attributes_instance.to_dict()
# create an instance of InventoryUserAttributes from a dict
inventory_user_attributes_from_dict = InventoryUserAttributes.from_dict(inventory_user_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


