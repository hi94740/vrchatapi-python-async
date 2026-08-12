# CalendarEventDiscovery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_cursor** | **str** | Base64-encoded JSON:   type: object   properties:     dataSource:       type: string       enum:         - featured         - personalized     dataIndex:       type: integer       format: int32     phase:       type: string       enum:         - all         - live         - upcoming       description: see CalendarEventDiscoveryScope     asOf:       type: integer       format: int64       description: milliseconds since Unix epoch     paramHash:       type: string       format: string       description: Base64-encoded 256-bit hash of the original query parameters | 
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


