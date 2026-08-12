# GroupMemberLimitedUser

Only visible via the /groups/:groupId/members endpoint, **not** when fetching a specific user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_avatar_tags** | **List[str]** |  | [optional] 
**current_avatar_thumbnail_image_url** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**icon_url** | **str** |  | [optional] 
**id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 
**profile_pic_override** | **str** |  | [optional] 
**thumbnail_url** | **str** |  | [optional] 

## Example

```python
from vrchatapi.models.group_member_limited_user import GroupMemberLimitedUser

# TODO update the JSON string below
json = "{}"
# create an instance of GroupMemberLimitedUser from a JSON string
group_member_limited_user_instance = GroupMemberLimitedUser.from_json(json)
# print the JSON string representation of the object
print(GroupMemberLimitedUser.to_json())

# convert the object into a dict
group_member_limited_user_dict = group_member_limited_user_instance.to_dict()
# create an instance of GroupMemberLimitedUser from a dict
group_member_limited_user_from_dict = GroupMemberLimitedUser.from_dict(group_member_limited_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


