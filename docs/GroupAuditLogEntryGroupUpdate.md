# GroupAuditLogEntryGroupUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor_display_name** | **str** | The display name of the user who performed the action. | 
**actor_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**created_at** | **datetime** | When the action was performed. | 
**description** | **str** | A human-readable description of the event. | 
**group_id** | **str** |  | 
**id** | **str** |  | 
**data** | [**GroupAuditLogEntryDataGroupUpdate**](GroupAuditLogEntryDataGroupUpdate.md) |  | 
**event_type** | **str** |  | 
**target_id** | **str** |  | 

## Example

```python
from vrchatapi.models.group_audit_log_entry_group_update import GroupAuditLogEntryGroupUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of GroupAuditLogEntryGroupUpdate from a JSON string
group_audit_log_entry_group_update_instance = GroupAuditLogEntryGroupUpdate.from_json(json)
# print the JSON string representation of the object
print(GroupAuditLogEntryGroupUpdate.to_json())

# convert the object into a dict
group_audit_log_entry_group_update_dict = group_audit_log_entry_group_update_instance.to_dict()
# create an instance of GroupAuditLogEntryGroupUpdate from a dict
group_audit_log_entry_group_update_from_dict = GroupAuditLogEntryGroupUpdate.from_dict(group_audit_log_entry_group_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


