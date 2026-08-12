# CalendarEventRecurrenceEnd

Details about how a recurring event stops being scheduled

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Required for \&quot;afterOccurrences\&quot; - The number of times the event will be scheduled before it stops being scheduled | [optional] 
**var_date** | **str** | Required for \&quot;afterDate\&quot; - The date and time after which the event will stop being scheduled, **without timezone or offset** | [optional] 
**type** | [**CalendarEventRecurrenceEndType**](CalendarEventRecurrenceEndType.md) |  | [default to CalendarEventRecurrenceEndType.AFTERDATE]

## Example

```python
from vrchatapi.models.calendar_event_recurrence_end import CalendarEventRecurrenceEnd

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEventRecurrenceEnd from a JSON string
calendar_event_recurrence_end_instance = CalendarEventRecurrenceEnd.from_json(json)
# print the JSON string representation of the object
print(CalendarEventRecurrenceEnd.to_json())

# convert the object into a dict
calendar_event_recurrence_end_dict = calendar_event_recurrence_end_instance.to_dict()
# create an instance of CalendarEventRecurrenceEnd from a dict
calendar_event_recurrence_end_from_dict = CalendarEventRecurrenceEnd.from_dict(calendar_event_recurrence_end_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


