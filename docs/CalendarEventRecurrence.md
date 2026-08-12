# CalendarEventRecurrence

Details about how a recurring event will be scheduled. If the event is to be scheduled indefinitely, this will lack an \"end\" property.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days_of_week** | [**List[CalendarDayOfWeek]**](CalendarDayOfWeek.md) | Which days of the week the event will be scheduled, only valid/present for \&quot;weekly\&quot; recurring events | [optional] 
**end** | [**CalendarEventRecurrenceEnd**](CalendarEventRecurrenceEnd.md) |  | [optional] 
**frequency** | [**CalendarEventFrequency**](CalendarEventFrequency.md) |  | [default to CalendarEventFrequency.WEEKLY]
**interval** | **int** | How often the event will be scheduled, in units of \&quot;frequency\&quot; | 
**timezone** | **str** | The timezone the event will be scheduled in, in Area/Location format | 

## Example

```python
from vrchatapi.models.calendar_event_recurrence import CalendarEventRecurrence

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEventRecurrence from a JSON string
calendar_event_recurrence_instance = CalendarEventRecurrence.from_json(json)
# print the JSON string representation of the object
print(CalendarEventRecurrence.to_json())

# convert the object into a dict
calendar_event_recurrence_dict = calendar_event_recurrence_instance.to_dict()
# create an instance of CalendarEventRecurrence from a dict
calendar_event_recurrence_from_dict = CalendarEventRecurrence.from_dict(calendar_event_recurrence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


