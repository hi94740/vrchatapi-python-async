# AgeVerificationStatusResult

The caller's age verification status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 

## Example

```python
from vrchatapi.models.age_verification_status_result import AgeVerificationStatusResult

# TODO update the JSON string below
json = "{}"
# create an instance of AgeVerificationStatusResult from a JSON string
age_verification_status_result_instance = AgeVerificationStatusResult.from_json(json)
# print the JSON string representation of the object
print(AgeVerificationStatusResult.to_json())

# convert the object into a dict
age_verification_status_result_dict = age_verification_status_result_instance.to_dict()
# create an instance of AgeVerificationStatusResult from a dict
age_verification_status_result_from_dict = AgeVerificationStatusResult.from_dict(age_verification_status_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


