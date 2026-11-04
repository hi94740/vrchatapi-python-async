# GroupAuditLogEntryDataGroupUpdate

Carries only the fields the update changed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_group_join_prompt** | [**GroupAuditLogEntryBooleanChange**](GroupAuditLogEntryBooleanChange.md) |  | [optional] 
**banner_id** | [**GroupAuditLogEntryFileIDChange**](GroupAuditLogEntryFileIDChange.md) |  | [optional] 
**description** | [**GroupAuditLogEntryStringChange**](GroupAuditLogEntryStringChange.md) |  | [optional] 
**icon_id** | [**GroupAuditLogEntryFileIDChange**](GroupAuditLogEntryFileIDChange.md) |  | [optional] 
**join_state** | [**GroupAuditLogEntryJoinStateChange**](GroupAuditLogEntryJoinStateChange.md) |  | [optional] 
**languages** | [**GroupAuditLogEntryStringListChange**](GroupAuditLogEntryStringListChange.md) |  | [optional] 
**links** | [**GroupAuditLogEntryStringListChange**](GroupAuditLogEntryStringListChange.md) |  | [optional] 
**name** | [**GroupAuditLogEntryStringChange**](GroupAuditLogEntryStringChange.md) |  | [optional] 
**nameplate_id** | [**GroupAuditLogEntryFileIDChange**](GroupAuditLogEntryFileIDChange.md) |  | [optional] 
**rules** | [**GroupAuditLogEntryStringChange**](GroupAuditLogEntryStringChange.md) |  | [optional] 
**short_code** | [**GroupAuditLogEntryStringChange**](GroupAuditLogEntryStringChange.md) |  | [optional] 
**tags** | [**GroupAuditLogEntryStringListChange**](GroupAuditLogEntryStringListChange.md) |  | [optional] 

## Example

```python
from vrchatapi.models.group_audit_log_entry_data_group_update import GroupAuditLogEntryDataGroupUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of GroupAuditLogEntryDataGroupUpdate from a JSON string
group_audit_log_entry_data_group_update_instance = GroupAuditLogEntryDataGroupUpdate.from_json(json)
# print the JSON string representation of the object
print(GroupAuditLogEntryDataGroupUpdate.to_json())

# convert the object into a dict
group_audit_log_entry_data_group_update_dict = group_audit_log_entry_data_group_update_instance.to_dict()
# create an instance of GroupAuditLogEntryDataGroupUpdate from a dict
group_audit_log_entry_data_group_update_from_dict = GroupAuditLogEntryDataGroupUpdate.from_dict(group_audit_log_entry_data_group_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


