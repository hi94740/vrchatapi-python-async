# Verify2FAResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] [default to True]
**verified** | **bool** |  | 

## Example

```python
from vrchatapi.models.verify2_fa_result import Verify2FAResult

# TODO update the JSON string below
json = "{}"
# create an instance of Verify2FAResult from a JSON string
verify2_fa_result_instance = Verify2FAResult.from_json(json)
# print the JSON string representation of the object
print(Verify2FAResult.to_json())

# convert the object into a dict
verify2_fa_result_dict = verify2_fa_result_instance.to_dict()
# create an instance of Verify2FAResult from a dict
verify2_fa_result_from_dict = Verify2FAResult.from_dict(verify2_fa_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


