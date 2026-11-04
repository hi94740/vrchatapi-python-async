# WebsocketNotificationEncoded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from vrchatapi.models.websocket_notification_encoded import WebsocketNotificationEncoded

# TODO update the JSON string below
json = "{}"
# create an instance of WebsocketNotificationEncoded from a JSON string
websocket_notification_encoded_instance = WebsocketNotificationEncoded.from_json(json)
# print the JSON string representation of the object
print(WebsocketNotificationEncoded.to_json())

# convert the object into a dict
websocket_notification_encoded_dict = websocket_notification_encoded_instance.to_dict()
# create an instance of WebsocketNotificationEncoded from a dict
websocket_notification_encoded_from_dict = WebsocketNotificationEncoded.from_dict(websocket_notification_encoded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


