# WebsocketFriendLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_request_invite** | **bool** |  | 
**location** | **str** | Represents a unique location, consisting of a world identifier and an instance identifier, or \&quot;offline\&quot; if the user is not on your friends list. | 
**traveling_to_location** | **str** | Represents a unique location, consisting of a world identifier and an instance identifier, or \&quot;offline\&quot; if the user is not on your friends list. | 
**user** | [**User**](User.md) |  | 
**user_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**world_id** | **str** | WorldID be \&quot;offline\&quot; on User profiles if you are not friends with that user. | 

## Example

```python
from vrchatapi.models.websocket_friend_location import WebsocketFriendLocation

# TODO update the JSON string below
json = "{}"
# create an instance of WebsocketFriendLocation from a JSON string
websocket_friend_location_instance = WebsocketFriendLocation.from_json(json)
# print the JSON string representation of the object
print(WebsocketFriendLocation.to_json())

# convert the object into a dict
websocket_friend_location_dict = websocket_friend_location_instance.to_dict()
# create an instance of WebsocketFriendLocation from a dict
websocket_friend_location_from_dict = WebsocketFriendLocation.from_dict(websocket_friend_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


