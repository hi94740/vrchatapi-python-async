# PaginatedCalendarEventList

An offset-based list of CalendarEvents

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_next** | **bool** | Whether there are more results after this page. | [optional] 
**results** | [**List[CalendarEvent]**](CalendarEvent.md) |   | [optional] 
**total_count** | **int** | The total number of results that the query would return if there were no pagination. | [optional] 

## Example

```python
from vrchatapi.models.paginated_calendar_event_list import PaginatedCalendarEventList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedCalendarEventList from a JSON string
paginated_calendar_event_list_instance = PaginatedCalendarEventList.from_json(json)
# print the JSON string representation of the object
print(PaginatedCalendarEventList.to_json())

# convert the object into a dict
paginated_calendar_event_list_dict = paginated_calendar_event_list_instance.to_dict()
# create an instance of PaginatedCalendarEventList from a dict
paginated_calendar_event_list_from_dict = PaginatedCalendarEventList.from_dict(paginated_calendar_event_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


