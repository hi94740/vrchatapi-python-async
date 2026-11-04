# InfoPushDataPromotionNotification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | 
**command** | **str** |  | 
**image_url** | **str** |  | 
**parameter** | **str** |  | 
**title** | **str** |  | 

## Example

```python
from vrchatapi.models.info_push_data_promotion_notification import InfoPushDataPromotionNotification

# TODO update the JSON string below
json = "{}"
# create an instance of InfoPushDataPromotionNotification from a JSON string
info_push_data_promotion_notification_instance = InfoPushDataPromotionNotification.from_json(json)
# print the JSON string representation of the object
print(InfoPushDataPromotionNotification.to_json())

# convert the object into a dict
info_push_data_promotion_notification_dict = info_push_data_promotion_notification_instance.to_dict()
# create an instance of InfoPushDataPromotionNotification from a dict
info_push_data_promotion_notification_from_dict = InfoPushDataPromotionNotification.from_dict(info_push_data_promotion_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


