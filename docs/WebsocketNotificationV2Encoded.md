# WebsocketNotificationV2Encoded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from vrchatapi.models.websocket_notification_v2_encoded import WebsocketNotificationV2Encoded

# TODO update the JSON string below
json = "{}"
# create an instance of WebsocketNotificationV2Encoded from a JSON string
websocket_notification_v2_encoded_instance = WebsocketNotificationV2Encoded.from_json(json)
# print the JSON string representation of the object
print(WebsocketNotificationV2Encoded.to_json())

# convert the object into a dict
websocket_notification_v2_encoded_dict = websocket_notification_v2_encoded_instance.to_dict()
# create an instance of WebsocketNotificationV2Encoded from a dict
websocket_notification_v2_encoded_from_dict = WebsocketNotificationV2Encoded.from_dict(websocket_notification_v2_encoded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


