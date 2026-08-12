# LimitedUserFriend

User object received when querying your friends list

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bio** | **str** |  | [optional] 
**bio_links** | **List[str]** |   | [optional] 
**current_avatar_image_url** | **str** | When profilePicOverride is not empty, use it instead. | [optional] 
**current_avatar_tags** | **List[str]** |  | [optional] 
**current_avatar_thumbnail_image_url** | **str** | When profilePicOverride is not empty, use it instead. | [optional] 
**developer_type** | [**DeveloperType**](DeveloperType.md) |  | [default to DeveloperType.NONE]
**display_name** | **str** |  | 
**friend_key** | **str** |  | 
**id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**image_url** | **str** |  | 
**is_friend** | **bool** |  | 
**last_activity** | **datetime** |  | 
**last_login** | **datetime** |  | 
**last_mobile** | **datetime** |  | 
**last_platform** | **str** | This is normally &#x60;android&#x60;, &#x60;ios&#x60;, &#x60;standalonewindows&#x60;, &#x60;web&#x60;, or the empty value &#x60;&#x60;, but also supposedly can be any random Unity version such as &#x60;2019.2.4-801-Release&#x60; or &#x60;2019.2.2-772-Release&#x60; or even &#x60;unknownplatform&#x60;. | 
**location** | **str** |  | 
**platform** | **str** |  | 
**profile_pic_override** | **str** |  | [optional] 
**profile_pic_override_thumbnail** | **str** |  | [optional] 
**status** | [**UserStatus**](UserStatus.md) |  | [default to UserStatus.OFFLINE]
**status_description** | **str** |  | 
**tags** | **List[str]** | &lt;- Always empty. | 
**user_icon** | **str** |  | [optional] 

## Example

```python
from vrchatapi.models.limited_user_friend import LimitedUserFriend

# TODO update the JSON string below
json = "{}"
# create an instance of LimitedUserFriend from a JSON string
limited_user_friend_instance = LimitedUserFriend.from_json(json)
# print the JSON string representation of the object
print(LimitedUserFriend.to_json())

# convert the object into a dict
limited_user_friend_dict = limited_user_friend_instance.to_dict()
# create an instance of LimitedUserFriend from a dict
limited_user_friend_from_dict = LimitedUserFriend.from_dict(limited_user_friend_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


