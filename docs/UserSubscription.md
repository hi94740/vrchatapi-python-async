# UserSubscription



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [default to True]
**amount** | **float** |  | 
**created_at** | **datetime** |  | 
**description** | **str** |  | 
**expires** | **datetime** |  | 
**id** | **str** |  | 
**is_bulk_gift** | **bool** |  | [default to False]
**is_gift** | **bool** |  | [default to False]
**license_groups** | **List[str]** |  | 
**period** | [**SubscriptionPeriod**](SubscriptionPeriod.md) |  | [default to SubscriptionPeriod.MONTH]
**starts** | **str** |  | [optional] 
**status** | [**TransactionStatus**](TransactionStatus.md) |  | [default to TransactionStatus.ACTIVE]
**steam_item_id** | **str** |  | [optional] 
**store** | **str** | Which \&quot;Store\&quot; it came from. Right now only Stores are \&quot;Steam\&quot; and \&quot;Admin\&quot;. | 
**tier** | **int** |  | 
**transaction_id** | **str** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from vrchatapi.models.user_subscription import UserSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of UserSubscription from a JSON string
user_subscription_instance = UserSubscription.from_json(json)
# print the JSON string representation of the object
print(UserSubscription.to_json())

# convert the object into a dict
user_subscription_dict = user_subscription_instance.to_dict()
# create an instance of UserSubscription from a dict
user_subscription_from_dict = UserSubscription.from_dict(user_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


