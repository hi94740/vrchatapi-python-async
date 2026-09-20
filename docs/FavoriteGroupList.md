# FavoriteGroupList

A user's favorite groups of one type, with the limits that apply to them.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**favorite_groups** | [**List[FavoriteGroupSummary]**](FavoriteGroupSummary.md) |  | 
**max_favorite_groups** | **int** | Only returned when the owner is the currently authenticated user. | [optional] 
**max_favorites_per_group** | **int** | Only returned when the owner is the currently authenticated user. | [optional] 

## Example

```python
from vrchatapi.models.favorite_group_list import FavoriteGroupList

# TODO update the JSON string below
json = "{}"
# create an instance of FavoriteGroupList from a JSON string
favorite_group_list_instance = FavoriteGroupList.from_json(json)
# print the JSON string representation of the object
print(FavoriteGroupList.to_json())

# convert the object into a dict
favorite_group_list_dict = favorite_group_list_instance.to_dict()
# create an instance of FavoriteGroupList from a dict
favorite_group_list_from_dict = FavoriteGroupList.from_dict(favorite_group_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


