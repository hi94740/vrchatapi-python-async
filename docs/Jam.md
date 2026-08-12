# Jam



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**id** | **str** |  | 
**is_visible** | **bool** |  | 
**more_info** | **str** |  | 
**state** | **str** | One of: - submissions_open - closed | 
**state_change_dates** | [**JamStateChangeDates**](JamStateChangeDates.md) |  | 
**submission_content_gate_date** | **datetime** |  | 
**submission_content_gated** | **bool** |  | 
**title** | **str** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from vrchatapi.models.jam import Jam

# TODO update the JSON string below
json = "{}"
# create an instance of Jam from a JSON string
jam_instance = Jam.from_json(json)
# print the JSON string representation of the object
print(Jam.to_json())

# convert the object into a dict
jam_dict = jam_instance.to_dict()
# create an instance of Jam from a dict
jam_from_dict = Jam.from_dict(jam_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


