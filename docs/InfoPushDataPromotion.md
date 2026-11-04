# InfoPushDataPromotion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**impressions** | **int** |  | 
**notification** | [**InfoPushDataPromotionNotification**](InfoPushDataPromotionNotification.md) |  | 
**type** | **str** |  | 

## Example

```python
from vrchatapi.models.info_push_data_promotion import InfoPushDataPromotion

# TODO update the JSON string below
json = "{}"
# create an instance of InfoPushDataPromotion from a JSON string
info_push_data_promotion_instance = InfoPushDataPromotion.from_json(json)
# print the JSON string representation of the object
print(InfoPushDataPromotion.to_json())

# convert the object into a dict
info_push_data_promotion_dict = info_push_data_promotion_instance.to_dict()
# create an instance of InfoPushDataPromotion from a dict
info_push_data_promotion_from_dict = InfoPushDataPromotion.from_dict(info_push_data_promotion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


