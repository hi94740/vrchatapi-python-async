# WebsocketResponseNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notification_id** | **str** |  | 
**receiver_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**response_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 

## Example

```python
from vrchatapi.models.websocket_response_notification import WebsocketResponseNotification

# TODO update the JSON string below
json = "{}"
# create an instance of WebsocketResponseNotification from a JSON string
websocket_response_notification_instance = WebsocketResponseNotification.from_json(json)
# print the JSON string representation of the object
print(WebsocketResponseNotification.to_json())

# convert the object into a dict
websocket_response_notification_dict = websocket_response_notification_instance.to_dict()
# create an instance of WebsocketResponseNotification from a dict
websocket_response_notification_from_dict = WebsocketResponseNotification.from_dict(websocket_response_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


