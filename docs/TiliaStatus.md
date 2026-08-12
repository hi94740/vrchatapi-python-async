# TiliaStatus



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**economy_online** | **bool** |  | 
**economy_state** | **int** |  | [optional] 
**planned_offline_window_end** | **datetime** |  | [optional] 
**planned_offline_window_start** | **datetime** |  | [optional] 

## Example

```python
from vrchatapi.models.tilia_status import TiliaStatus

# TODO update the JSON string below
json = "{}"
# create an instance of TiliaStatus from a JSON string
tilia_status_instance = TiliaStatus.from_json(json)
# print the JSON string representation of the object
print(TiliaStatus.to_json())

# convert the object into a dict
tilia_status_dict = tilia_status_instance.to_dict()
# create an instance of TiliaStatus from a dict
tilia_status_from_dict = TiliaStatus.from_dict(tilia_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


