# NotificationDetailRequestInvite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform** | **str** | This is normally &#x60;android&#x60;, &#x60;ios&#x60;, &#x60;standalonewindows&#x60;, &#x60;web&#x60;, or the empty value &#x60;&#x60;, but also supposedly can be any random Unity version such as &#x60;2019.2.4-801-Release&#x60; or &#x60;2019.2.2-772-Release&#x60; or even &#x60;unknownplatform&#x60;. | [optional] 
**request_message** | **str** | Used when using InviteMessage Slot. | [optional] 

## Example

```python
from vrchatapi.models.notification_detail_request_invite import NotificationDetailRequestInvite

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationDetailRequestInvite from a JSON string
notification_detail_request_invite_instance = NotificationDetailRequestInvite.from_json(json)
# print the JSON string representation of the object
print(NotificationDetailRequestInvite.to_json())

# convert the object into a dict
notification_detail_request_invite_dict = notification_detail_request_invite_instance.to_dict()
# create an instance of NotificationDetailRequestInvite from a dict
notification_detail_request_invite_from_dict = NotificationDetailRequestInvite.from_dict(notification_detail_request_invite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


