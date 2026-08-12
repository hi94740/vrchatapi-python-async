# AvatarPerformance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**android** | **str** |  | [optional] 
**android_sort** | **int** |  | [optional] 
**ios** | **str** |  | [optional] 
**ios_sort** | **int** |  | [optional] 
**standalonewindows** | **str** |  | [optional] 
**standalonewindows_sort** | **int** |  | [optional] 

## Example

```python
from vrchatapi.models.avatar_performance import AvatarPerformance

# TODO update the JSON string below
json = "{}"
# create an instance of AvatarPerformance from a JSON string
avatar_performance_instance = AvatarPerformance.from_json(json)
# print the JSON string representation of the object
print(AvatarPerformance.to_json())

# convert the object into a dict
avatar_performance_dict = avatar_performance_instance.to_dict()
# create an instance of AvatarPerformance from a dict
avatar_performance_from_dict = AvatarPerformance.from_dict(avatar_performance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


