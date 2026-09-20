# BareError

An error body carrying only a message string. Unlike `Error`, there is no nested object and no `status_code`, so a consumer that assumes the usual shape will read `undefined` from it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | 

## Example

```python
from vrchatapi.models.bare_error import BareError

# TODO update the JSON string below
json = "{}"
# create an instance of BareError from a JSON string
bare_error_instance = BareError.from_json(json)
# print the JSON string representation of the object
print(BareError.to_json())

# convert the object into a dict
bare_error_dict = bare_error_instance.to_dict()
# create an instance of BareError from a dict
bare_error_from_dict = BareError.from_dict(bare_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


