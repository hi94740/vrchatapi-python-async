# InstanceContentSettings

Types of dynamic user content permitted in an instance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drones** | **bool** |  | [optional] [default to True]
**emoji** | **bool** |  | [optional] [default to True]
**pedestals** | **bool** |  | [optional] [default to True]
**prints** | **bool** |  | [optional] [default to True]
**props** | **bool** |  | [optional] [default to True]
**stickers** | **bool** |  | [optional] [default to True]

## Example

```python
from vrchatapi.models.instance_content_settings import InstanceContentSettings

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceContentSettings from a JSON string
instance_content_settings_instance = InstanceContentSettings.from_json(json)
# print the JSON string representation of the object
print(InstanceContentSettings.to_json())

# convert the object into a dict
instance_content_settings_dict = instance_content_settings_instance.to_dict()
# create an instance of InstanceContentSettings from a dict
instance_content_settings_from_dict = InstanceContentSettings.from_dict(instance_content_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


