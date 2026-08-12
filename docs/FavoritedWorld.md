# FavoritedWorld



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 
**author_name** | **str** |  | 
**capacity** | **int** |  | 
**created_at** | **datetime** |  | [optional] 
**default_content_settings** | [**InstanceContentSettings**](InstanceContentSettings.md) |  | [optional] 
**description** | **str** |  | [optional] 
**favorite_group** | **str** |  | 
**favorite_id** | **str** |  | 
**favorites** | **int** |  | [optional] [default to 0]
**featured** | **bool** |  | [optional] [default to False]
**heat** | **int** |  | [optional] [default to 0]
**id** | **str** | WorldID be \&quot;offline\&quot; on User profiles if you are not friends with that user. | 
**image_url** | **str** |  | 
**labs_publication_date** | **str** |  | [optional] 
**name** | **str** |  | 
**occupants** | **int** |  | [default to 0]
**organization** | **str** |  | [optional] [default to 'vrchat']
**popularity** | **int** |  | [optional] [default to 0]
**preview_youtube_id** | **str** |  | [optional] 
**publication_date** | **str** |  | [optional] 
**recommended_capacity** | **int** |  | [optional] 
**release_status** | [**ReleaseStatus**](ReleaseStatus.md) |  | [default to ReleaseStatus.PUBLIC]
**tags** | **List[str]** |   | [optional] 
**thumbnail_image_url** | **str** |  | 
**udon_products** | **List[str]** |  | [optional] 
**unity_packages** | [**List[UnityPackage]**](UnityPackage.md) |   | [optional] 
**updated_at** | **datetime** |  | [optional] 
**url_list** | **List[str]** |  | [optional] 
**version** | **int** |  | [optional] 
**visits** | **int** |  | [optional] [default to 0]

## Example

```python
from vrchatapi.models.favorited_world import FavoritedWorld

# TODO update the JSON string below
json = "{}"
# create an instance of FavoritedWorld from a JSON string
favorited_world_instance = FavoritedWorld.from_json(json)
# print the JSON string representation of the object
print(FavoritedWorld.to_json())

# convert the object into a dict
favorited_world_dict = favorited_world_instance.to_dict()
# create an instance of FavoritedWorld from a dict
favorited_world_from_dict = FavoritedWorld.from_dict(favorited_world_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


