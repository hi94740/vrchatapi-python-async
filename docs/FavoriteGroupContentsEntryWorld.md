# FavoriteGroupContentsEntryWorld


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 
**author_name** | **str** |  | 
**capacity** | **int** |  | 
**created_at** | **datetime** |  | [optional] 
**default_content_settings** | [**InstanceContentSettings**](InstanceContentSettings.md) |  | [optional] 
**description** | **str** |  | [optional] 
**disabled_prop_abilities** | **List[object]** |  | [optional] 
**favorite_group** | **str** |  | [optional] 
**favorite_id** | **str** |  | [optional] 
**favorites** | **int** |  | [optional] [default to 0]
**featured** | **bool** |  | [optional] [default to False]
**heat** | **int** |  | [optional] [default to 0]
**id** | **str** | WorldID be \&quot;offline\&quot; on User profiles if you are not friends with that user. | 
**image_url** | **str** |  | 
**is_hype_train_eligible** | **bool** |  | [optional] 
**labs_publication_date** | **str** |  | [optional] 
**name** | **str** |  | 
**occupants** | **int** |  | 
**organization** | **str** |  | [optional] [default to 'vrchat']
**popularity** | **int** |  | [optional] [default to 0]
**preview_youtube_id** | **str** |  | [optional] 
**publication_date** | **str** |  | [optional] 
**recommended_capacity** | **int** |  | [optional] 
**release_status** | [**ReleaseStatus**](ReleaseStatus.md) |  | [default to ReleaseStatus.PUBLIC]
**store_id** | **str** |  | [optional] 
**tags** | **List[str]** |   | [optional] 
**thumbnail_image_url** | **str** |  | 
**udon_products** | **List[str]** |  | [optional] 
**unity_packages** | [**List[UnityPackage]**](UnityPackage.md) |   | [optional] 
**updated_at** | **datetime** |  | [optional] 
**url_list** | **List[str]** |  | [optional] 
**version** | **int** |  | [optional] 
**visits** | **int** |  | [optional] [default to 0]
**is_secure** | **bool** |  | 

## Example

```python
from vrchatapi.models.favorite_group_contents_entry_world import FavoriteGroupContentsEntryWorld

# TODO update the JSON string below
json = "{}"
# create an instance of FavoriteGroupContentsEntryWorld from a JSON string
favorite_group_contents_entry_world_instance = FavoriteGroupContentsEntryWorld.from_json(json)
# print the JSON string representation of the object
print(FavoriteGroupContentsEntryWorld.to_json())

# convert the object into a dict
favorite_group_contents_entry_world_dict = favorite_group_contents_entry_world_instance.to_dict()
# create an instance of FavoriteGroupContentsEntryWorld from a dict
favorite_group_contents_entry_world_from_dict = FavoriteGroupContentsEntryWorld.from_dict(favorite_group_contents_entry_world_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


