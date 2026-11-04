# GroupAuditLogEntryDataGroupCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**banner_id** | **str** |  | 
**banner_version** | **int** |  | [optional] 
**description** | **str** |  | 
**discoverability** | [**GroupAuditLogEntryDataGroupCreateDiscoverability**](GroupAuditLogEntryDataGroupCreateDiscoverability.md) |  | 
**galleries** | [**List[GroupAuditLogEntryDataGroupCreateGallery]**](GroupAuditLogEntryDataGroupCreateGallery.md) |  | [optional] 
**icon_id** | **str** |  | 
**icon_version** | **int** |  | [optional] 
**join_state** | [**GroupJoinState**](GroupJoinState.md) |  | [default to GroupJoinState.OPEN]
**name** | **str** |  | 
**owner_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**privacy** | [**GroupPrivacy**](GroupPrivacy.md) |  | [default to GroupPrivacy.DEFAULT]
**rules** | **str** |  | 
**short_code** | **str** |  | 

## Example

```python
from vrchatapi.models.group_audit_log_entry_data_group_create import GroupAuditLogEntryDataGroupCreate

# TODO update the JSON string below
json = "{}"
# create an instance of GroupAuditLogEntryDataGroupCreate from a JSON string
group_audit_log_entry_data_group_create_instance = GroupAuditLogEntryDataGroupCreate.from_json(json)
# print the JSON string representation of the object
print(GroupAuditLogEntryDataGroupCreate.to_json())

# convert the object into a dict
group_audit_log_entry_data_group_create_dict = group_audit_log_entry_data_group_create_instance.to_dict()
# create an instance of GroupAuditLogEntryDataGroupCreate from a dict
group_audit_log_entry_data_group_create_from_dict = GroupAuditLogEntryDataGroupCreate.from_dict(group_audit_log_entry_data_group_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


