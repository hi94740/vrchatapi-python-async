# NotificationInvite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**message** | **str** |  | 
**receiver_user_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 
**seen** | **bool** | Not included in notification objects received from the Websocket API | [optional] [default to False]
**sender_user_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**sender_username** | **str** | The name of the user who sent the notification. | [optional] 
**details** | **str** | A JSON-encoded string. | 
**type** | **str** |  | 

## Example

```python
from vrchatapi.models.notification_invite import NotificationInvite

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationInvite from a JSON string
notification_invite_instance = NotificationInvite.from_json(json)
# print the JSON string representation of the object
print(NotificationInvite.to_json())

# convert the object into a dict
notification_invite_dict = notification_invite_instance.to_dict()
# create an instance of NotificationInvite from a dict
notification_invite_from_dict = NotificationInvite.from_dict(notification_invite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


