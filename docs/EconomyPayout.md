# EconomyPayout


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_amount_tokens** | **int** |  | 
**payment_amount_usd** | **int** |  | 
**payment_created** | **datetime** |  | 
**payment_out_id** | **int** |  | 
**payment_platform** | **str** |  | 
**payment_platform_code** | **int** |  | 
**payment_status** | **str** |  | 
**payment_status_code** | **int** |  | 
**payment_updated** | **datetime** |  | 
**platform_payment_guid** | **str** |  | [optional] 
**platform_payment_method** | **str** |  | [optional] 
**reversal_date** | **datetime** |  | [optional] 
**reversal_reason** | **str** |  | [optional] 
**reversal_reason_code** | **int** |  | [optional] 
**reversal_transaction_id** | **int** |  | [optional] 
**transaction_id** | **int** |  | 

## Example

```python
from vrchatapi.models.economy_payout import EconomyPayout

# TODO update the JSON string below
json = "{}"
# create an instance of EconomyPayout from a JSON string
economy_payout_instance = EconomyPayout.from_json(json)
# print the JSON string representation of the object
print(EconomyPayout.to_json())

# convert the object into a dict
economy_payout_dict = economy_payout_instance.to_dict()
# create an instance of EconomyPayout from a dict
economy_payout_from_dict = EconomyPayout.from_dict(economy_payout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


