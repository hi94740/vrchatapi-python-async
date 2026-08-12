# UpdateCalendarEventRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional] 
**close_instance_after_end_minutes** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**ends_at** | **datetime** | Time the vent starts at | [optional] 
**featured** | **bool** |  | [optional] 
**guest_early_join_minutes** | **int** |  | [optional] 
**host_early_join_minutes** | **int** |  | [optional] 
**image_id** | **str** |  | [optional] 
**is_draft** | **bool** |  | [optional] 
**languages** | **List[str]** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**platforms** | **List[str]** |  | [optional] 
**recurrence** | [**CalendarEventRecurrence**](CalendarEventRecurrence.md) |  | [optional] 
**role_ids** | **List[str]** |  | [optional] 
**send_creation_notification** | **bool** | Send notification to group members. | [optional] [default to False]
**starts_at** | **datetime** | Time the vent starts at | [optional] 
**tags** | **List[str]** |  | [optional] 
**title** | **str** | Event title | [optional] 
**uses_instance_overflow** | **bool** |  | [optional] 

## Example

```python
from vrchatapi.models.update_calendar_event_request import UpdateCalendarEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCalendarEventRequest from a JSON string
update_calendar_event_request_instance = UpdateCalendarEventRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateCalendarEventRequest.to_json())

# convert the object into a dict
update_calendar_event_request_dict = update_calendar_event_request_instance.to_dict()
# create an instance of UpdateCalendarEventRequest from a dict
update_calendar_event_request_from_dict = UpdateCalendarEventRequest.from_dict(update_calendar_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


