# AdminUnityPackage



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_url** | **str** |  | 
**asset_version** | **int** |  | 
**platform** | **str** | This is normally &#x60;android&#x60;, &#x60;ios&#x60;, &#x60;standalonewindows&#x60;, &#x60;web&#x60;, or the empty value &#x60;&#x60;, but also supposedly can be any random Unity version such as &#x60;2019.2.4-801-Release&#x60; or &#x60;2019.2.2-772-Release&#x60; or even &#x60;unknownplatform&#x60;. | 
**unity_version** | **str** |  | [default to '2022.3.22f1-DWR']
**variant** | **str** |  | 

## Example

```python
from vrchatapi.models.admin_unity_package import AdminUnityPackage

# TODO update the JSON string below
json = "{}"
# create an instance of AdminUnityPackage from a JSON string
admin_unity_package_instance = AdminUnityPackage.from_json(json)
# print the JSON string representation of the object
print(AdminUnityPackage.to_json())

# convert the object into a dict
admin_unity_package_dict = admin_unity_package_instance.to_dict()
# create an instance of AdminUnityPackage from a dict
admin_unity_package_from_dict = AdminUnityPackage.from_dict(admin_unity_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


