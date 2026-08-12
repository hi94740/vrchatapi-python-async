# PlayerModeration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | 
**id** | **str** |  | 
**source_display_name** | **str** |  | 
**source_user_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**target_display_name** | **str** |  | 
**target_user_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**type** | [**PlayerModerationType**](PlayerModerationType.md) |  | [default to PlayerModerationType.UNMUTE]

## Example

```python
from vrchatapi.models.player_moderation import PlayerModeration

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerModeration from a JSON string
player_moderation_instance = PlayerModeration.from_json(json)
# print the JSON string representation of the object
print(PlayerModeration.to_json())

# convert the object into a dict
player_moderation_dict = player_moderation_instance.to_dict()
# create an instance of PlayerModeration from a dict
player_moderation_from_dict = PlayerModeration.from_dict(player_moderation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


