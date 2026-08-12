# InventoryDefaultAttributesValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_value** | **str** |  | [optional] 
**validator** | [**InventoryDefaultAttributesValueValidator**](InventoryDefaultAttributesValueValidator.md) |  | [optional] 

## Example

```python
from vrchatapi.models.inventory_default_attributes_value import InventoryDefaultAttributesValue

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryDefaultAttributesValue from a JSON string
inventory_default_attributes_value_instance = InventoryDefaultAttributesValue.from_json(json)
# print the JSON string representation of the object
print(InventoryDefaultAttributesValue.to_json())

# convert the object into a dict
inventory_default_attributes_value_dict = inventory_default_attributes_value_instance.to_dict()
# create an instance of InventoryDefaultAttributesValue from a dict
inventory_default_attributes_value_from_dict = InventoryDefaultAttributesValue.from_dict(inventory_default_attributes_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


