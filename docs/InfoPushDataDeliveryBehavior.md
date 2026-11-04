# InfoPushDataDeliveryBehavior


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bypass24_hour_window** | **bool** |  | [optional] 
**max_redelivery_attempts** | **int** |  | [optional] 
**redeliver_if_no_engagement** | **bool** |  | [optional] 

## Example

```python
from vrchatapi.models.info_push_data_delivery_behavior import InfoPushDataDeliveryBehavior

# TODO update the JSON string below
json = "{}"
# create an instance of InfoPushDataDeliveryBehavior from a JSON string
info_push_data_delivery_behavior_instance = InfoPushDataDeliveryBehavior.from_json(json)
# print the JSON string representation of the object
print(InfoPushDataDeliveryBehavior.to_json())

# convert the object into a dict
info_push_data_delivery_behavior_dict = info_push_data_delivery_behavior_instance.to_dict()
# create an instance of InfoPushDataDeliveryBehavior from a dict
info_push_data_delivery_behavior_from_dict = InfoPushDataDeliveryBehavior.from_dict(info_push_data_delivery_behavior_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


