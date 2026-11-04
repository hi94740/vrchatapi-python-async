# WebsocketGroupJoined


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** |  | 

## Example

```python
from vrchatapi.models.websocket_group_joined import WebsocketGroupJoined

# TODO update the JSON string below
json = "{}"
# create an instance of WebsocketGroupJoined from a JSON string
websocket_group_joined_instance = WebsocketGroupJoined.from_json(json)
# print the JSON string representation of the object
print(WebsocketGroupJoined.to_json())

# convert the object into a dict
websocket_group_joined_dict = websocket_group_joined_instance.to_dict()
# create an instance of WebsocketGroupJoined from a dict
websocket_group_joined_from_dict = WebsocketGroupJoined.from_dict(websocket_group_joined_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


