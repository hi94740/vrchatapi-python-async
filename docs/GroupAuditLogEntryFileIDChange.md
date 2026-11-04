# GroupAuditLogEntryFileIDChange

A File ID field's value before and after an update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new** | **str** |  | 
**old** | **str** |  | 

## Example

```python
from vrchatapi.models.group_audit_log_entry_file_id_change import GroupAuditLogEntryFileIDChange

# TODO update the JSON string below
json = "{}"
# create an instance of GroupAuditLogEntryFileIDChange from a JSON string
group_audit_log_entry_file_id_change_instance = GroupAuditLogEntryFileIDChange.from_json(json)
# print the JSON string representation of the object
print(GroupAuditLogEntryFileIDChange.to_json())

# convert the object into a dict
group_audit_log_entry_file_id_change_dict = group_audit_log_entry_file_id_change_instance.to_dict()
# create an instance of GroupAuditLogEntryFileIDChange from a dict
group_audit_log_entry_file_id_change_from_dict = GroupAuditLogEntryFileIDChange.from_dict(group_audit_log_entry_file_id_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


