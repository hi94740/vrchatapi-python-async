# WebsocketClearNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 

## Example

```python
from vrchatapi.models.websocket_clear_notification import WebsocketClearNotification

# TODO update the JSON string below
json = "{}"
# create an instance of WebsocketClearNotification from a JSON string
websocket_clear_notification_instance = WebsocketClearNotification.from_json(json)
# print the JSON string representation of the object
print(WebsocketClearNotification.to_json())

# convert the object into a dict
websocket_clear_notification_dict = websocket_clear_notification_instance.to_dict()
# create an instance of WebsocketClearNotification from a dict
websocket_clear_notification_from_dict = WebsocketClearNotification.from_dict(websocket_clear_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


