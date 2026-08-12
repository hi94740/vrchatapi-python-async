# TransactionAgreement

Represents a single Transaction, which is likely between VRChat and Steam.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agreement** | **str** |  | 
**agreement_id** | **str** |  | 
**billing_type** | **str** |  | 
**currency** | **str** |  | 
**end_date** | **str** |  | 
**failed_attempts** | **int** |  | 
**frequency** | **int** |  | 
**item_id** | **int** |  | 
**last_amount** | **float** |  | 
**last_amount_vat** | **float** |  | 
**last_payment** | **str** |  | 
**next_payment** | **str** |  | 
**outstanding** | **int** |  | 
**period** | **str** |  | 
**recurring_amt** | **float** |  | 
**start_date** | **str** |  | 
**status** | **str** | This is NOT TransactionStatus, but whatever Steam return. | 
**time_created** | **str** |  | 

## Example

```python
from vrchatapi.models.transaction_agreement import TransactionAgreement

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionAgreement from a JSON string
transaction_agreement_instance = TransactionAgreement.from_json(json)
# print the JSON string representation of the object
print(TransactionAgreement.to_json())

# convert the object into a dict
transaction_agreement_dict = transaction_agreement_instance.to_dict()
# create an instance of TransactionAgreement from a dict
transaction_agreement_from_dict = TransactionAgreement.from_dict(transaction_agreement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


