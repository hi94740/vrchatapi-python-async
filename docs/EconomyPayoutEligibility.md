# EconomyPayoutEligibility


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issue** | **str** |  | 
**ok_balance** | **bool** |  | 
**ok_frequency** | **bool** |  | 
**ok_not_ongoing** | **bool** |  | 
**ok_standing** | **bool** |  | 

## Example

```python
from vrchatapi.models.economy_payout_eligibility import EconomyPayoutEligibility

# TODO update the JSON string below
json = "{}"
# create an instance of EconomyPayoutEligibility from a JSON string
economy_payout_eligibility_instance = EconomyPayoutEligibility.from_json(json)
# print the JSON string representation of the object
print(EconomyPayoutEligibility.to_json())

# convert the object into a dict
economy_payout_eligibility_dict = economy_payout_eligibility_instance.to_dict()
# create an instance of EconomyPayoutEligibility from a dict
economy_payout_eligibility_from_dict = EconomyPayoutEligibility.from_dict(economy_payout_eligibility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


