# UserNote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**note** | **str** |  | 
**target_user** | [**UserNoteTargetUser**](UserNoteTargetUser.md) |  | [optional] 
**target_user_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**user_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 

## Example

```python
from vrchatapi.models.user_note import UserNote

# TODO update the JSON string below
json = "{}"
# create an instance of UserNote from a JSON string
user_note_instance = UserNote.from_json(json)
# print the JSON string representation of the object
print(UserNote.to_json())

# convert the object into a dict
user_note_dict = user_note_instance.to_dict()
# create an instance of UserNote from a dict
user_note_from_dict = UserNote.from_dict(user_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


