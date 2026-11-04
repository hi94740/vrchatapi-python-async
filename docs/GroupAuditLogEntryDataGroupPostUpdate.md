# GroupAuditLogEntryDataGroupPostUpdate

Carries only the fields the update changed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**editor_id** | [**GroupAuditLogEntryUserIdChange**](GroupAuditLogEntryUserIdChange.md) |  | [optional] 
**text** | [**GroupAuditLogEntryStringChange**](GroupAuditLogEntryStringChange.md) |  | [optional] 
**title** | [**GroupAuditLogEntryStringChange**](GroupAuditLogEntryStringChange.md) |  | [optional] 

## Example

```python
from vrchatapi.models.group_audit_log_entry_data_group_post_update import GroupAuditLogEntryDataGroupPostUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of GroupAuditLogEntryDataGroupPostUpdate from a JSON string
group_audit_log_entry_data_group_post_update_instance = GroupAuditLogEntryDataGroupPostUpdate.from_json(json)
# print the JSON string representation of the object
print(GroupAuditLogEntryDataGroupPostUpdate.to_json())

# convert the object into a dict
group_audit_log_entry_data_group_post_update_dict = group_audit_log_entry_data_group_post_update_instance.to_dict()
# create an instance of GroupAuditLogEntryDataGroupPostUpdate from a dict
group_audit_log_entry_data_group_post_update_from_dict = GroupAuditLogEntryDataGroupPostUpdate.from_dict(group_audit_log_entry_data_group_post_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


