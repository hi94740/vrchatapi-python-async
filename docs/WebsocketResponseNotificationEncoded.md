# WebsocketResponseNotificationEncoded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from vrchatapi.models.websocket_response_notification_encoded import WebsocketResponseNotificationEncoded

# TODO update the JSON string below
json = "{}"
# create an instance of WebsocketResponseNotificationEncoded from a JSON string
websocket_response_notification_encoded_instance = WebsocketResponseNotificationEncoded.from_json(json)
# print the JSON string representation of the object
print(WebsocketResponseNotificationEncoded.to_json())

# convert the object into a dict
websocket_response_notification_encoded_dict = websocket_response_notification_encoded_instance.to_dict()
# create an instance of WebsocketResponseNotificationEncoded from a dict
websocket_response_notification_encoded_from_dict = WebsocketResponseNotificationEncoded.from_dict(websocket_response_notification_encoded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


