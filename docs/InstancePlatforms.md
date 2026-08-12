# InstancePlatforms


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**android** | **int** |  | 
**ios** | **int** |  | [optional] 
**standalonewindows** | **int** |  | 

## Example

```python
from vrchatapi.models.instance_platforms import InstancePlatforms

# TODO update the JSON string below
json = "{}"
# create an instance of InstancePlatforms from a JSON string
instance_platforms_instance = InstancePlatforms.from_json(json)
# print the JSON string representation of the object
print(InstancePlatforms.to_json())

# convert the object into a dict
instance_platforms_dict = instance_platforms_instance.to_dict()
# create an instance of InstancePlatforms from a dict
instance_platforms_from_dict = InstancePlatforms.from_dict(instance_platforms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


