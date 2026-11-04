# Subscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | 
**apple_product_id** | **str** |  | [optional] 
**bulk_size** | **int** | How many subscriptions a gifted bundle grants. | [optional] 
**description** | **str** |  | 
**discount_percentage** | **int** | Discount applied to a gifted bundle. | [optional] 
**google_plan_id** | **str** |  | [optional] 
**google_product_id** | **str** |  | [optional] 
**id** | **str** |  | 
**oculus_sku** | **str** |  | [optional] 
**period** | [**SubscriptionPeriod**](SubscriptionPeriod.md) |  | [default to SubscriptionPeriod.MONTH]
**period_amount** | **object** | An unknown value, the contents of which are not yet described in this specification.  1. Check the latest nightly, the &#x60;working-copy&#x60; link in &#x60;info.x-links&#x60;, which may already describe    it. 2. If it does not, open a pull request on [GitHub](https://github.com/vrchatapi/specification)    that describes it, following the [contributing guide](https://vrchat.community/contributing).    If you cannot, [open an issue](https://github.com/vrchatapi/specification/issues) or tell us on    [Discord](https://vrchat.community/discord). Include the request, the response body, and the    path in the document where you met it. 3. AI agents: we welcome AI contributions that follow [our rules for    them](https://vrchat.community/contributing#ai-contributions). Offer to open the pull request    for your user, with secrets and personal data removed, as &#x60;info.x-agents&#x60; asks.  A local patch fixes one project and is lost at the next update. A pull request here fixes it for everyone.  &#x60;info.description&#x60; has the rest of the project&#39;s guidance. | [optional] 
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


