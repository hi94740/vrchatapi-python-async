# GroupMyMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted_by_display_name** | **str** |  | [optional] 
**accepted_by_id** | **str** |  | [optional] 
**banned_at** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**group_id** | **str** |  | [optional] 
**has2_fa** | **bool** |  | [optional] [default to False]
**has_joined_from_purchase** | **bool** |  | [optional] [default to False]
**id** | **str** |  | [optional] 
**is_representing** | **bool** |  | [optional] [default to False]
**is_subscribed_to_announcements** | **bool** |  | [optional] [default to True]
**is_subscribed_to_event_announcements** | **bool** |  | [optional] 
**joined_at** | **datetime** |  | [optional] 
**last_post_read_at** | **datetime** |  | [optional] 
**m_role_ids** | **List[str]** |  | [optional] 
**manager_notes** | **str** |  | [optional] 
**membership_status** | **str** |  | [optional] 
**permissions** | [**List[GroupPermissions]**](GroupPermissions.md) |  | [optional] 
**role_ids** | **List[str]** |  | [optional] 
**user_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 
**visibility** | **str** |  | [optional] 

## Example

```python
from vrchatapi.models.group_my_member import GroupMyMember

# TODO update the JSON string below
json = "{}"
# create an instance of GroupMyMember from a JSON string
group_my_member_instance = GroupMyMember.from_json(json)
# print the JSON string representation of the object
print(GroupMyMember.to_json())

# convert the object into a dict
group_my_member_dict = group_my_member_instance.to_dict()
# create an instance of GroupMyMember from a dict
group_my_member_from_dict = GroupMyMember.from_dict(group_my_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


