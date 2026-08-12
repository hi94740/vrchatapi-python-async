# ServiceQueueStats

Statistics about the user's currently queued service request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**estimated_service_duration_seconds** | **int** |  | 

## Example

```python
from vrchatapi.models.service_queue_stats import ServiceQueueStats

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceQueueStats from a JSON string
service_queue_stats_instance = ServiceQueueStats.from_json(json)
# print the JSON string representation of the object
print(ServiceQueueStats.to_json())

# convert the object into a dict
service_queue_stats_dict = service_queue_stats_instance.to_dict()
# create an instance of ServiceQueueStats from a dict
service_queue_stats_from_dict = ServiceQueueStats.from_dict(service_queue_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


