# WebsocketNotificationV2Delete


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**version** | **int** |  | 

## Example

```python
from vrchatapi.models.websocket_notification_v2_delete import WebsocketNotificationV2Delete

# TODO update the JSON string below
json = "{}"
# create an instance of WebsocketNotificationV2Delete from a JSON string
websocket_notification_v2_delete_instance = WebsocketNotificationV2Delete.from_json(json)
# print the JSON string representation of the object
print(WebsocketNotificationV2Delete.to_json())

# convert the object into a dict
websocket_notification_v2_delete_dict = websocket_notification_v2_delete_instance.to_dict()
# create an instance of WebsocketNotificationV2Delete from a dict
websocket_notification_v2_delete_from_dict = WebsocketNotificationV2Delete.from_dict(websocket_notification_v2_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


