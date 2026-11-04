# CalendarEventDiscovery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_cursor** | **str** | Pass back as the &#x60;nextCursor&#x60; query parameter to read the page after this one. | [optional] 
**results** | [**List[CalendarEvent]**](CalendarEvent.md) |  | 

## Example

```python
from vrchatapi.models.calendar_event_discovery import CalendarEventDiscovery

# TODO update the JSON string below
json = "{}"
# create an instance of CalendarEventDiscovery from a JSON string
calendar_event_discovery_instance = CalendarEventDiscovery.from_json(json)
# print the JSON string representation of the object
print(CalendarEventDiscovery.to_json())

# convert the object into a dict
calendar_event_discovery_dict = calendar_event_discovery_instance.to_dict()
# create an instance of CalendarEventDiscovery from a dict
calendar_event_discovery_from_dict = CalendarEventDiscovery.from_dict(calendar_event_discovery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


