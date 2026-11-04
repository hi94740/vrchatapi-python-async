# InstanceDiscovery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribution_id** | **str** |  | 
**instances** | [**List[LimitedInstance]**](LimitedInstance.md) |  | 

## Example

```python
from vrchatapi.models.instance_discovery import InstanceDiscovery

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceDiscovery from a JSON string
instance_discovery_instance = InstanceDiscovery.from_json(json)
# print the JSON string representation of the object
print(InstanceDiscovery.to_json())

# convert the object into a dict
instance_discovery_dict = instance_discovery_instance.to_dict()
# create an instance of InstanceDiscovery from a dict
instance_discovery_from_dict = InstanceDiscovery.from_dict(instance_discovery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


