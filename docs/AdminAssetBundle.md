# AdminAssetBundle



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**asset_type** | **str** |  | 
**author_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**author_name** | **str** |  | 
**description** | **str** |  | 
**image_url** | **str** |  | 
**name** | **str** |  | 
**release_status** | [**ReleaseStatus**](ReleaseStatus.md) |  | [default to ReleaseStatus.PUBLIC]
**tags** | **List[str]** |  | 
**thumbnail_image_url** | **str** |  | 
**unity_package_url** | **str** |  | 
**unity_packages** | [**List[AdminUnityPackage]**](AdminUnityPackage.md) |  | 

## Example

```python
from vrchatapi.models.admin_asset_bundle import AdminAssetBundle

# TODO update the JSON string below
json = "{}"
# create an instance of AdminAssetBundle from a JSON string
admin_asset_bundle_instance = AdminAssetBundle.from_json(json)
# print the JSON string representation of the object
print(AdminAssetBundle.to_json())

# convert the object into a dict
admin_asset_bundle_dict = admin_asset_bundle_instance.to_dict()
# create an instance of AdminAssetBundle from a dict
admin_asset_bundle_from_dict = AdminAssetBundle.from_dict(admin_asset_bundle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


