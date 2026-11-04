# WebsocketFriendUpdateEncoded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from vrchatapi.models.websocket_friend_update_encoded import WebsocketFriendUpdateEncoded

# TODO update the JSON string below
json = "{}"
# create an instance of WebsocketFriendUpdateEncoded from a JSON string
websocket_friend_update_encoded_instance = WebsocketFriendUpdateEncoded.from_json(json)
# print the JSON string representation of the object
print(WebsocketFriendUpdateEncoded.to_json())

# convert the object into a dict
websocket_friend_update_encoded_dict = websocket_friend_update_encoded_instance.to_dict()
# create an instance of WebsocketFriendUpdateEncoded from a dict
websocket_friend_update_encoded_from_dict = WebsocketFriendUpdateEncoded.from_dict(websocket_friend_update_encoded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


