# BetaUserField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_values** | **List[str]** |  | [optional] 
**exclude_from_analytics** | **bool** |  | [optional] 
**required** | **bool** |  | 

## Example

```python
from vrchatapi.models.beta_user_field import BetaUserField

# TODO update the JSON string below
json = "{}"
# create an instance of BetaUserField from a JSON string
beta_user_field_instance = BetaUserField.from_json(json)
# print the JSON string representation of the object
print(BetaUserField.to_json())

# convert the object into a dict
beta_user_field_dict = beta_user_field_instance.to_dict()
# create an instance of BetaUserField from a dict
beta_user_field_from_dict = BetaUserField.from_dict(beta_user_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


