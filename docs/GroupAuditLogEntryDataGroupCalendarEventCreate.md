# GroupAuditLogEntryDataGroupCalendarEventCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_type** | [**CalendarEventAccess**](CalendarEventAccess.md) |  | [default to CalendarEventAccess.PUBLIC]
**description** | **str** | The description of the calendar event. | 
**image_id** | **str** |  | 
**title** | **str** | The title of the calendar event. | 
**type** | **str** | The type of calendar entry. | 

## Example

```python
from vrchatapi.models.group_audit_log_entry_data_group_calendar_event_create import GroupAuditLogEntryDataGroupCalendarEventCreate

# TODO update the JSON string below
json = "{}"
# create an instance of GroupAuditLogEntryDataGroupCalendarEventCreate from a JSON string
group_audit_log_entry_data_group_calendar_event_create_instance = GroupAuditLogEntryDataGroupCalendarEventCreate.from_json(json)
# print the JSON string representation of the object
print(GroupAuditLogEntryDataGroupCalendarEventCreate.to_json())

# convert the object into a dict
group_audit_log_entry_data_group_calendar_event_create_dict = group_audit_log_entry_data_group_calendar_event_create_instance.to_dict()
# create an instance of GroupAuditLogEntryDataGroupCalendarEventCreate from a dict
group_audit_log_entry_data_group_calendar_event_create_from_dict = GroupAuditLogEntryDataGroupCalendarEventCreate.from_dict(group_audit_log_entry_data_group_calendar_event_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


