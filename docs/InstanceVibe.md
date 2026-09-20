# InstanceVibe

A vibe an instance can be tagged with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted** | **bool** |  | 
**id** | **str** |  | 
**title** | **str** |  | 

## Example

```python
from vrchatapi.models.instance_vibe import InstanceVibe

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceVibe from a JSON string
instance_vibe_instance = InstanceVibe.from_json(json)
# print the JSON string representation of the object
print(InstanceVibe.to_json())

# convert the object into a dict
instance_vibe_dict = instance_vibe_instance.to_dict()
# create an instance of InstanceVibe from a dict
instance_vibe_from_dict = InstanceVibe.from_dict(instance_vibe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


