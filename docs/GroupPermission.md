# GroupPermission

A permission that can be granted to a role in a group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_to_add** | **bool** | Whether the user is allowed to add this permission to a role. | [optional] [default to False]
**display_name** | **str** | The display name of the permission. | [optional] 
**help** | **str** | Human-readable description of the permission. | [optional] 
**is_management_permission** | **bool** | Whether this permission is a \&quot;management\&quot; permission. | [optional] [default to False]
**name** | **str** | The name of the permission. | [optional] 

## Example

```python
from vrchatapi.models.group_permission import GroupPermission

# TODO update the JSON string below
json = "{}"
# create an instance of GroupPermission from a JSON string
group_permission_instance = GroupPermission.from_json(json)
# print the JSON string representation of the object
print(GroupPermission.to_json())

# convert the object into a dict
group_permission_dict = group_permission_instance.to_dict()
# create an instance of GroupPermission from a dict
group_permission_from_dict = GroupPermission.from_dict(group_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


