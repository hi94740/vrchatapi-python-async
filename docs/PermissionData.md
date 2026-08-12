# PermissionData

Specific values afforded the user by this permission

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badges** | **List[str]** | Badges afforded the user by this permission | [optional] 
**max** | **int** | Maximum value afforded the user by this permission | [optional] 
**max_favorite_groups** | **Dict[str, int]** | Maximum favorite groups afforded the user by this permission | [optional] 
**max_favorites_per_group** | **Dict[str, int]** | Maximum favorites per group afforded the user by this permission | [optional] 
**tags** | **List[str]** | Tags afforded the user by this permission | [optional] 

## Example

```python
from vrchatapi.models.permission_data import PermissionData

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionData from a JSON string
permission_data_instance = PermissionData.from_json(json)
# print the JSON string representation of the object
print(PermissionData.to_json())

# convert the object into a dict
permission_data_dict = permission_data_instance.to_dict()
# create an instance of PermissionData from a dict
permission_data_from_dict = PermissionData.from_dict(permission_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


