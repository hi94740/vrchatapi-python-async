# WebsocketGroupRoleUpdated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | [**GroupRole**](GroupRole.md) |  | 

## Example

```python
from vrchatapi.models.websocket_group_role_updated import WebsocketGroupRoleUpdated

# TODO update the JSON string below
json = "{}"
# create an instance of WebsocketGroupRoleUpdated from a JSON string
websocket_group_role_updated_instance = WebsocketGroupRoleUpdated.from_json(json)
# print the JSON string representation of the object
print(WebsocketGroupRoleUpdated.to_json())

# convert the object into a dict
websocket_group_role_updated_dict = websocket_group_role_updated_instance.to_dict()
# create an instance of WebsocketGroupRoleUpdated from a dict
websocket_group_role_updated_from_dict = WebsocketGroupRoleUpdated.from_dict(websocket_group_role_updated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


