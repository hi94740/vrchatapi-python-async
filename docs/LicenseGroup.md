# LicenseGroup



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**id** | **str** |  | 
**licenses** | [**List[License]**](License.md) |  | 
**name** | **str** |  | 

## Example

```python
from vrchatapi.models.license_group import LicenseGroup

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseGroup from a JSON string
license_group_instance = LicenseGroup.from_json(json)
# print the JSON string representation of the object
print(LicenseGroup.to_json())

# convert the object into a dict
license_group_dict = license_group_instance.to_dict()
# create an instance of LicenseGroup from a dict
license_group_from_dict = LicenseGroup.from_dict(license_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


