# LimitedUnityPackage



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**platform** | **str** | This is normally &#x60;android&#x60;, &#x60;ios&#x60;, &#x60;standalonewindows&#x60;, &#x60;web&#x60;, or the empty value &#x60;&#x60;, but also supposedly can be any random Unity version such as &#x60;2019.2.4-801-Release&#x60; or &#x60;2019.2.2-772-Release&#x60; or even &#x60;unknownplatform&#x60;. | 
**unity_version** | **str** |  | 

## Example

```python
from vrchatapi.models.limited_unity_package import LimitedUnityPackage

# TODO update the JSON string below
json = "{}"
# create an instance of LimitedUnityPackage from a JSON string
limited_unity_package_instance = LimitedUnityPackage.from_json(json)
# print the JSON string representation of the object
print(LimitedUnityPackage.to_json())

# convert the object into a dict
limited_unity_package_dict = limited_unity_package_instance.to_dict()
# create an instance of LimitedUnityPackage from a dict
limited_unity_package_from_dict = LimitedUnityPackage.from_dict(limited_unity_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


