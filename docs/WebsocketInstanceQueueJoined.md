# WebsocketInstanceQueueJoined


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** | Represents a unique location, consisting of a world identifier and an instance identifier, or \&quot;offline\&quot; if the user is not on your friends list. | 
**position** | **int** |  | 

## Example

```python
from vrchatapi.models.websocket_instance_queue_joined import WebsocketInstanceQueueJoined

# TODO update the JSON string below
json = "{}"
# create an instance of WebsocketInstanceQueueJoined from a JSON string
websocket_instance_queue_joined_instance = WebsocketInstanceQueueJoined.from_json(json)
# print the JSON string representation of the object
print(WebsocketInstanceQueueJoined.to_json())

# convert the object into a dict
websocket_instance_queue_joined_dict = websocket_instance_queue_joined_instance.to_dict()
# create an instance of WebsocketInstanceQueueJoined from a dict
websocket_instance_queue_joined_from_dict = WebsocketInstanceQueueJoined.from_dict(websocket_instance_queue_joined_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


