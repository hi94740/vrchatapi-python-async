# NotificationDetailInviteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**in_response_to** | **str** |  | 
**response_message** | **str** |  | 

## Example

```python
from vrchatapi.models.notification_detail_invite_response import NotificationDetailInviteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationDetailInviteResponse from a JSON string
notification_detail_invite_response_instance = NotificationDetailInviteResponse.from_json(json)
# print the JSON string representation of the object
print(NotificationDetailInviteResponse.to_json())

# convert the object into a dict
notification_detail_invite_response_dict = notification_detail_invite_response_instance.to_dict()
# create an instance of NotificationDetailInviteResponse from a dict
notification_detail_invite_response_from_dict = NotificationDetailInviteResponse.from_dict(notification_detail_invite_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


