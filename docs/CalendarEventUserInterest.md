# CalendarEventUserInterest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**is_following** | **bool** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from vrchatapi.models.calendar_event_user_interest import CalendarEventUserInterest

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEventUserInterest from a JSON string
calendar_event_user_interest_instance = CalendarEventUserInterest.from_json(json)
# print the JSON string representation of the object
print(CalendarEventUserInterest.to_json())

# convert the object into a dict
calendar_event_user_interest_dict = calendar_event_user_interest_instance.to_dict()
# create an instance of CalendarEventUserInterest from a dict
calendar_event_user_interest_from_dict = CalendarEventUserInterest.from_dict(calendar_event_user_interest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


