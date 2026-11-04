# GroupAuditLogEntryStringChange

A text field's value before and after an update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new** | **str** |  | 
**old** | **str** |  | 

## Example

```python
from vrchatapi.models.group_audit_log_entry_string_change import GroupAuditLogEntryStringChange

# TODO update the JSON string below
json = "{}"
# create an instance of GroupAuditLogEntryStringChange from a JSON string
group_audit_log_entry_string_change_instance = GroupAuditLogEntryStringChange.from_json(json)
# print the JSON string representation of the object
print(GroupAuditLogEntryStringChange.to_json())

# convert the object into a dict
group_audit_log_entry_string_change_dict = group_audit_log_entry_string_change_instance.to_dict()
# create an instance of GroupAuditLogEntryStringChange from a dict
group_audit_log_entry_string_change_from_dict = GroupAuditLogEntryStringChange.from_dict(group_audit_log_entry_string_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


