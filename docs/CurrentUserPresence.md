# CurrentUserPresence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar_thumbnail** | **str** |  | [optional] 
**current_avatar_tags** | **List[str]** |  | [optional] 
**debugflag** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**groups** | **List[str]** |  | [optional] 
**id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 
**instance** | **str** |  | [optional] 
**instance_type** | **str** | either an InstanceType or an empty string | [optional] 
**is_rejoining** | **str** |  | [optional] 
**platform** | **str** | This is normally &#x60;android&#x60;, &#x60;ios&#x60;, &#x60;standalonewindows&#x60;, &#x60;web&#x60;, or the empty value &#x60;&#x60;, but also supposedly can be any random Unity version such as &#x60;2019.2.4-801-Release&#x60; or &#x60;2019.2.2-772-Release&#x60; or even &#x60;unknownplatform&#x60;. | [optional] 
**profile_pic_override** | **str** |  | [optional] 
**status** | **str** | either a UserStatus or empty string | [optional] 
**traveling_to_instance** | **str** |  | [optional] 
**traveling_to_world** | **str** | Represents a unique location, consisting of a world identifier and an instance identifier, or \&quot;offline\&quot; if the user is not on your friends list. | [optional] 
**user_icon** | **str** |  | [optional] 
**world** | **str** | WorldID be \&quot;offline\&quot; on User profiles if you are not friends with that user. | [optional] 

## Example

```python
from vrchatapi.models.current_user_presence import CurrentUserPresence

# TODO update the JSON string below
json = "{}"
# create an instance of CurrentUserPresence from a JSON string
current_user_presence_instance = CurrentUserPresence.from_json(json)
# print the JSON string representation of the object
print(CurrentUserPresence.to_json())

# convert the object into a dict
current_user_presence_dict = current_user_presence_instance.to_dict()
# create an instance of CurrentUserPresence from a dict
current_user_presence_from_dict = CurrentUserPresence.from_dict(current_user_presence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


