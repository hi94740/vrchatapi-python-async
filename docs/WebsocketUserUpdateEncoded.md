# WebsocketUserUpdateEncoded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from vrchatapi.models.websocket_user_update_encoded import WebsocketUserUpdateEncoded

# TODO update the JSON string below
json = "{}"
# create an instance of WebsocketUserUpdateEncoded from a JSON string
websocket_user_update_encoded_instance = WebsocketUserUpdateEncoded.from_json(json)
# print the JSON string representation of the object
print(WebsocketUserUpdateEncoded.to_json())

# convert the object into a dict
websocket_user_update_encoded_dict = websocket_user_update_encoded_instance.to_dict()
# create an instance of WebsocketUserUpdateEncoded from a dict
websocket_user_update_encoded_from_dict = WebsocketUserUpdateEncoded.from_dict(websocket_user_update_encoded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


