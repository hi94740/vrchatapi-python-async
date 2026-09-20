# GroupRoleTemplateRole

A role a group role template creates alongside the everyone role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**is_added_on_join** | **bool** |  | [optional] [default to False]
**name** | **str** |  | 
**permissions** | [**List[GroupPermissions]**](GroupPermissions.md) |  | 

## Example

```python
from vrchatapi.models.group_role_template_role import GroupRoleTemplateRole

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRoleTemplateRole from a JSON string
group_role_template_role_instance = GroupRoleTemplateRole.from_json(json)
# print the JSON string representation of the object
print(GroupRoleTemplateRole.to_json())

# convert the object into a dict
group_role_template_role_dict = group_role_template_role_instance.to_dict()
# create an instance of GroupRoleTemplateRole from a dict
group_role_template_role_from_dict = GroupRoleTemplateRole.from_dict(group_role_template_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


