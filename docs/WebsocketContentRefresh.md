# WebsocketContentRefresh


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | [**WebsocketContentRefreshActionType**](WebsocketContentRefreshActionType.md) |  | 
**content_type** | **str** |  | 
**file_id** | **str** |  | 
**item_id** | **str** |  | 
**item_type** | [**InventoryItemType**](InventoryItemType.md) |  | [default to InventoryItemType.BUNDLE]

## Example

```python
from vrchatapi.models.websocket_content_refresh import WebsocketContentRefresh

# TODO update the JSON string below
json = "{}"
# create an instance of WebsocketContentRefresh from a JSON string
websocket_content_refresh_instance = WebsocketContentRefresh.from_json(json)
# print the JSON string representation of the object
print(WebsocketContentRefresh.to_json())

# convert the object into a dict
websocket_content_refresh_dict = websocket_content_refresh_instance.to_dict()
# create an instance of WebsocketContentRefresh from a dict
websocket_content_refresh_from_dict = WebsocketContentRefresh.from_dict(websocket_content_refresh_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


