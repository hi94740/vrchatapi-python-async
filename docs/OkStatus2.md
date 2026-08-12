# OkStatus2

Another status response consisting of solely a string description of whether the result of an operation was ok.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **str** | The actual status itself | 

## Example

```python
from vrchatapi.models.ok_status2 import OkStatus2

# TODO update the JSON string below
json = "{}"
# create an instance of OkStatus2 from a JSON string
ok_status2_instance = OkStatus2.from_json(json)
# print the JSON string representation of the object
print(OkStatus2.to_json())

# convert the object into a dict
ok_status2_dict = ok_status2_instance.to_dict()
# create an instance of OkStatus2 from a dict
ok_status2_from_dict = OkStatus2.from_dict(ok_status2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


