# GroupAuditLogEntryDataGroupInstanceClose


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_access_type** | [**GroupAccessType**](GroupAccessType.md) |  | [default to GroupAccessType.MEMBERS]
**role_ids** | **List[str]** | The role IDs that have access to the instance. | 

## Example

```python
from vrchatapi.models.group_audit_log_entry_data_group_instance_close import GroupAuditLogEntryDataGroupInstanceClose

# TODO update the JSON string below
json = "{}"
# create an instance of GroupAuditLogEntryDataGroupInstanceClose from a JSON string
group_audit_log_entry_data_group_instance_close_instance = GroupAuditLogEntryDataGroupInstanceClose.from_json(json)
# print the JSON string representation of the object
print(GroupAuditLogEntryDataGroupInstanceClose.to_json())

# convert the object into a dict
group_audit_log_entry_data_group_instance_close_dict = group_audit_log_entry_data_group_instance_close_instance.to_dict()
# create an instance of GroupAuditLogEntryDataGroupInstanceClose from a dict
group_audit_log_entry_data_group_instance_close_from_dict = GroupAuditLogEntryDataGroupInstanceClose.from_dict(group_audit_log_entry_data_group_instance_close_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


