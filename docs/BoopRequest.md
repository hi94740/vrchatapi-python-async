# BoopRequest

See NotificationDetailBoop; either inventoryItemId (accessed through .id) by itself, or emojiId (accessed through .metadata.fileId or built-in emoji name) with optional emojiVersion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emoji_id** | **str** | Either a FileID or a string constant for default emojis | [optional] 
**emoji_version** | **int** |  | [optional] 
**inventory_item_id** | **str** |  | [optional] 

## Example

```python
from vrchatapi.models.boop_request import BoopRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BoopRequest from a JSON string
boop_request_instance = BoopRequest.from_json(json)
# print the JSON string representation of the object
print(BoopRequest.to_json())

# convert the object into a dict
boop_request_dict = boop_request_instance.to_dict()
# create an instance of BoopRequest from a dict
boop_request_from_dict = BoopRequest.from_dict(boop_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


