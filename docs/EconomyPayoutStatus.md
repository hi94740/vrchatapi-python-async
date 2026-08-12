# EconomyPayoutStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | 
**active_payout** | [**EconomyPayout**](EconomyPayout.md) |  | [optional] 
**active_payout_cancellable** | **bool** |  | 
**active_payout_tilia_amount** | **int** |  | 
**earnings_balance** | **int** |  | 
**eligibility** | [**EconomyPayoutEligibility**](EconomyPayoutEligibility.md) |  | 
**payout_eligible** | **bool** |  | 
**tilia_id** | **str** |  | 

## Example

```python
from vrchatapi.models.economy_payout_status import EconomyPayoutStatus

# TODO update the JSON string below
json = "{}"
# create an instance of EconomyPayoutStatus from a JSON string
economy_payout_status_instance = EconomyPayoutStatus.from_json(json)
# print the JSON string representation of the object
print(EconomyPayoutStatus.to_json())

# convert the object into a dict
economy_payout_status_dict = economy_payout_status_instance.to_dict()
# create an instance of EconomyPayoutStatus from a dict
economy_payout_status_from_dict = EconomyPayoutStatus.from_dict(economy_payout_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


