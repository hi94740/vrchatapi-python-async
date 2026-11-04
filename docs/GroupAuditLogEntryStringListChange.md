# GroupAuditLogEntryStringListChange

A list field's value before and after an update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new** | **List[str]** |  | 
**old** | **List[str]** |  | 

## Example

```python
from vrchatapi.models.group_audit_log_entry_string_list_change import GroupAuditLogEntryStringListChange

# TODO update the JSON string below
json = "{}"
# create an instance of GroupAuditLogEntryStringListChange from a JSON string
group_audit_log_entry_string_list_change_instance = GroupAuditLogEntryStringListChange.from_json(json)
# print the JSON string representation of the object
print(GroupAuditLogEntryStringListChange.to_json())

# convert the object into a dict
group_audit_log_entry_string_list_change_dict = group_audit_log_entry_string_list_change_instance.to_dict()
# create an instance of GroupAuditLogEntryStringListChange from a dict
group_audit_log_entry_string_list_change_from_dict = GroupAuditLogEntryStringListChange.from_dict(group_audit_log_entry_string_list_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


