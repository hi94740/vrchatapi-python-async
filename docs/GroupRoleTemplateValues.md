# GroupRoleTemplateValues


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_permissions** | [**List[GroupPermissions]**](GroupPermissions.md) |  | 
**description** | **str** |  | 
**name** | **str** |  | 
**roles** | [**GroupRoleTemplateValuesRoles**](GroupRoleTemplateValuesRoles.md) |  | 

## Example

```python
from vrchatapi.models.group_role_template_values import GroupRoleTemplateValues

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRoleTemplateValues from a JSON string
group_role_template_values_instance = GroupRoleTemplateValues.from_json(json)
# print the JSON string representation of the object
print(GroupRoleTemplateValues.to_json())

# convert the object into a dict
group_role_template_values_dict = group_role_template_values_instance.to_dict()
# create an instance of GroupRoleTemplateValues from a dict
group_role_template_values_from_dict = GroupRoleTemplateValues.from_dict(group_role_template_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


