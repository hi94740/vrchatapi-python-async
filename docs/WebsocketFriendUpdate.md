# WebsocketFriendUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**User**](User.md) |  | 
**user_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 

## Example

```python
from vrchatapi.models.websocket_friend_update import WebsocketFriendUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of WebsocketFriendUpdate from a JSON string
websocket_friend_update_instance = WebsocketFriendUpdate.from_json(json)
# print the JSON string representation of the object
print(WebsocketFriendUpdate.to_json())

# convert the object into a dict
websocket_friend_update_dict = websocket_friend_update_instance.to_dict()
# create an instance of WebsocketFriendUpdate from a dict
websocket_friend_update_from_dict = WebsocketFriendUpdate.from_dict(websocket_friend_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


