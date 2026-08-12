# FollowCalendarEventRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_following** | **bool** |  | 

## Example

```python
from vrchatapi.models.follow_calendar_event_request import FollowCalendarEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FollowCalendarEventRequest from a JSON string
follow_calendar_event_request_instance = FollowCalendarEventRequest.from_json(json)
# print the JSON string representation of the object
print(FollowCalendarEventRequest.to_json())

# convert the object into a dict
follow_calendar_event_request_dict = follow_calendar_event_request_instance.to_dict()
# create an instance of FollowCalendarEventRequest from a dict
follow_calendar_event_request_from_dict = FollowCalendarEventRequest.from_dict(follow_calendar_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


