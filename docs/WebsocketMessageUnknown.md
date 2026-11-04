# WebsocketMessageUnknown

A websocket message whose `type` has no schema of its own.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **object** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from vrchatapi.models.websocket_message_unknown import WebsocketMessageUnknown

# TODO update the JSON string below
json = "{}"
# create an instance of WebsocketMessageUnknown from a JSON string
websocket_message_unknown_instance = WebsocketMessageUnknown.from_json(json)
# print the JSON string representation of the object
print(WebsocketMessageUnknown.to_json())

# convert the object into a dict
websocket_message_unknown_dict = websocket_message_unknown_instance.to_dict()
# create an instance of WebsocketMessageUnknown from a dict
websocket_message_unknown_from_dict = WebsocketMessageUnknown.from_dict(websocket_message_unknown_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


