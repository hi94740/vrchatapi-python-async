# UpdateGroupRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**is_self_assignable** | **bool** |  | [optional] [default to False]
**name** | **str** |  | [optional] 
**order** | **int** |  | [optional] 
**permissions** | [**List[GroupPermissions]**](GroupPermissions.md) |  | [optional] 

## Example

```python
from vrchatapi.models.update_group_role_request import UpdateGroupRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGroupRoleRequest from a JSON string
update_group_role_request_instance = UpdateGroupRoleRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateGroupRoleRequest.to_json())

# convert the object into a dict
update_group_role_request_dict = update_group_role_request_instance.to_dict()
# create an instance of UpdateGroupRoleRequest from a dict
update_group_role_request_from_dict = UpdateGroupRoleRequest.from_dict(update_group_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


