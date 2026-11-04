# GroupAuditLogEntryDataGroupRoleCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The role description. | 
**is_added_on_join** | **bool** | Whether the role is automatically assigned on join. | 
**is_self_assignable** | **bool** | Whether users can self-assign this role. | 
**name** | **str** | The role name. | 
**order** | **int** | The display order of the role. | [optional] 
**permissions** | [**List[GroupPermissions]**](GroupPermissions.md) | The permissions assigned to this role. | 
**requires_purchase** | **bool** | Whether the role requires a purchase. | 
**requires_two_factor** | **bool** | Whether the role requires two-factor authentication. | 
**group_id** | **str** |  | 
**last_updated_by_user_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 

## Example

```python
from vrchatapi.models.group_audit_log_entry_data_group_role_create import GroupAuditLogEntryDataGroupRoleCreate

# TODO update the JSON string below
json = "{}"
# create an instance of GroupAuditLogEntryDataGroupRoleCreate from a JSON string
group_audit_log_entry_data_group_role_create_instance = GroupAuditLogEntryDataGroupRoleCreate.from_json(json)
# print the JSON string representation of the object
print(GroupAuditLogEntryDataGroupRoleCreate.to_json())

# convert the object into a dict
group_audit_log_entry_data_group_role_create_dict = group_audit_log_entry_data_group_role_create_instance.to_dict()
# create an instance of GroupAuditLogEntryDataGroupRoleCreate from a dict
group_audit_log_entry_data_group_role_create_from_dict = GroupAuditLogEntryDataGroupRoleCreate.from_dict(group_audit_log_entry_data_group_role_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


