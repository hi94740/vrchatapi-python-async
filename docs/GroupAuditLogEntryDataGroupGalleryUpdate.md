# GroupAuditLogEntryDataGroupGalleryUpdate

Carries only the fields the update changed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members_only** | [**GroupAuditLogEntryBooleanChange**](GroupAuditLogEntryBooleanChange.md) |  | [optional] 
**name** | [**GroupAuditLogEntryStringChange**](GroupAuditLogEntryStringChange.md) |  | [optional] 

## Example

```python
from vrchatapi.models.group_audit_log_entry_data_group_gallery_update import GroupAuditLogEntryDataGroupGalleryUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of GroupAuditLogEntryDataGroupGalleryUpdate from a JSON string
group_audit_log_entry_data_group_gallery_update_instance = GroupAuditLogEntryDataGroupGalleryUpdate.from_json(json)
# print the JSON string representation of the object
print(GroupAuditLogEntryDataGroupGalleryUpdate.to_json())

# convert the object into a dict
group_audit_log_entry_data_group_gallery_update_dict = group_audit_log_entry_data_group_gallery_update_instance.to_dict()
# create an instance of GroupAuditLogEntryDataGroupGalleryUpdate from a dict
group_audit_log_entry_data_group_gallery_update_from_dict = GroupAuditLogEntryDataGroupGalleryUpdate.from_dict(group_audit_log_entry_data_group_gallery_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


