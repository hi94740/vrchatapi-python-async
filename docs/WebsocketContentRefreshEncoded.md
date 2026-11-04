# WebsocketContentRefreshEncoded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from vrchatapi.models.websocket_content_refresh_encoded import WebsocketContentRefreshEncoded

# TODO update the JSON string below
json = "{}"
# create an instance of WebsocketContentRefreshEncoded from a JSON string
websocket_content_refresh_encoded_instance = WebsocketContentRefreshEncoded.from_json(json)
# print the JSON string representation of the object
print(WebsocketContentRefreshEncoded.to_json())

# convert the object into a dict
websocket_content_refresh_encoded_dict = websocket_content_refresh_encoded_instance.to_dict()
# create an instance of WebsocketContentRefreshEncoded from a dict
websocket_content_refresh_encoded_from_dict = WebsocketContentRefreshEncoded.from_dict(websocket_content_refresh_encoded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


