# NotificationV2DataGroupInformative


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** |  | 
**group_name** | **str** |  | 
**transfer_target_display_name** | **str** |  | [optional] 

## Example

```python
from vrchatapi.models.notification_v2_data_group_informative import NotificationV2DataGroupInformative

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationV2DataGroupInformative from a JSON string
notification_v2_data_group_informative_instance = NotificationV2DataGroupInformative.from_json(json)
# print the JSON string representation of the object
print(NotificationV2DataGroupInformative.to_json())

# convert the object into a dict
notification_v2_data_group_informative_dict = notification_v2_data_group_informative_instance.to_dict()
# create an instance of NotificationV2DataGroupInformative from a dict
notification_v2_data_group_informative_from_dict = NotificationV2DataGroupInformative.from_dict(notification_v2_data_group_informative_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


