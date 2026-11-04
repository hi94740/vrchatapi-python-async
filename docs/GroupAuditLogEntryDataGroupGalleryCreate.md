# GroupAuditLogEntryDataGroupGalleryCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The gallery description. | 
**members_only** | **bool** | Whether the gallery is members only. | 
**name** | **str** | The gallery name. | 
**role_ids_to_auto_approve** | **List[str]** | The role IDs whose submissions are approved automatically. | 
**role_ids_to_manage** | **List[str]** | The role IDs that can manage the gallery. | 
**role_ids_to_submit** | **List[str]** | The role IDs that can submit to the gallery. | 
**role_ids_to_view** | **List[str]** | The role IDs that can view the gallery. | 

## Example

```python
from vrchatapi.models.group_audit_log_entry_data_group_gallery_create import GroupAuditLogEntryDataGroupGalleryCreate

# TODO update the JSON string below
json = "{}"
# create an instance of GroupAuditLogEntryDataGroupGalleryCreate from a JSON string
group_audit_log_entry_data_group_gallery_create_instance = GroupAuditLogEntryDataGroupGalleryCreate.from_json(json)
# print the JSON string representation of the object
print(GroupAuditLogEntryDataGroupGalleryCreate.to_json())

# convert the object into a dict
group_audit_log_entry_data_group_gallery_create_dict = group_audit_log_entry_data_group_gallery_create_instance.to_dict()
# create an instance of GroupAuditLogEntryDataGroupGalleryCreate from a dict
group_audit_log_entry_data_group_gallery_create_from_dict = GroupAuditLogEntryDataGroupGalleryCreate.from_dict(group_audit_log_entry_data_group_gallery_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


