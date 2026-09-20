# MutualFriend

User object received when querying mutual friends

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**banner_color** | **str** | Hex colour without a leading &#x60;#&#x60;. | [optional] 
**banner_type** | **str** |  | [optional] 
**banner_url** | **str** |  | [optional] 
**display_name** | **str** |  | 
**icon_frame** | **str** |  | [optional] 
**icon_url** | **str** |  | [optional] 
**id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**nameplate_effect** | **str** |  | [optional] 
**profile_effect** | **str** |  | [optional] 
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


