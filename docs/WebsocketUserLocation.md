# WebsocketUserLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance** | **str** | InstanceID can be \&quot;offline\&quot; on User profiles if you are not friends with that user and \&quot;private\&quot; if you are friends and user is in private instance. | 
**location** | **str** | Represents a unique location, consisting of a world identifier and an instance identifier, or \&quot;offline\&quot; if the user is not on your friends list. | 
**traveling_to_location** | **str** | Represents a unique location, consisting of a world identifier and an instance identifier, or \&quot;offline\&quot; if the user is not on your friends list. | 
**user** | [**User**](User.md) |  | 
**user_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 

## Example

```python
from vrchatapi.models.websocket_user_location import WebsocketUserLocation

# TODO update the JSON string below
json = "{}"
# create an instance of WebsocketUserLocation from a JSON string
websocket_user_location_instance = WebsocketUserLocation.from_json(json)
# print the JSON string representation of the object
print(WebsocketUserLocation.to_json())

# convert the object into a dict
websocket_user_location_dict = websocket_user_location_instance.to_dict()
# create an instance of WebsocketUserLocation from a dict
websocket_user_location_from_dict = WebsocketUserLocation.from_dict(websocket_user_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


