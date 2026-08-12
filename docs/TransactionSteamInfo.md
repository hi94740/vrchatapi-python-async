# TransactionSteamInfo



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Steam Order ID | 
**steam_id** | **str** | Steam User ID | 
**steam_url** | **str** | Empty | 
**trans_id** | **str** | Steam Transaction ID, NOT the same as VRChat TransactionID | 
**wallet_info** | [**TransactionSteamWalletInfo**](TransactionSteamWalletInfo.md) |  | 

## Example

```python
from vrchatapi.models.transaction_steam_info import TransactionSteamInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionSteamInfo from a JSON string
transaction_steam_info_instance = TransactionSteamInfo.from_json(json)
# print the JSON string representation of the object
print(TransactionSteamInfo.to_json())

# convert the object into a dict
transaction_steam_info_dict = transaction_steam_info_instance.to_dict()
# create an instance of TransactionSteamInfo from a dict
transaction_steam_info_from_dict = TransactionSteamInfo.from_dict(transaction_steam_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


