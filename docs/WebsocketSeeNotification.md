# WebsocketSeeNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from vrchatapi.models.websocket_see_notification import WebsocketSeeNotification

# TODO update the JSON string below
json = "{}"
# create an instance of WebsocketSeeNotification from a JSON string
websocket_see_notification_instance = WebsocketSeeNotification.from_json(json)
# print the JSON string representation of the object
print(WebsocketSeeNotification.to_json())

# convert the object into a dict
websocket_see_notification_dict = websocket_see_notification_instance.to_dict()
# create an instance of WebsocketSeeNotification from a dict
websocket_see_notification_from_dict = WebsocketSeeNotification.from_dict(websocket_see_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


