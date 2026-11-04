# WebsocketUserLocationEncoded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from vrchatapi.models.websocket_user_location_encoded import WebsocketUserLocationEncoded

# TODO update the JSON string below
json = "{}"
# create an instance of WebsocketUserLocationEncoded from a JSON string
websocket_user_location_encoded_instance = WebsocketUserLocationEncoded.from_json(json)
# print the JSON string representation of the object
print(WebsocketUserLocationEncoded.to_json())

# convert the object into a dict
websocket_user_location_encoded_dict = websocket_user_location_encoded_instance.to_dict()
# create an instance of WebsocketUserLocationEncoded from a dict
websocket_user_location_encoded_from_dict = WebsocketUserLocationEncoded.from_dict(websocket_user_location_encoded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


