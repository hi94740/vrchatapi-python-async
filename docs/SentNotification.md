# SentNotification



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**details** | **Dict[str, str]** |  | 
**id** | **str** |  | 
**message** | **str** |  | 
**receiver_user_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**sender_user_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**sender_username** | **str** | -| **DEPRECATED:** VRChat API no longer return usernames of other users. [See issue by Tupper for more information](https://github.com/pypy-vrc/VRCX/issues/429). | [optional] 
**type** | [**NotificationType**](NotificationType.md) |  | [default to NotificationType.FRIENDREQUEST]

## Example

```python
from vrchatapi.models.sent_notification import SentNotification

# TODO update the JSON string below
json = "{}"
# create an instance of SentNotification from a JSON string
sent_notification_instance = SentNotification.from_json(json)
# print the JSON string representation of the object
print(SentNotification.to_json())

# convert the object into a dict
sent_notification_dict = sent_notification_instance.to_dict()
# create an instance of SentNotification from a dict
sent_notification_from_dict = SentNotification.from_dict(sent_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


