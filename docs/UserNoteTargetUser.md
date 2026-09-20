# UserNoteTargetUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 
**display_name** | **str** |  | [optional] 

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


