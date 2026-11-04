# GroupAuditLogEntryDataGroupMemberRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **str** |  | 
**role_name** | **str** | The name of the role that was assigned or unassigned. | 

## Example

```python
from vrchatapi.models.group_audit_log_entry_data_group_member_role import GroupAuditLogEntryDataGroupMemberRole

# TODO update the JSON string below
json = "{}"
# create an instance of GroupAuditLogEntryDataGroupMemberRole from a JSON string
group_audit_log_entry_data_group_member_role_instance = GroupAuditLogEntryDataGroupMemberRole.from_json(json)
# print the JSON string representation of the object
print(GroupAuditLogEntryDataGroupMemberRole.to_json())

# convert the object into a dict
group_audit_log_entry_data_group_member_role_dict = group_audit_log_entry_data_group_member_role_instance.to_dict()
# create an instance of GroupAuditLogEntryDataGroupMemberRole from a dict
group_audit_log_entry_data_group_member_role_from_dict = GroupAuditLogEntryDataGroupMemberRole.from_dict(group_audit_log_entry_data_group_member_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


