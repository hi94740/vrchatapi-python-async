# PropUnityPackage



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_url** | **str** |  | 
**asset_version** | **int** |  | 
**platform** | **str** | This is normally &#x60;android&#x60;, &#x60;ios&#x60;, &#x60;standalonewindows&#x60;, &#x60;web&#x60;, or the empty value &#x60;&#x60;, but also supposedly can be any random Unity version such as &#x60;2019.2.4-801-Release&#x60; or &#x60;2019.2.2-772-Release&#x60; or even &#x60;unknownplatform&#x60;. | 
**prop_signature** | **str** |  | 
**unity_version** | **str** |  | [default to '2022.3.22f1']
**variant** | **str** |  | 

## Example

```python
from vrchatapi.models.prop_unity_package import PropUnityPackage

# TODO update the JSON string below
json = "{}"
# create an instance of PropUnityPackage from a JSON string
prop_unity_package_instance = PropUnityPackage.from_json(json)
# print the JSON string representation of the object
print(PropUnityPackage.to_json())

# convert the object into a dict
prop_unity_package_dict = prop_unity_package_instance.to_dict()
# create an instance of PropUnityPackage from a dict
prop_unity_package_from_dict = PropUnityPackage.from_dict(prop_unity_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


