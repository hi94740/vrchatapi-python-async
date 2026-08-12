# NotificationDetailRequestInviteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**in_response_to** | **str** |  | 
**request_message** | **str** | Used when using InviteMessage Slot. | [optional] 

## Example

```python
from vrchatapi.models.notification_detail_request_invite_response import NotificationDetailRequestInviteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationDetailRequestInviteResponse from a JSON string
notification_detail_request_invite_response_instance = NotificationDetailRequestInviteResponse.from_json(json)
# print the JSON string representation of the object
print(NotificationDetailRequestInviteResponse.to_json())

# convert the object into a dict
notification_detail_request_invite_response_dict = notification_detail_request_invite_response_instance.to_dict()
# create an instance of NotificationDetailRequestInviteResponse from a dict
notification_detail_request_invite_response_from_dict = NotificationDetailRequestInviteResponse.from_dict(notification_detail_request_invite_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


