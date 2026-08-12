# NotificationV2DetailsBoop

Either inventoryItemId by itself, or emojiId with optional emojiVersion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emoji_id** | **str** | Either a FileID or a string constant for default emojis | 
**emoji_version** | **int** |  | 
**inventory_item_id** | **str** |  | 

## Example

```python
from vrchatapi.models.notification_v2_details_boop import NotificationV2DetailsBoop

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationV2DetailsBoop from a JSON string
notification_v2_details_boop_instance = NotificationV2DetailsBoop.from_json(json)
# print the JSON string representation of the object
print(NotificationV2DetailsBoop.to_json())

# convert the object into a dict
notification_v2_details_boop_dict = notification_v2_details_boop_instance.to_dict()
# create an instance of NotificationV2DetailsBoop from a dict
notification_v2_details_boop_from_dict = NotificationV2DetailsBoop.from_dict(notification_v2_details_boop_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


