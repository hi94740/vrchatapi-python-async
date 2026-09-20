# WorldFavoriteList

A world favorite group summarised for a public profile, with a sample of its worlds' thumbnails.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**thumbnails** | **List[str]** |  | 

## Example

```python
from vrchatapi.models.world_favorite_list import WorldFavoriteList

# TODO update the JSON string below
json = "{}"
# create an instance of WorldFavoriteList from a JSON string
world_favorite_list_instance = WorldFavoriteList.from_json(json)
# print the JSON string representation of the object
print(WorldFavoriteList.to_json())

# convert the object into a dict
world_favorite_list_dict = world_favorite_list_instance.to_dict()
# create an instance of WorldFavoriteList from a dict
world_favorite_list_from_dict = WorldFavoriteList.from_dict(world_favorite_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


