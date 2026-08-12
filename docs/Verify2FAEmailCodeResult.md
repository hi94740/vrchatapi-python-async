# Verify2FAEmailCodeResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verified** | **bool** |  | 

## Example

```python
from vrchatapi.models.verify2_fa_email_code_result import Verify2FAEmailCodeResult

# TODO update the JSON string below
json = "{}"
# create an instance of Verify2FAEmailCodeResult from a JSON string
verify2_fa_email_code_result_instance = Verify2FAEmailCodeResult.from_json(json)
# print the JSON string representation of the object
print(Verify2FAEmailCodeResult.to_json())

# convert the object into a dict
verify2_fa_email_code_result_dict = verify2_fa_email_code_result_instance.to_dict()
# create an instance of Verify2FAEmailCodeResult from a dict
verify2_fa_email_code_result_from_dict = Verify2FAEmailCodeResult.from_dict(verify2_fa_email_code_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


