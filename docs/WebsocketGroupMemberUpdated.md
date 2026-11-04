# WebsocketGroupMemberUpdated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member** | [**GroupMemberLimitedUser**](GroupMemberLimitedUser.md) |  | 

## Example

```python
from vrchatapi.models.websocket_group_member_updated import WebsocketGroupMemberUpdated

# TODO update the JSON string below
json = "{}"
# create an instance of WebsocketGroupMemberUpdated from a JSON string
websocket_group_member_updated_instance = WebsocketGroupMemberUpdated.from_json(json)
# print the JSON string representation of the object
print(WebsocketGroupMemberUpdated.to_json())

# convert the object into a dict
websocket_group_member_updated_dict = websocket_group_member_updated_instance.to_dict()
# create an instance of WebsocketGroupMemberUpdated from a dict
websocket_group_member_updated_from_dict = WebsocketGroupMemberUpdated.from_dict(websocket_group_member_updated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


