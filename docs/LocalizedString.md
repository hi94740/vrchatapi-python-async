# LocalizedString

A string the client resolves through its localization table, falling back to `fallback` when the key is unknown.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fallback** | **str** | The text to show when &#x60;key&#x60; cannot be resolved. | 
**key** | **str** | The localization key. | 

## Example

```python
from vrchatapi.models.localized_string import LocalizedString

# TODO update the JSON string below
json = "{}"
# create an instance of LocalizedString from a JSON string
localized_string_instance = LocalizedString.from_json(json)
# print the JSON string representation of the object
print(LocalizedString.to_json())

# convert the object into a dict
localized_string_dict = localized_string_instance.to_dict()
# create an instance of LocalizedString from a dict
localized_string_from_dict = LocalizedString.from_dict(localized_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


