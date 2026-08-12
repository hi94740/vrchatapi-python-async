# TiliaKyc


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Tilia account identifier. | 
**kyc_id** | **str** | KYC verification identifier. | 
**kyc_requirements** | **str** | Requirement state reported by Tilia. | 
**match_checks** | **List[str]** | Match checks returned by Tilia. | 
**pii_level** | **str** | PII verification level. | 
**rules** | **List[str]** | Additional rules returned by Tilia. | 
**state** | **str** | Overall KYC state. | 
**tilia_retry_rule_code** | **str** | Retry rule code returned by Tilia, if any. | 

## Example

```python
from vrchatapi.models.tilia_kyc import TiliaKyc

# TODO update the JSON string below
json = "{}"
# create an instance of TiliaKyc from a JSON string
tilia_kyc_instance = TiliaKyc.from_json(json)
# print the JSON string representation of the object
print(TiliaKyc.to_json())

# convert the object into a dict
tilia_kyc_dict = tilia_kyc_instance.to_dict()
# create an instance of TiliaKyc from a dict
tilia_kyc_from_dict = TiliaKyc.from_dict(tilia_kyc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


