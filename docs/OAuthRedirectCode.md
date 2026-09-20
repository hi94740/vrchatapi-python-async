# OAuthRedirectCode

A short-lived code used to hand the current session to an OAuth redirect.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 

## Example

```python
from vrchatapi.models.o_auth_redirect_code import OAuthRedirectCode

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthRedirectCode from a JSON string
o_auth_redirect_code_instance = OAuthRedirectCode.from_json(json)
# print the JSON string representation of the object
print(OAuthRedirectCode.to_json())

# convert the object into a dict
o_auth_redirect_code_dict = o_auth_redirect_code_instance.to_dict()
# create an instance of OAuthRedirectCode from a dict
o_auth_redirect_code_from_dict = OAuthRedirectCode.from_dict(o_auth_redirect_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


