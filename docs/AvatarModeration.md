# AvatarModeration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar_moderation_type** | [**AvatarModerationType**](AvatarModerationType.md) |  | 
**created** | **datetime** |  | 
**target_avatar_id** | **str** |  | 

## Example

```python
from vrchatapi.models.avatar_moderation import AvatarModeration

# TODO update the JSON string below
json = "{}"
# create an instance of AvatarModeration from a JSON string
avatar_moderation_instance = AvatarModeration.from_json(json)
# print the JSON string representation of the object
print(AvatarModeration.to_json())

# convert the object into a dict
avatar_moderation_dict = avatar_moderation_instance.to_dict()
# create an instance of AvatarModeration from a dict
avatar_moderation_from_dict = AvatarModeration.from_dict(avatar_moderation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


