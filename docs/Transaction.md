# Transaction



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agreement** | [**TransactionAgreement**](TransactionAgreement.md) |  | [optional] 
**created_at** | **datetime** |  | 
**error** | **str** |  | 
**id** | **str** |  | 
**is_gift** | **bool** |  | [optional] [default to False]
**is_tokens** | **bool** |  | [optional] [default to False]
**sandbox** | **bool** |  | [default to False]
**status** | [**TransactionStatus**](TransactionStatus.md) |  | [default to TransactionStatus.ACTIVE]
**steam** | [**TransactionSteamInfo**](TransactionSteamInfo.md) |  | [optional] 
**subscription** | [**Subscription**](Subscription.md) |  | 
**updated_at** | **datetime** |  | 
**user_display_name** | **str** |  | [optional] 
**user_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 

## Example

```python
from vrchatapi.models.transaction import Transaction

# TODO update the JSON string below
json = "{}"
# create an instance of Transaction from a JSON string
transaction_instance = Transaction.from_json(json)
# print the JSON string representation of the object
print(Transaction.to_json())

# convert the object into a dict
transaction_dict = transaction_instance.to_dict()
# create an instance of Transaction from a dict
transaction_from_dict = Transaction.from_dict(transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


