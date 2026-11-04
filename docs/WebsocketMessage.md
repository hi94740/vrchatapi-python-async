# WebsocketMessage

A message received over the websocket. The shape of `content` depends on `type`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**content** | **object** |  | [optional] 

## Example

```python
from vrchatapi.models.websocket_message import WebsocketMessage

# TODO update the JSON string below
json = "{}"
# create an instance of WebsocketMessage from a JSON string
websocket_message_instance = WebsocketMessage.from_json(json)
# print the JSON string representation of the object
print(WebsocketMessage.to_json())

# convert the object into a dict
websocket_message_dict = websocket_message_instance.to_dict()
# create an instance of WebsocketMessage from a dict
websocket_message_from_dict = WebsocketMessage.from_dict(websocket_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


