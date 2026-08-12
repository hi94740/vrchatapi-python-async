# Pending2FAResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**qr_code_data_url** | **str** |  | 
**secret** | **str** |  | 

## Example

```python
from vrchatapi.models.pending2_fa_result import Pending2FAResult

# TODO update the JSON string below
json = "{}"
# create an instance of Pending2FAResult from a JSON string
pending2_fa_result_instance = Pending2FAResult.from_json(json)
# print the JSON string representation of the object
print(Pending2FAResult.to_json())

# convert the object into a dict
pending2_fa_result_dict = pending2_fa_result_instance.to_dict()
# create an instance of Pending2FAResult from a dict
pending2_fa_result_from_dict = Pending2FAResult.from_dict(pending2_fa_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


