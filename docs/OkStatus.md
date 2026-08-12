# OkStatus

A status response consisting of solely a string description of whether the result of an operation was ok.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **str** | The actual status itself | [default to 'maybe?']

## Example

```python
from vrchatapi.models.ok_status import OkStatus

# TODO update the JSON string below
json = "{}"
# create an instance of OkStatus from a JSON string
ok_status_instance = OkStatus.from_json(json)
# print the JSON string representation of the object
print(OkStatus.to_json())

# convert the object into a dict
ok_status_dict = ok_status_instance.to_dict()
# create an instance of OkStatus from a dict
ok_status_from_dict = OkStatus.from_dict(ok_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


