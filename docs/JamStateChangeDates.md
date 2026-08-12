# JamStateChangeDates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**closed** | **datetime** |  | [optional] 
**submissions_closed** | **datetime** |  | [optional] 
**submissions_opened** | **datetime** |  | [optional] 
**winners_selected** | **datetime** |  | [optional] 

## Example

```python
from vrchatapi.models.jam_state_change_dates import JamStateChangeDates

# TODO update the JSON string below
json = "{}"
# create an instance of JamStateChangeDates from a JSON string
jam_state_change_dates_instance = JamStateChangeDates.from_json(json)
# print the JSON string representation of the object
print(JamStateChangeDates.to_json())

# convert the object into a dict
jam_state_change_dates_dict = jam_state_change_dates_instance.to_dict()
# create an instance of JamStateChangeDates from a dict
jam_state_change_dates_from_dict = JamStateChangeDates.from_dict(jam_state_change_dates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


