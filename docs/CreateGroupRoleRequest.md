# CreateGroupRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**is_self_assignable** | **bool** |  | [optional] [default to False]
**name** | **str** |  | [optional] 
**permissions** | [**List[GroupPermissions]**](GroupPermissions.md) |  | [optional] 

## Example

```python
from vrchatapi.models.create_group_role_request import CreateGroupRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGroupRoleRequest from a JSON string
create_group_role_request_instance = CreateGroupRoleRequest.from_json(json)
# print the JSON string representation of the object
print(CreateGroupRoleRequest.to_json())

# convert the object into a dict
create_group_role_request_dict = create_group_role_request_instance.to_dict()
# create an instance of CreateGroupRoleRequest from a dict
create_group_role_request_from_dict = CreateGroupRoleRequest.from_dict(create_group_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


