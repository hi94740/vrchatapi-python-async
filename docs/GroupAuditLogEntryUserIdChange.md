# GroupAuditLogEntryUserIdChange

A user ID field's value before and after an update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**old** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 

## Example

```python
from vrchatapi.models.group_audit_log_entry_user_id_change import GroupAuditLogEntryUserIdChange

# TODO update the JSON string below
json = "{}"
# create an instance of GroupAuditLogEntryUserIdChange from a JSON string
group_audit_log_entry_user_id_change_instance = GroupAuditLogEntryUserIdChange.from_json(json)
# print the JSON string representation of the object
print(GroupAuditLogEntryUserIdChange.to_json())

# convert the object into a dict
group_audit_log_entry_user_id_change_dict = group_audit_log_entry_user_id_change_instance.to_dict()
# create an instance of GroupAuditLogEntryUserIdChange from a dict
group_audit_log_entry_user_id_change_from_dict = GroupAuditLogEntryUserIdChange.from_dict(group_audit_log_entry_user_id_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


