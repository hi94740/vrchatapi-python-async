# WebsocketNotificationV2Update


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**updates** | **object** |  | 
**version** | **int** |  | 

## Example

```python
from vrchatapi.models.websocket_notification_v2_update import WebsocketNotificationV2Update

# TODO update the JSON string below
json = "{}"
# create an instance of WebsocketNotificationV2Update from a JSON string
websocket_notification_v2_update_instance = WebsocketNotificationV2Update.from_json(json)
# print the JSON string representation of the object
print(WebsocketNotificationV2Update.to_json())

# convert the object into a dict
websocket_notification_v2_update_dict = websocket_notification_v2_update_instance.to_dict()
# create an instance of WebsocketNotificationV2Update from a dict
websocket_notification_v2_update_from_dict = WebsocketNotificationV2Update.from_dict(websocket_notification_v2_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


