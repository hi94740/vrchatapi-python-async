# RespondNotificationV2Request


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_data** | **str** |  | [optional] [default to '']
**response_type** | **str** |  | 

## Example

```python
from vrchatapi.models.respond_notification_v2_request import RespondNotificationV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of RespondNotificationV2Request from a JSON string
respond_notification_v2_request_instance = RespondNotificationV2Request.from_json(json)
# print the JSON string representation of the object
print(RespondNotificationV2Request.to_json())

# convert the object into a dict
respond_notification_v2_request_dict = respond_notification_v2_request_instance.to_dict()
# create an instance of RespondNotificationV2Request from a dict
respond_notification_v2_request_from_dict = RespondNotificationV2Request.from_dict(respond_notification_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


