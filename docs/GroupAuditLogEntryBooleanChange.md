# GroupAuditLogEntryBooleanChange

A boolean field's value before and after an update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new** | **bool** |  | 
**old** | **bool** |  | 

## Example

```python
from vrchatapi.models.group_audit_log_entry_boolean_change import GroupAuditLogEntryBooleanChange

# TODO update the JSON string below
json = "{}"
# create an instance of GroupAuditLogEntryBooleanChange from a JSON string
group_audit_log_entry_boolean_change_instance = GroupAuditLogEntryBooleanChange.from_json(json)
# print the JSON string representation of the object
print(GroupAuditLogEntryBooleanChange.to_json())

# convert the object into a dict
group_audit_log_entry_boolean_change_dict = group_audit_log_entry_boolean_change_instance.to_dict()
# create an instance of GroupAuditLogEntryBooleanChange from a dict
group_audit_log_entry_boolean_change_from_dict = GroupAuditLogEntryBooleanChange.from_dict(group_audit_log_entry_boolean_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


