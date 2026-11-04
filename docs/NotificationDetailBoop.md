# NotificationDetailBoop

Either inventoryItemId by itself, or emojiId with optional emojiVersion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emoji_id** | **str** |  | [optional] 
**emoji_version** | **int** |  | [optional] 
**inventory_item_id** | **str** |  | [optional] 

## Example

```python
from vrchatapi.models.notification_detail_boop import NotificationDetailBoop

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationDetailBoop from a JSON string
notification_detail_boop_instance = NotificationDetailBoop.from_json(json)
# print the JSON string representation of the object
print(NotificationDetailBoop.to_json())

# convert the object into a dict
notification_detail_boop_dict = notification_detail_boop_instance.to_dict()
# create an instance of NotificationDetailBoop from a dict
notification_detail_boop_from_dict = NotificationDetailBoop.from_dict(notification_detail_boop_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


