# InfoPushExperiment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**variant** | **str** |  | [optional] 

## Example

```python
from vrchatapi.models.info_push_experiment import InfoPushExperiment

# TODO update the JSON string below
json = "{}"
# create an instance of InfoPushExperiment from a JSON string
info_push_experiment_instance = InfoPushExperiment.from_json(json)
# print the JSON string representation of the object
print(InfoPushExperiment.to_json())

# convert the object into a dict
info_push_experiment_dict = info_push_experiment_instance.to_dict()
# create an instance of InfoPushExperiment from a dict
info_push_experiment_from_dict = InfoPushExperiment.from_dict(info_push_experiment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


