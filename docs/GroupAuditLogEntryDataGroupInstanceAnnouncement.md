# GroupAuditLogEntryDataGroupInstanceAnnouncement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The announcement message. | 
**title** | **str** | The announcement title. | 

## Example

```python
from vrchatapi.models.group_audit_log_entry_data_group_instance_announcement import GroupAuditLogEntryDataGroupInstanceAnnouncement

# TODO update the JSON string below
json = "{}"
# create an instance of GroupAuditLogEntryDataGroupInstanceAnnouncement from a JSON string
group_audit_log_entry_data_group_instance_announcement_instance = GroupAuditLogEntryDataGroupInstanceAnnouncement.from_json(json)
# print the JSON string representation of the object
print(GroupAuditLogEntryDataGroupInstanceAnnouncement.to_json())

# convert the object into a dict
group_audit_log_entry_data_group_instance_announcement_dict = group_audit_log_entry_data_group_instance_announcement_instance.to_dict()
# create an instance of GroupAuditLogEntryDataGroupInstanceAnnouncement from a dict
group_audit_log_entry_data_group_instance_announcement_from_dict = GroupAuditLogEntryDataGroupInstanceAnnouncement.from_dict(group_audit_log_entry_data_group_instance_announcement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


