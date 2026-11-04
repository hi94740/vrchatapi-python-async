# WebsocketGroupMemberUpdatedEncoded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from vrchatapi.models.websocket_group_member_updated_encoded import WebsocketGroupMemberUpdatedEncoded

# TODO update the JSON string below
json = "{}"
# create an instance of WebsocketGroupMemberUpdatedEncoded from a JSON string
websocket_group_member_updated_encoded_instance = WebsocketGroupMemberUpdatedEncoded.from_json(json)
# print the JSON string representation of the object
print(WebsocketGroupMemberUpdatedEncoded.to_json())

# convert the object into a dict
websocket_group_member_updated_encoded_dict = websocket_group_member_updated_encoded_instance.to_dict()
# create an instance of WebsocketGroupMemberUpdatedEncoded from a dict
websocket_group_member_updated_encoded_from_dict = WebsocketGroupMemberUpdatedEncoded.from_dict(websocket_group_member_updated_encoded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


