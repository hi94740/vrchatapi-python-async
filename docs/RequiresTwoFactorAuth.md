# RequiresTwoFactorAuth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requires_two_factor_auth** | [**List[TwoFactorAuthType]**](TwoFactorAuthType.md) |  | 

## Example

```python
from vrchatapi.models.requires_two_factor_auth import RequiresTwoFactorAuth

# TODO update the JSON string below
json = "{}"
# create an instance of RequiresTwoFactorAuth from a JSON string
requires_two_factor_auth_instance = RequiresTwoFactorAuth.from_json(json)
# print the JSON string representation of the object
print(RequiresTwoFactorAuth.to_json())

# convert the object into a dict
requires_two_factor_auth_dict = requires_two_factor_auth_instance.to_dict()
# create an instance of RequiresTwoFactorAuth from a dict
requires_two_factor_auth_from_dict = RequiresTwoFactorAuth.from_dict(requires_two_factor_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


