# GroupAuditLogEntryDataGroupGalleryDelete


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
**created_at** | **datetime** | The creation timestamp of the gallery. | 
**updated_at** | **datetime** | The last update timestamp of the gallery. | 

## Example

```python
from vrchatapi.models.group_audit_log_entry_data_group_gallery_delete import GroupAuditLogEntryDataGroupGalleryDelete

# TODO update the JSON string below
json = "{}"
# create an instance of GroupAuditLogEntryDataGroupGalleryDelete from a JSON string
group_audit_log_entry_data_group_gallery_delete_instance = GroupAuditLogEntryDataGroupGalleryDelete.from_json(json)
# print the JSON string representation of the object
print(GroupAuditLogEntryDataGroupGalleryDelete.to_json())

# convert the object into a dict
group_audit_log_entry_data_group_gallery_delete_dict = group_audit_log_entry_data_group_gallery_delete_instance.to_dict()
# create an instance of GroupAuditLogEntryDataGroupGalleryDelete from a dict
group_audit_log_entry_data_group_gallery_delete_from_dict = GroupAuditLogEntryDataGroupGalleryDelete.from_dict(group_audit_log_entry_data_group_gallery_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


