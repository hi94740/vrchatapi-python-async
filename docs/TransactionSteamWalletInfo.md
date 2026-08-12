# TransactionSteamWalletInfo



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** |  | [default to 'US']
**currency** | **str** |  | [default to 'USD']
**state** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from vrchatapi.models.transaction_steam_wallet_info import TransactionSteamWalletInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionSteamWalletInfo from a JSON string
transaction_steam_wallet_info_instance = TransactionSteamWalletInfo.from_json(json)
# print the JSON string representation of the object
print(TransactionSteamWalletInfo.to_json())

# convert the object into a dict
transaction_steam_wallet_info_dict = transaction_steam_wallet_info_instance.to_dict()
# create an instance of TransactionSteamWalletInfo from a dict
transaction_steam_wallet_info_from_dict = TransactionSteamWalletInfo.from_dict(transaction_steam_wallet_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


