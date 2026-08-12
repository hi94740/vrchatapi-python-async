# GroupRoleTemplateValuesRoles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**base_permissions** | [**List[GroupPermissions]**](GroupPermissions.md) |  | [optional] 
**is_added_on_join** | **bool** |  | [optional] [default to False]

## Example

```python
from vrchatapi.models.group_role_template_values_roles import GroupRoleTemplateValuesRoles

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRoleTemplateValuesRoles from a JSON string
group_role_template_values_roles_instance = GroupRoleTemplateValuesRoles.from_json(json)
# print the JSON string representation of the object
print(GroupRoleTemplateValuesRoles.to_json())

# convert the object into a dict
group_role_template_values_roles_dict = group_role_template_values_roles_instance.to_dict()
# create an instance of GroupRoleTemplateValuesRoles from a dict
group_role_template_values_roles_from_dict = GroupRoleTemplateValuesRoles.from_dict(group_role_template_values_roles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


