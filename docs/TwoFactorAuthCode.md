# TwoFactorAuthCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 

## Example

```python
from vrchatapi.models.two_factor_auth_code import TwoFactorAuthCode

# TODO update the JSON string below
json = "{}"
# create an instance of TwoFactorAuthCode from a JSON string
two_factor_auth_code_instance = TwoFactorAuthCode.from_json(json)
# print the JSON string representation of the object
print(TwoFactorAuthCode.to_json())

# convert the object into a dict
two_factor_auth_code_dict = two_factor_auth_code_instance.to_dict()
# create an instance of TwoFactorAuthCode from a dict
two_factor_auth_code_from_dict = TwoFactorAuthCode.from_dict(two_factor_auth_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


