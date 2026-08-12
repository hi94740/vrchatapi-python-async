# MutualFriend

User object received when querying mutual friends

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar_thumbnail** | **str** | When profilePicOverride is not empty, use it instead. | [optional] 
**current_avatar_image_url** | **str** | When profilePicOverride is not empty, use it instead. | 
**current_avatar_tags** | **List[str]** |  | [optional] 
**current_avatar_thumbnail_image_url** | **str** | When profilePicOverride is not empty, use it instead. | [optional] 
**display_name** | **str** |  | 
**id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**image_url** | **str** |  | 
**profile_pic_override** | **str** |  | [optional] 
**status** | [**UserStatus**](UserStatus.md) |  | [default to UserStatus.OFFLINE]
**status_description** | **str** |  | 

## Example

```python
from vrchatapi.models.mutual_friend import MutualFriend

# TODO update the JSON string below
json = "{}"
# create an instance of MutualFriend from a JSON string
mutual_friend_instance = MutualFriend.from_json(json)
# print the JSON string representation of the object
print(MutualFriend.to_json())

# convert the object into a dict
mutual_friend_dict = mutual_friend_instance.to_dict()
# create an instance of MutualFriend from a dict
mutual_friend_from_dict = MutualFriend.from_dict(mutual_friend_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


