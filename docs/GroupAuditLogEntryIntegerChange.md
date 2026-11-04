# GroupAuditLogEntryIntegerChange

An integer field's value before and after an update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new** | **int** |  | 
**old** | **int** |  | 

## Example

```python
from vrchatapi.models.group_audit_log_entry_integer_change import GroupAuditLogEntryIntegerChange

# TODO update the JSON string below
json = "{}"
# create an instance of GroupAuditLogEntryIntegerChange from a JSON string
group_audit_log_entry_integer_change_instance = GroupAuditLogEntryIntegerChange.from_json(json)
# print the JSON string representation of the object
print(GroupAuditLogEntryIntegerChange.to_json())

# convert the object into a dict
group_audit_log_entry_integer_change_dict = group_audit_log_entry_integer_change_instance.to_dict()
# create an instance of GroupAuditLogEntryIntegerChange from a dict
group_audit_log_entry_integer_change_from_dict = GroupAuditLogEntryIntegerChange.from_dict(group_audit_log_entry_integer_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


