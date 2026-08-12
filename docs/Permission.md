# Permission



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PermissionData**](PermissionData.md) |  | [optional] 
**description** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**id** | **str** |  | 
**name** | **str** |  | 
**owner_display_name** | **str** |  | 
**owner_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**type** | **str** |  | [optional] 

## Example

```python
from vrchatapi.models.permission import Permission

# TODO update the JSON string below
json = "{}"
# create an instance of Permission from a JSON string
permission_instance = Permission.from_json(json)
# print the JSON string representation of the object
print(Permission.to_json())

# convert the object into a dict
permission_dict = permission_instance.to_dict()
# create an instance of Permission from a dict
permission_from_dict = Permission.from_dict(permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


