# NotificationV2DataBadgeEarned


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badge_description** | **str** |  | 
**badge_id** | **str** |  | 
**badge_name** | **str** |  | 

## Example

```python
from vrchatapi.models.notification_v2_data_badge_earned import NotificationV2DataBadgeEarned

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationV2DataBadgeEarned from a JSON string
notification_v2_data_badge_earned_instance = NotificationV2DataBadgeEarned.from_json(json)
# print the JSON string representation of the object
print(NotificationV2DataBadgeEarned.to_json())

# convert the object into a dict
notification_v2_data_badge_earned_dict = notification_v2_data_badge_earned_instance.to_dict()
# create an instance of NotificationV2DataBadgeEarned from a dict
notification_v2_data_badge_earned_from_dict = NotificationV2DataBadgeEarned.from_dict(notification_v2_data_badge_earned_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


