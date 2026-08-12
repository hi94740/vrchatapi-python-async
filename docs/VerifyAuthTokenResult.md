# VerifyAuthTokenResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | 
**token** | **str** |  | 

## Example

```python
from vrchatapi.models.verify_auth_token_result import VerifyAuthTokenResult

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyAuthTokenResult from a JSON string
verify_auth_token_result_instance = VerifyAuthTokenResult.from_json(json)
# print the JSON string representation of the object
print(VerifyAuthTokenResult.to_json())

# convert the object into a dict
verify_auth_token_result_dict = verify_auth_token_result_instance.to_dict()
# create an instance of VerifyAuthTokenResult from a dict
verify_auth_token_result_from_dict = VerifyAuthTokenResult.from_dict(verify_auth_token_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


