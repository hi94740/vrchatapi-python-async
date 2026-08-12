# TwoFactorEmailCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 

## Example

```python
from vrchatapi.models.two_factor_email_code import TwoFactorEmailCode

# TODO update the JSON string below
json = "{}"
# create an instance of TwoFactorEmailCode from a JSON string
two_factor_email_code_instance = TwoFactorEmailCode.from_json(json)
# print the JSON string representation of the object
print(TwoFactorEmailCode.to_json())

# convert the object into a dict
two_factor_email_code_dict = two_factor_email_code_instance.to_dict()
# create an instance of TwoFactorEmailCode from a dict
two_factor_email_code_from_dict = TwoFactorEmailCode.from_dict(two_factor_email_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


