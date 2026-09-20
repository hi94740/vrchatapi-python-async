# UserCosmetic

A cosmetic a user holds, without the template's presentation fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acquired_on** | **datetime** |  | 
**acquisition** | **str** |  | 
**id** | **str** |  | 
**item_type** | [**InventoryItemType**](InventoryItemType.md) |  | [default to InventoryItemType.BUNDLE]
**template_id** | **str** |  | 
**user_attributes** | [**InventoryUserAttributes**](InventoryUserAttributes.md) |  | 

## Example

```python
from vrchatapi.models.user_cosmetic import UserCosmetic

# TODO update the JSON string below
json = "{}"
# create an instance of UserCosmetic from a JSON string
user_cosmetic_instance = UserCosmetic.from_json(json)
# print the JSON string representation of the object
print(UserCosmetic.to_json())

# convert the object into a dict
user_cosmetic_dict = user_cosmetic_instance.to_dict()
# create an instance of UserCosmetic from a dict
user_cosmetic_from_dict = UserCosmetic.from_dict(user_cosmetic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


