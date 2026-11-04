# WebsocketHideNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from vrchatapi.models.websocket_hide_notification import WebsocketHideNotification

# TODO update the JSON string below
json = "{}"
# create an instance of WebsocketHideNotification from a JSON string
websocket_hide_notification_instance = WebsocketHideNotification.from_json(json)
# print the JSON string representation of the object
print(WebsocketHideNotification.to_json())

# convert the object into a dict
websocket_hide_notification_dict = websocket_hide_notification_instance.to_dict()
# create an instance of WebsocketHideNotification from a dict
websocket_hide_notification_from_dict = WebsocketHideNotification.from_dict(websocket_hide_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


