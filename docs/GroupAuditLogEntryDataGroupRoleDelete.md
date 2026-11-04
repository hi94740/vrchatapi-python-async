# GroupAuditLogEntryDataGroupRoleDelete


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The role description. | 
**is_added_on_join** | **bool** | Whether the role is automatically assigned on join. | 
**is_self_assignable** | **bool** | Whether users can self-assign this role. | 
**name** | **str** | The role name. | 
**order** | **int** | The display order of the role. | [optional] 
**permissions** | [**List[GroupPermissions]**](GroupPermissions.md) | The permissions assigned to this role. | 
**requires_purchase** | **bool** | Whether the role requires a purchase. | 
**requires_two_factor** | **bool** | Whether the role requires two-factor authentication. | 
**created_at** | **datetime** | The creation timestamp of the role. | 
**default_role** | **bool** | Whether the role is the group&#39;s default role. | 
**is_management_role** | **bool** | Whether the role is a management role. | 

## Example

```python
from vrchatapi.models.group_audit_log_entry_data_group_role_delete import GroupAuditLogEntryDataGroupRoleDelete

# TODO update the JSON string below
json = "{}"
# create an instance of GroupAuditLogEntryDataGroupRoleDelete from a JSON string
group_audit_log_entry_data_group_role_delete_instance = GroupAuditLogEntryDataGroupRoleDelete.from_json(json)
# print the JSON string representation of the object
print(GroupAuditLogEntryDataGroupRoleDelete.to_json())

# convert the object into a dict
group_audit_log_entry_data_group_role_delete_dict = group_audit_log_entry_data_group_role_delete_instance.to_dict()
# create an instance of GroupAuditLogEntryDataGroupRoleDelete from a dict
group_audit_log_entry_data_group_role_delete_from_dict = GroupAuditLogEntryDataGroupRoleDelete.from_dict(group_audit_log_entry_data_group_role_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


