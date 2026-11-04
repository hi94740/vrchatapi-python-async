# GroupAuditLogEntryDataGroupInstanceModeration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** | Represents a unique location, consisting of a world identifier and an instance identifier, or \&quot;offline\&quot; if the user is not on your friends list. | 

## Example

```python
from vrchatapi.models.group_audit_log_entry_data_group_instance_moderation import GroupAuditLogEntryDataGroupInstanceModeration

# TODO update the JSON string below
json = "{}"
# create an instance of GroupAuditLogEntryDataGroupInstanceModeration from a JSON string
group_audit_log_entry_data_group_instance_moderation_instance = GroupAuditLogEntryDataGroupInstanceModeration.from_json(json)
# print the JSON string representation of the object
print(GroupAuditLogEntryDataGroupInstanceModeration.to_json())

# convert the object into a dict
group_audit_log_entry_data_group_instance_moderation_dict = group_audit_log_entry_data_group_instance_moderation_instance.to_dict()
# create an instance of GroupAuditLogEntryDataGroupInstanceModeration from a dict
group_audit_log_entry_data_group_instance_moderation_from_dict = GroupAuditLogEntryDataGroupInstanceModeration.from_dict(group_audit_log_entry_data_group_instance_moderation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


