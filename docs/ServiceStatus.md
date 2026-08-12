# ServiceStatus

Status information for a service request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**id** | **str** | The id of this service, NOT the id of the thing this service was requested for. | 
**progress** | **List[object]** |  | 
**requester_user_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**state** | **str** |  | 
**subject_id** | **str** | The id of the thing this service was requested for. | 
**subject_type** | **str** | The kind of the thing this service was requested for. | 
**type** | **str** | The kind of service that was requested. | 
**updated_at** | **datetime** |  | 

## Example

```python
from vrchatapi.models.service_status import ServiceStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceStatus from a JSON string
service_status_instance = ServiceStatus.from_json(json)
# print the JSON string representation of the object
print(ServiceStatus.to_json())

# convert the object into a dict
service_status_dict = service_status_instance.to_dict()
# create an instance of ServiceStatus from a dict
service_status_from_dict = ServiceStatus.from_dict(service_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


