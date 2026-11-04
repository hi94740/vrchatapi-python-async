# WebsocketFriendDelete


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 

## Example

```python
from vrchatapi.models.websocket_friend_delete import WebsocketFriendDelete

# TODO update the JSON string below
json = "{}"
# create an instance of WebsocketFriendDelete from a JSON string
websocket_friend_delete_instance = WebsocketFriendDelete.from_json(json)
# print the JSON string representation of the object
print(WebsocketFriendDelete.to_json())

# convert the object into a dict
websocket_friend_delete_dict = websocket_friend_delete_instance.to_dict()
# create an instance of WebsocketFriendDelete from a dict
websocket_friend_delete_from_dict = WebsocketFriendDelete.from_dict(websocket_friend_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


