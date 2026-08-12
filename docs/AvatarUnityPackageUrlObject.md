# AvatarUnityPackageUrlObject

**Deprecation:** `Object` has unknown usage/fields, and is always empty. Use normal `Url` field instead.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unity_package_url** | **str** |  | [optional] 

## Example

```python
from vrchatapi.models.avatar_unity_package_url_object import AvatarUnityPackageUrlObject

# TODO update the JSON string below
json = "{}"
# create an instance of AvatarUnityPackageUrlObject from a JSON string
avatar_unity_package_url_object_instance = AvatarUnityPackageUrlObject.from_json(json)
# print the JSON string representation of the object
print(AvatarUnityPackageUrlObject.to_json())

# convert the object into a dict
avatar_unity_package_url_object_dict = avatar_unity_package_url_object_instance.to_dict()
# create an instance of AvatarUnityPackageUrlObject from a dict
avatar_unity_package_url_object_from_dict = AvatarUnityPackageUrlObject.from_dict(avatar_unity_package_url_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


