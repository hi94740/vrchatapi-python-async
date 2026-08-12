# InviteMessage



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_be_updated** | **bool** |  | [default to True]
**id** | **str** |  | 
**message** | **str** |  | 
**message_type** | [**InviteMessageType**](InviteMessageType.md) |  | [default to InviteMessageType.MESSAGE]
**remaining_cooldown_minutes** | **int** | Changes to 60 when updated, although probably server-side configurable. | [default to 0]
**slot** | **int** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from vrchatapi.models.invite_message import InviteMessage

# TODO update the JSON string below
json = "{}"
# create an instance of InviteMessage from a JSON string
invite_message_instance = InviteMessage.from_json(json)
# print the JSON string representation of the object
print(InviteMessage.to_json())

# convert the object into a dict
invite_message_dict = invite_message_instance.to_dict()
# create an instance of InviteMessage from a dict
invite_message_from_dict = InviteMessage.from_dict(invite_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


