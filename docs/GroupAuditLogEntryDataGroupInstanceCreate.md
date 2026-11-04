# GroupAuditLogEntryDataGroupInstanceCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calendar_entry_id** | **str** |  | 
**group_access_type** | [**GroupAccessType**](GroupAccessType.md) |  | [default to GroupAccessType.MEMBERS]
**role_ids** | **List[str]** |  | 

## Example

```python
from vrchatapi.models.group_audit_log_entry_data_group_instance_create import GroupAuditLogEntryDataGroupInstanceCreate

# TODO update the JSON string below
json = "{}"
# create an instance of GroupAuditLogEntryDataGroupInstanceCreate from a JSON string
group_audit_log_entry_data_group_instance_create_instance = GroupAuditLogEntryDataGroupInstanceCreate.from_json(json)
# print the JSON string representation of the object
print(GroupAuditLogEntryDataGroupInstanceCreate.to_json())

# convert the object into a dict
group_audit_log_entry_data_group_instance_create_dict = group_audit_log_entry_data_group_instance_create_instance.to_dict()
# create an instance of GroupAuditLogEntryDataGroupInstanceCreate from a dict
group_audit_log_entry_data_group_instance_create_from_dict = GroupAuditLogEntryDataGroupInstanceCreate.from_dict(group_audit_log_entry_data_group_instance_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


