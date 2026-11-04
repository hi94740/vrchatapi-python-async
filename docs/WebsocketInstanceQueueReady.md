# WebsocketInstanceQueueReady


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry** | **datetime** |  | 
**location** | **str** | Represents a unique location, consisting of a world identifier and an instance identifier, or \&quot;offline\&quot; if the user is not on your friends list. | 

## Example

```python
from vrchatapi.models.websocket_instance_queue_ready import WebsocketInstanceQueueReady

# TODO update the JSON string below
json = "{}"
# create an instance of WebsocketInstanceQueueReady from a JSON string
websocket_instance_queue_ready_instance = WebsocketInstanceQueueReady.from_json(json)
# print the JSON string representation of the object
print(WebsocketInstanceQueueReady.to_json())

# convert the object into a dict
websocket_instance_queue_ready_dict = websocket_instance_queue_ready_instance.to_dict()
# create an instance of WebsocketInstanceQueueReady from a dict
websocket_instance_queue_ready_from_dict = WebsocketInstanceQueueReady.from_dict(websocket_instance_queue_ready_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


