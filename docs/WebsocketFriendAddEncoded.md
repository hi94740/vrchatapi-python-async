# WebsocketFriendAddEncoded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from vrchatapi.models.websocket_friend_add_encoded import WebsocketFriendAddEncoded

# TODO update the JSON string below
json = "{}"
# create an instance of WebsocketFriendAddEncoded from a JSON string
websocket_friend_add_encoded_instance = WebsocketFriendAddEncoded.from_json(json)
# print the JSON string representation of the object
print(WebsocketFriendAddEncoded.to_json())

# convert the object into a dict
websocket_friend_add_encoded_dict = websocket_friend_add_encoded_instance.to_dict()
# create an instance of WebsocketFriendAddEncoded from a dict
websocket_friend_add_encoded_from_dict = WebsocketFriendAddEncoded.from_dict(websocket_friend_add_encoded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


