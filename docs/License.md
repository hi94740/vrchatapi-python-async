# License


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**for_action** | [**LicenseAction**](LicenseAction.md) |  | [default to LicenseAction.HAVE]
**for_id** | **str** | Either a AvatarID, LicenseGroupID, PermissionID or ProductID. This depends on the &#x60;forType&#x60; field. | 
**for_name** | **str** |  | 
**for_type** | [**LicenseType**](LicenseType.md) |  | [default to LicenseType.PERMISSION]

## Example

```python
from vrchatapi.models.license import License

# TODO update the JSON string below
json = "{}"
# create an instance of License from a JSON string
license_instance = License.from_json(json)
# print the JSON string representation of the object
print(License.to_json())

# convert the object into a dict
license_dict = license_instance.to_dict()
# create an instance of License from a dict
license_from_dict = License.from_dict(license_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


