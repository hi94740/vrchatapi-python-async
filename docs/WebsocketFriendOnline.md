# WebsocketFriendOnline


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_request_invite** | **bool** |  | 
**location** | **str** | Represents a unique location, consisting of a world identifier and an instance identifier, or \&quot;offline\&quot; if the user is not on your friends list. | 
**platform** | **str** | This is normally &#x60;android&#x60;, &#x60;ios&#x60;, &#x60;standalonewindows&#x60;, &#x60;web&#x60;, or the empty value &#x60;&#x60;, but also supposedly can be any random Unity version such as &#x60;2019.2.4-801-Release&#x60; or &#x60;2019.2.2-772-Release&#x60; or even &#x60;unknownplatform&#x60;. | 
**user_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 

## Example

```python
from vrchatapi.models.websocket_friend_online import WebsocketFriendOnline

# TODO update the JSON string below
json = "{}"
# create an instance of WebsocketFriendOnline from a JSON string
websocket_friend_online_instance = WebsocketFriendOnline.from_json(json)
# print the JSON string representation of the object
print(WebsocketFriendOnline.to_json())

# convert the object into a dict
websocket_friend_online_dict = websocket_friend_online_instance.to_dict()
# create an instance of WebsocketFriendOnline from a dict
websocket_friend_online_from_dict = WebsocketFriendOnline.from_dict(websocket_friend_online_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


