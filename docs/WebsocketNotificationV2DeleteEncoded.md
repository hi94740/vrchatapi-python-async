# WebsocketNotificationV2DeleteEncoded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from vrchatapi.models.websocket_notification_v2_delete_encoded import WebsocketNotificationV2DeleteEncoded

# TODO update the JSON string below
json = "{}"
# create an instance of WebsocketNotificationV2DeleteEncoded from a JSON string
websocket_notification_v2_delete_encoded_instance = WebsocketNotificationV2DeleteEncoded.from_json(json)
# print the JSON string representation of the object
print(WebsocketNotificationV2DeleteEncoded.to_json())

# convert the object into a dict
websocket_notification_v2_delete_encoded_dict = websocket_notification_v2_delete_encoded_instance.to_dict()
# create an instance of WebsocketNotificationV2DeleteEncoded from a dict
websocket_notification_v2_delete_encoded_from_dict = WebsocketNotificationV2DeleteEncoded.from_dict(websocket_notification_v2_delete_encoded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


