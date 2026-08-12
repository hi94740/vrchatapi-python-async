# CreateCalendarEventRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_type** | [**CalendarEventAccess**](CalendarEventAccess.md) |  | [default to CalendarEventAccess.PUBLIC]
**category** | [**CalendarEventCategory**](CalendarEventCategory.md) |  | [default to CalendarEventCategory.OTHER]
**close_instance_after_end_minutes** | **int** |  | [optional] 
**description** | **str** |  | 
**ends_at** | **datetime** | Time the event ends at | 
**featured** | **bool** |  | [optional] 
**guest_early_join_minutes** | **int** |  | [optional] 
**host_early_join_minutes** | **int** |  | [optional] 
**image_id** | **str** |  | [optional] 
**is_draft** | **bool** |  | [optional] 
**languages** | **List[str]** |  | [optional] 
**occurrence_kind** | [**CalendarEventOccurrenceKind**](CalendarEventOccurrenceKind.md) |  | [optional] [default to CalendarEventOccurrenceKind.SINGLE]
**parent_id** | **str** |  | [optional] 
**platforms** | [**List[CalendarEventPlatform]**](CalendarEventPlatform.md) |  | [optional] 
**recurrence** | [**CalendarEventRecurrence**](CalendarEventRecurrence.md) |  | [optional] 
**role_ids** | **List[str]** |  | [optional] 
**send_creation_notification** | **bool** | Send notification to group members. | 
**starts_at** | **datetime** | Time the event starts at | 
**tags** | **List[str]** |  | [optional] 
**title** | **str** | Event title | 
**uses_instance_overflow** | **bool** |  | [optional] 

## Example

```python
from vrchatapi.models.create_calendar_event_request import CreateCalendarEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCalendarEventRequest from a JSON string
create_calendar_event_request_instance = CreateCalendarEventRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCalendarEventRequest.to_json())

# convert the object into a dict
create_calendar_event_request_dict = create_calendar_event_request_instance.to_dict()
# create an instance of CreateCalendarEventRequest from a dict
create_calendar_event_request_from_dict = CreateCalendarEventRequest.from_dict(create_calendar_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


