# SsoToken

A token for a third-party service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | 

## Example

```python
from vrchatapi.models.sso_token import SsoToken

# TODO update the JSON string below
json = "{}"
# create an instance of SsoToken from a JSON string
sso_token_instance = SsoToken.from_json(json)
# print the JSON string representation of the object
print(SsoToken.to_json())

# convert the object into a dict
sso_token_dict = sso_token_instance.to_dict()
# create an instance of SsoToken from a dict
sso_token_from_dict = SsoToken.from_dict(sso_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


