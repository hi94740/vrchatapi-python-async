# ModerateUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**moderated** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**type** | [**PlayerModerationType**](PlayerModerationType.md) |  | [default to PlayerModerationType.UNMUTE]

## Example

```python
from vrchatapi.models.moderate_user_request import ModerateUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ModerateUserRequest from a JSON string
moderate_user_request_instance = ModerateUserRequest.from_json(json)
# print the JSON string representation of the object
print(ModerateUserRequest.to_json())

# convert the object into a dict
moderate_user_request_dict = moderate_user_request_instance.to_dict()
# create an instance of ModerateUserRequest from a dict
moderate_user_request_from_dict = ModerateUserRequest.from_dict(moderate_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


