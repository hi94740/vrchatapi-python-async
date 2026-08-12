# NotificationV2Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** |  | 
**icon** | **str** |  | 
**text** | **str** |  | 
**text_key** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from vrchatapi.models.notification_v2_response import NotificationV2Response

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationV2Response from a JSON string
notification_v2_response_instance = NotificationV2Response.from_json(json)
# print the JSON string representation of the object
print(NotificationV2Response.to_json())

# convert the object into a dict
notification_v2_response_dict = notification_v2_response_instance.to_dict()
# create an instance of NotificationV2Response from a dict
notification_v2_response_from_dict = NotificationV2Response.from_dict(notification_v2_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


