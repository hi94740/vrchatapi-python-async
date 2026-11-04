# GroupAuditLogEntryDataGroupMemberUserUpdate

Carries only the fields the update changed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manager_notes** | [**GroupAuditLogEntryStringChange**](GroupAuditLogEntryStringChange.md) |  | [optional] 

## Example

```python
from vrchatapi.models.group_audit_log_entry_data_group_member_user_update import GroupAuditLogEntryDataGroupMemberUserUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of GroupAuditLogEntryDataGroupMemberUserUpdate from a JSON string
group_audit_log_entry_data_group_member_user_update_instance = GroupAuditLogEntryDataGroupMemberUserUpdate.from_json(json)
# print the JSON string representation of the object
print(GroupAuditLogEntryDataGroupMemberUserUpdate.to_json())

# convert the object into a dict
group_audit_log_entry_data_group_member_user_update_dict = group_audit_log_entry_data_group_member_user_update_instance.to_dict()
# create an instance of GroupAuditLogEntryDataGroupMemberUserUpdate from a dict
group_audit_log_entry_data_group_member_user_update_from_dict = GroupAuditLogEntryDataGroupMemberUserUpdate.from_dict(group_audit_log_entry_data_group_member_user_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


