# NotificationV2DataGroupTransfer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_name** | **str** |  | 
**owner_user_display_name** | **str** |  | 

## Example

```python
from vrchatapi.models.notification_v2_data_group_transfer import NotificationV2DataGroupTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationV2DataGroupTransfer from a JSON string
notification_v2_data_group_transfer_instance = NotificationV2DataGroupTransfer.from_json(json)
# print the JSON string representation of the object
print(NotificationV2DataGroupTransfer.to_json())

# convert the object into a dict
notification_v2_data_group_transfer_dict = notification_v2_data_group_transfer_instance.to_dict()
# create an instance of NotificationV2DataGroupTransfer from a dict
notification_v2_data_group_transfer_from_dict = NotificationV2DataGroupTransfer.from_dict(notification_v2_data_group_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


