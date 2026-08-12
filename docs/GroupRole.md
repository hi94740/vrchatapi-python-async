# GroupRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**group_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**is_management_role** | **bool** |  | [optional] [default to False]
**is_self_assignable** | **bool** |  | [optional] [default to False]
**name** | **str** |  | [optional] 
**order** | **int** |  | [optional] 
**permissions** | [**List[GroupPermissions]**](GroupPermissions.md) |  | [optional] 
**requires_purchase** | **bool** |  | [optional] [default to False]
**requires_two_factor** | **bool** |  | [optional] [default to False]
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from vrchatapi.models.group_role import GroupRole

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRole from a JSON string
group_role_instance = GroupRole.from_json(json)
# print the JSON string representation of the object
print(GroupRole.to_json())

# convert the object into a dict
group_role_dict = group_role_instance.to_dict()
# create an instance of GroupRole from a dict
group_role_from_dict = GroupRole.from_dict(group_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


