# Subscription



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | 
**apple_product_id** | **str** |  | [optional] 
**description** | **str** |  | 
**google_plan_id** | **str** |  | [optional] 
**google_product_id** | **str** |  | [optional] 
**id** | **str** |  | 
**oculus_sku** | **str** |  | [optional] 
**period** | [**SubscriptionPeriod**](SubscriptionPeriod.md) |  | [default to SubscriptionPeriod.MONTH]
**pico_sku** | **str** |  | [optional] 
**steam_item_id** | **str** |  | 
**tier** | **int** |  | 

## Example

```python
from vrchatapi.models.subscription import Subscription

# TODO update the JSON string below
json = "{}"
# create an instance of Subscription from a JSON string
subscription_instance = Subscription.from_json(json)
# print the JSON string representation of the object
print(Subscription.to_json())

# convert the object into a dict
subscription_dict = subscription_instance.to_dict()
# create an instance of Subscription from a dict
subscription_from_dict = Subscription.from_dict(subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


