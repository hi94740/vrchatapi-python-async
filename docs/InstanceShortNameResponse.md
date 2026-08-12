# InstanceShortNameResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secure_name** | **str** |  | 
**short_name** | **str** |  | [optional] 

## Example

```python
from vrchatapi.models.instance_short_name_response import InstanceShortNameResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceShortNameResponse from a JSON string
instance_short_name_response_instance = InstanceShortNameResponse.from_json(json)
# print the JSON string representation of the object
print(InstanceShortNameResponse.to_json())

# convert the object into a dict
instance_short_name_response_dict = instance_short_name_response_instance.to_dict()
# create an instance of InstanceShortNameResponse from a dict
instance_short_name_response_from_dict = InstanceShortNameResponse.from_dict(instance_short_name_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


