# GroupAuditLogEntryDataGroupRoleUpdate

Carries only the fields the update changed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | [**GroupAuditLogEntryStringChange**](GroupAuditLogEntryStringChange.md) |  | [optional] 
**is_added_on_join** | [**GroupAuditLogEntryBooleanChange**](GroupAuditLogEntryBooleanChange.md) |  | [optional] 
**is_self_assignable** | [**GroupAuditLogEntryBooleanChange**](GroupAuditLogEntryBooleanChange.md) |  | [optional] 
**name** | [**GroupAuditLogEntryStringChange**](GroupAuditLogEntryStringChange.md) |  | [optional] 
**order** | [**GroupAuditLogEntryIntegerChange**](GroupAuditLogEntryIntegerChange.md) |  | [optional] 
**permissions** | [**GroupAuditLogEntryStringListChange**](GroupAuditLogEntryStringListChange.md) |  | [optional] 
**requires_two_factor** | [**GroupAuditLogEntryBooleanChange**](GroupAuditLogEntryBooleanChange.md) |  | [optional] 

## Example

```python
from vrchatapi.models.group_audit_log_entry_data_group_role_update import GroupAuditLogEntryDataGroupRoleUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of GroupAuditLogEntryDataGroupRoleUpdate from a JSON string
group_audit_log_entry_data_group_role_update_instance = GroupAuditLogEntryDataGroupRoleUpdate.from_json(json)
# print the JSON string representation of the object
print(GroupAuditLogEntryDataGroupRoleUpdate.to_json())

# convert the object into a dict
group_audit_log_entry_data_group_role_update_dict = group_audit_log_entry_data_group_role_update_instance.to_dict()
# create an instance of GroupAuditLogEntryDataGroupRoleUpdate from a dict
group_audit_log_entry_data_group_role_update_from_dict = GroupAuditLogEntryDataGroupRoleUpdate.from_dict(group_audit_log_entry_data_group_role_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


