# WebsocketNotificationV2UpdateEncoded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from vrchatapi.models.websocket_notification_v2_update_encoded import WebsocketNotificationV2UpdateEncoded

# TODO update the JSON string below
json = "{}"
# create an instance of WebsocketNotificationV2UpdateEncoded from a JSON string
websocket_notification_v2_update_encoded_instance = WebsocketNotificationV2UpdateEncoded.from_json(json)
# print the JSON string representation of the object
print(WebsocketNotificationV2UpdateEncoded.to_json())

# convert the object into a dict
websocket_notification_v2_update_encoded_dict = websocket_notification_v2_update_encoded_instance.to_dict()
# create an instance of WebsocketNotificationV2UpdateEncoded from a dict
websocket_notification_v2_update_encoded_from_dict = WebsocketNotificationV2UpdateEncoded.from_dict(websocket_notification_v2_update_encoded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


