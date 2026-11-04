# NotificationV2Data


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badge_description** | **str** |  | [optional] 
**badge_id** | **str** |  | [optional] 
**badge_name** | **str** |  | [optional] 
**booping_user_display_name** | **str** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**owner_name** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**announcement_title** | **str** |  | [optional] 
**group_id** | **str** |  | [optional] 
**group_name** | **str** |  | [optional] 
**transfer_target_display_name** | **str** |  | [optional] 
**owner_user_display_name** | **str** |  | [optional] 

## Example

```python
from vrchatapi.models.notification_v2_data import NotificationV2Data

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationV2Data from a JSON string
notification_v2_data_instance = NotificationV2Data.from_json(json)
# print the JSON string representation of the object
print(NotificationV2Data.to_json())

# convert the object into a dict
notification_v2_data_dict = notification_v2_data_instance.to_dict()
# create an instance of NotificationV2Data from a dict
notification_v2_data_from_dict = NotificationV2Data.from_dict(notification_v2_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


