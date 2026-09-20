# FavoriteGroupContents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**favorites** | [**List[FavoriteGroupContentsEntry]**](FavoriteGroupContentsEntry.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from vrchatapi.models.favorite_group_contents import FavoriteGroupContents

# TODO update the JSON string below
json = "{}"
# create an instance of FavoriteGroupContents from a JSON string
favorite_group_contents_instance = FavoriteGroupContents.from_json(json)
# print the JSON string representation of the object
print(FavoriteGroupContents.to_json())

# convert the object into a dict
favorite_group_contents_dict = favorite_group_contents_instance.to_dict()
# create an instance of FavoriteGroupContents from a dict
favorite_group_contents_from_dict = FavoriteGroupContents.from_dict(favorite_group_contents_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


