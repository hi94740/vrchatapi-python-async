# GroupAuditLogEntryDataGroupAnnouncement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**image_id** | **str** |  | 
**send_notification** | **bool** | Whether a notification was sent for this announcement. | 
**text** | **str** | The text content of the announcement. | 
**title** | **str** | The title of the announcement. | 

## Example

```python
from vrchatapi.models.group_audit_log_entry_data_group_announcement import GroupAuditLogEntryDataGroupAnnouncement

# TODO update the JSON string below
json = "{}"
# create an instance of GroupAuditLogEntryDataGroupAnnouncement from a JSON string
group_audit_log_entry_data_group_announcement_instance = GroupAuditLogEntryDataGroupAnnouncement.from_json(json)
# print the JSON string representation of the object
print(GroupAuditLogEntryDataGroupAnnouncement.to_json())

# convert the object into a dict
group_audit_log_entry_data_group_announcement_dict = group_audit_log_entry_data_group_announcement_instance.to_dict()
# create an instance of GroupAuditLogEntryDataGroupAnnouncement from a dict
group_audit_log_entry_data_group_announcement_from_dict = GroupAuditLogEntryDataGroupAnnouncement.from_dict(group_audit_log_entry_data_group_announcement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


