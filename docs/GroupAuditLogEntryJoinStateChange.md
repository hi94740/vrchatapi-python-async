# GroupAuditLogEntryJoinStateChange

A join state field's value before and after an update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new** | [**GroupJoinState**](GroupJoinState.md) |  | [default to GroupJoinState.OPEN]
**old** | [**GroupJoinState**](GroupJoinState.md) |  | [default to GroupJoinState.OPEN]

## Example

```python
from vrchatapi.models.group_audit_log_entry_join_state_change import GroupAuditLogEntryJoinStateChange

# TODO update the JSON string below
json = "{}"
# create an instance of GroupAuditLogEntryJoinStateChange from a JSON string
group_audit_log_entry_join_state_change_instance = GroupAuditLogEntryJoinStateChange.from_json(json)
# print the JSON string representation of the object
print(GroupAuditLogEntryJoinStateChange.to_json())

# convert the object into a dict
group_audit_log_entry_join_state_change_dict = group_audit_log_entry_join_state_change_instance.to_dict()
# create an instance of GroupAuditLogEntryJoinStateChange from a dict
group_audit_log_entry_join_state_change_from_dict = GroupAuditLogEntryJoinStateChange.from_dict(group_audit_log_entry_join_state_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


