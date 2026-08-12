# UserSubscriptionEligible


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_cancelled_subscription** | **bool** |  | 
**gift_eligible** | **bool** |  | 
**non_extend_vendor_will_lose_gift_time** | **bool** |  | 
**purchase_eligible** | **bool** |  | 
**subscription_eligible** | **bool** |  | 
**subscription_on_alt_account** | **bool** |  | 

## Example

```python
from vrchatapi.models.user_subscription_eligible import UserSubscriptionEligible

# TODO update the JSON string below
json = "{}"
# create an instance of UserSubscriptionEligible from a JSON string
user_subscription_eligible_instance = UserSubscriptionEligible.from_json(json)
# print the JSON string representation of the object
print(UserSubscriptionEligible.to_json())

# convert the object into a dict
user_subscription_eligible_dict = user_subscription_eligible_instance.to_dict()
# create an instance of UserSubscriptionEligible from a dict
user_subscription_eligible_from_dict = UserSubscriptionEligible.from_dict(user_subscription_eligible_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


