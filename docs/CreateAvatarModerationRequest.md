# CreateAvatarModerationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar_moderation_type** | [**AvatarModerationType**](AvatarModerationType.md) |  | 
**target_avatar_id** | **str** |  | 

## Example

```python
from vrchatapi.models.create_avatar_moderation_request import CreateAvatarModerationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAvatarModerationRequest from a JSON string
create_avatar_moderation_request_instance = CreateAvatarModerationRequest.from_json(json)
# print the JSON string representation of the object
print(CreateAvatarModerationRequest.to_json())

# convert the object into a dict
create_avatar_moderation_request_dict = create_avatar_moderation_request_instance.to_dict()
# create an instance of CreateAvatarModerationRequest from a dict
create_avatar_moderation_request_from_dict = CreateAvatarModerationRequest.from_dict(create_avatar_moderation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


