# NotificationV2DataGroupAnnouncement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announcement_title** | **str** |  | 
**group_id** | **str** |  | 
**group_name** | **str** |  | 

## Example

```python
from vrchatapi.models.notification_v2_data_group_announcement import NotificationV2DataGroupAnnouncement

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationV2DataGroupAnnouncement from a JSON string
notification_v2_data_group_announcement_instance = NotificationV2DataGroupAnnouncement.from_json(json)
# print the JSON string representation of the object
print(NotificationV2DataGroupAnnouncement.to_json())

# convert the object into a dict
notification_v2_data_group_announcement_dict = notification_v2_data_group_announcement_instance.to_dict()
# create an instance of NotificationV2DataGroupAnnouncement from a dict
notification_v2_data_group_announcement_from_dict = NotificationV2DataGroupAnnouncement.from_dict(notification_v2_data_group_announcement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


