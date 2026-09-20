# FavoriteGroupContentsEntry

A favorite alongside the object it points at. The object appears under a property named for the favorite's type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar** | [**Avatar**](Avatar.md) |  | [optional] 
**favorite_id** | **str** |  | 
**id** | **str** |  | 
**tags** | **List[str]** |  | 
**type** | [**FavoriteType**](FavoriteType.md) |  | [default to FavoriteType.FRIEND]
**world** | [**FavoriteGroupContentsEntryWorld**](FavoriteGroupContentsEntryWorld.md) |  | [optional] 

## Example

```python
from vrchatapi.models.favorite_group_contents_entry import FavoriteGroupContentsEntry

# TODO update the JSON string below
json = "{}"
# create an instance of FavoriteGroupContentsEntry from a JSON string
favorite_group_contents_entry_instance = FavoriteGroupContentsEntry.from_json(json)
# print the JSON string representation of the object
print(FavoriteGroupContentsEntry.to_json())

# convert the object into a dict
favorite_group_contents_entry_dict = favorite_group_contents_entry_instance.to_dict()
# create an instance of FavoriteGroupContentsEntry from a dict
favorite_group_contents_entry_from_dict = FavoriteGroupContentsEntry.from_dict(favorite_group_contents_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


