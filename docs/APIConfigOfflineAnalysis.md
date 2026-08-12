# APIConfigOfflineAnalysis

Whether to allow offline analysis

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**android** | **bool** | Whether to allow offline analysis | [optional] [default to True]
**standalonewindows** | **bool** | Whether to allow offline analysis | [optional] [default to True]

## Example

```python
from vrchatapi.models.api_config_offline_analysis import APIConfigOfflineAnalysis

# TODO update the JSON string below
json = "{}"
# create an instance of APIConfigOfflineAnalysis from a JSON string
api_config_offline_analysis_instance = APIConfigOfflineAnalysis.from_json(json)
# print the JSON string representation of the object
print(APIConfigOfflineAnalysis.to_json())

# convert the object into a dict
api_config_offline_analysis_dict = api_config_offline_analysis_instance.to_dict()
# create an instance of APIConfigOfflineAnalysis from a dict
api_config_offline_analysis_from_dict = APIConfigOfflineAnalysis.from_dict(api_config_offline_analysis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


