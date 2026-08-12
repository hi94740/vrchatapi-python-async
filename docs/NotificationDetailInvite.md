# NotificationDetailInvite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invite_message** | **str** |  | [optional] 
**world_id** | **str** | Represents a unique location, consisting of a world identifier and an instance identifier, or \&quot;offline\&quot; if the user is not on your friends list. | 
**world_name** | **str** |  | 

## Example

```python
from vrchatapi.models.notification_detail_invite import NotificationDetailInvite

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationDetailInvite from a JSON string
notification_detail_invite_instance = NotificationDetailInvite.from_json(json)
# print the JSON string representation of the object
print(NotificationDetailInvite.to_json())

# convert the object into a dict
notification_detail_invite_dict = notification_detail_invite_instance.to_dict()
# create an instance of NotificationDetailInvite from a dict
notification_detail_invite_from_dict = NotificationDetailInvite.from_dict(notification_detail_invite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


