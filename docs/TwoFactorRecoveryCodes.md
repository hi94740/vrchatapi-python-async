# TwoFactorRecoveryCodes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**otp** | [**List[TwoFactorRecoveryCodesOtpInner]**](TwoFactorRecoveryCodesOtpInner.md) |  | [optional] 
**requires_two_factor_auth** | **List[str]** |  | [optional] 

## Example

```python
from vrchatapi.models.two_factor_recovery_codes import TwoFactorRecoveryCodes

# TODO update the JSON string below
json = "{}"
# create an instance of TwoFactorRecoveryCodes from a JSON string
two_factor_recovery_codes_instance = TwoFactorRecoveryCodes.from_json(json)
# print the JSON string representation of the object
print(TwoFactorRecoveryCodes.to_json())

# convert the object into a dict
two_factor_recovery_codes_dict = two_factor_recovery_codes_instance.to_dict()
# create an instance of TwoFactorRecoveryCodes from a dict
two_factor_recovery_codes_from_dict = TwoFactorRecoveryCodes.from_dict(two_factor_recovery_codes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


