# APIConfigAvatarPerfLimiter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**android_mobile** | [**PerformanceLimiterInfo**](PerformanceLimiterInfo.md) |  | 
**pc** | [**PerformanceLimiterInfo**](PerformanceLimiterInfo.md) |  | 
**pico** | [**PerformanceLimiterInfo**](PerformanceLimiterInfo.md) |  | 
**quest** | [**PerformanceLimiterInfo**](PerformanceLimiterInfo.md) |  | 
**xr_elite** | [**PerformanceLimiterInfo**](PerformanceLimiterInfo.md) |  | 
**i_os_mobile** | [**PerformanceLimiterInfo**](PerformanceLimiterInfo.md) |  | 

## Example

```python
from vrchatapi.models.api_config_avatar_perf_limiter import APIConfigAvatarPerfLimiter

# TODO update the JSON string below
json = "{}"
# create an instance of APIConfigAvatarPerfLimiter from a JSON string
api_config_avatar_perf_limiter_instance = APIConfigAvatarPerfLimiter.from_json(json)
# print the JSON string representation of the object
print(APIConfigAvatarPerfLimiter.to_json())

# convert the object into a dict
api_config_avatar_perf_limiter_dict = api_config_avatar_perf_limiter_instance.to_dict()
# create an instance of APIConfigAvatarPerfLimiter from a dict
api_config_avatar_perf_limiter_from_dict = APIConfigAvatarPerfLimiter.from_dict(api_config_avatar_perf_limiter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


