# UpdateInviteMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 

## Example

```python
from vrchatapi.models.update_invite_message_request import UpdateInviteMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInviteMessageRequest from a JSON string
update_invite_message_request_instance = UpdateInviteMessageRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateInviteMessageRequest.to_json())

# convert the object into a dict
update_invite_message_request_dict = update_invite_message_request_instance.to_dict()
# create an instance of UpdateInviteMessageRequest from a dict
update_invite_message_request_from_dict = UpdateInviteMessageRequest.from_dict(update_invite_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


