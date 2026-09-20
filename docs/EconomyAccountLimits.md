# EconomyAccountLimits

Returned only when `getLimits` is set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buying_token_max_per_day** | **int** |  | 
**buying_token_remaining_allowed** | **int** |  | 

## Example

```python
from vrchatapi.models.economy_account_limits import EconomyAccountLimits

# TODO update the JSON string below
json = "{}"
# create an instance of EconomyAccountLimits from a JSON string
economy_account_limits_instance = EconomyAccountLimits.from_json(json)
# print the JSON string representation of the object
print(EconomyAccountLimits.to_json())

# convert the object into a dict
economy_account_limits_dict = economy_account_limits_instance.to_dict()
# create an instance of EconomyAccountLimits from a dict
economy_account_limits_from_dict = EconomyAccountLimits.from_dict(economy_account_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


