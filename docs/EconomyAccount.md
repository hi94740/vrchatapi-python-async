# EconomyAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_activated_on** | **datetime** |  | 
**account_id** | **str** |  | 
**account_seller_registered_on** | **datetime** |  | [optional] 
**account_seller_status** | **str** |  | [optional] 
**blocked** | **bool** |  | 
**can_earn** | **bool** |  | [optional] 
**can_payout** | **bool** |  | [optional] 
**can_spend** | **bool** |  | 
**skrill_email** | **str** |  | [optional] 
**source** | **str** |  | 
**tilia_id** | **str** |  | [optional] 
**tilia_type** | **str** |  | [optional] 
**user_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 

## Example

```python
from vrchatapi.models.economy_account import EconomyAccount

# TODO update the JSON string below
json = "{}"
# create an instance of EconomyAccount from a JSON string
economy_account_instance = EconomyAccount.from_json(json)
# print the JSON string representation of the object
print(EconomyAccount.to_json())

# convert the object into a dict
economy_account_dict = economy_account_instance.to_dict()
# create an instance of EconomyAccount from a dict
economy_account_from_dict = EconomyAccount.from_dict(economy_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


