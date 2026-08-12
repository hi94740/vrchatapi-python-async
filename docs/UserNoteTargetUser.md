# UserNoteTargetUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**current_avatar_tags** | **List[str]** |  | [optional] 
**current_avatar_thumbnail_image_url** | **str** | When profilePicOverride is not empty, use it instead. | [optional] 
**display_name** | **str** |  | [optional] 
**profile_pic_override** | **str** |  | [optional] 
**user_icon** | **str** |  | [optional] 

## Example

```python
from vrchatapi.models.user_note_target_user import UserNoteTargetUser

# TODO update the JSON string below
json = "{}"
# create an instance of UserNoteTargetUser from a JSON string
user_note_target_user_instance = UserNoteTargetUser.from_json(json)
# print the JSON string representation of the object
print(UserNoteTargetUser.to_json())

# convert the object into a dict
user_note_target_user_dict = user_note_target_user_instance.to_dict()
# create an instance of UserNoteTargetUser from a dict
user_note_target_user_from_dict = UserNoteTargetUser.from_dict(user_note_target_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


