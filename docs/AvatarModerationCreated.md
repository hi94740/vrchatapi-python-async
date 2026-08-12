# AvatarModerationCreated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar_moderation_type** | [**AvatarModerationType**](AvatarModerationType.md) |  | 
**created** | **int** | Timestamp in milliseconds since Unix epoch | 
**target_avatar_id** | **str** |  | 

## Example

```python
from vrchatapi.models.avatar_moderation_created import AvatarModerationCreated

# TODO update the JSON string below
json = "{}"
# create an instance of AvatarModerationCreated from a JSON string
avatar_moderation_created_instance = AvatarModerationCreated.from_json(json)
# print the JSON string representation of the object
print(AvatarModerationCreated.to_json())

# convert the object into a dict
avatar_moderation_created_dict = avatar_moderation_created_instance.to_dict()
# create an instance of AvatarModerationCreated from a dict
avatar_moderation_created_from_dict = AvatarModerationCreated.from_dict(avatar_moderation_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


