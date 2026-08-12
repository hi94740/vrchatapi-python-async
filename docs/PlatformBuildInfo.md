# PlatformBuildInfo

Build information for a platform

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_build_number** | **int** | Minimum build number required for the platform | 
**redirection_address** | **str** | Redirection URL for updating the app | [optional] 

## Example

```python
from vrchatapi.models.platform_build_info import PlatformBuildInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformBuildInfo from a JSON string
platform_build_info_instance = PlatformBuildInfo.from_json(json)
# print the JSON string representation of the object
print(PlatformBuildInfo.to_json())

# convert the object into a dict
platform_build_info_dict = platform_build_info_instance.to_dict()
# create an instance of PlatformBuildInfo from a dict
platform_build_info_from_dict = PlatformBuildInfo.from_dict(platform_build_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


