# GroupAuditLogEntryDataGroupPostCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**image_id** | **str** |  | 
**text** | **str** | The text content of the post. | 
**title** | **str** | The title of the post. | 
**visibility** | [**GroupPostVisibility**](GroupPostVisibility.md) |  | 
**role_ids** | **List[str]** | The role IDs that can see the post. | 
**send_notification** | **bool** | Whether a notification was sent for this post. | 

## Example

```python
from vrchatapi.models.group_audit_log_entry_data_group_post_create import GroupAuditLogEntryDataGroupPostCreate

# TODO update the JSON string below
json = "{}"
# create an instance of GroupAuditLogEntryDataGroupPostCreate from a JSON string
group_audit_log_entry_data_group_post_create_instance = GroupAuditLogEntryDataGroupPostCreate.from_json(json)
# print the JSON string representation of the object
print(GroupAuditLogEntryDataGroupPostCreate.to_json())

# convert the object into a dict
group_audit_log_entry_data_group_post_create_dict = group_audit_log_entry_data_group_post_create_instance.to_dict()
# create an instance of GroupAuditLogEntryDataGroupPostCreate from a dict
group_audit_log_entry_data_group_post_create_from_dict = GroupAuditLogEntryDataGroupPostCreate.from_dict(group_audit_log_entry_data_group_post_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


