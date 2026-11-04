# NotificationV2DataEventAnnouncement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_id** | **str** |  | 
**owner_name** | **str** |  | 
**title** | **str** |  | 

## Example

```python
from vrchatapi.models.notification_v2_data_event_announcement import NotificationV2DataEventAnnouncement

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationV2DataEventAnnouncement from a JSON string
notification_v2_data_event_announcement_instance = NotificationV2DataEventAnnouncement.from_json(json)
# print the JSON string representation of the object
print(NotificationV2DataEventAnnouncement.to_json())

# convert the object into a dict
notification_v2_data_event_announcement_dict = notification_v2_data_event_announcement_instance.to_dict()
# create an instance of NotificationV2DataEventAnnouncement from a dict
notification_v2_data_event_announcement_from_dict = NotificationV2DataEventAnnouncement.from_dict(notification_v2_data_event_announcement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


