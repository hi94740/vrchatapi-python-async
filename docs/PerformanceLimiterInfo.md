# PerformanceLimiterInfo

Info about the performance limits on a platform

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_seats** | **int** | Maximum amount of seats. -1 means no limit. | 

## Example

```python
from vrchatapi.models.performance_limiter_info import PerformanceLimiterInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PerformanceLimiterInfo from a JSON string
performance_limiter_info_instance = PerformanceLimiterInfo.from_json(json)
# print the JSON string representation of the object
print(PerformanceLimiterInfo.to_json())

# convert the object into a dict
performance_limiter_info_dict = performance_limiter_info_instance.to_dict()
# create an instance of PerformanceLimiterInfo from a dict
performance_limiter_info_from_dict = PerformanceLimiterInfo.from_dict(performance_limiter_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


