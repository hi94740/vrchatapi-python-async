# FavoriteGroupSummary

A favorite group as listed for one favorite type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**num_favorites** | **int** |  | 
**visibility** | [**FavoriteGroupVisibility**](FavoriteGroupVisibility.md) |  | [default to FavoriteGroupVisibility.PRIVATE]

## Example

```python
from vrchatapi.models.favorite_group_summary import FavoriteGroupSummary

# TODO update the JSON string below
json = "{}"
# create an instance of FavoriteGroupSummary from a JSON string
favorite_group_summary_instance = FavoriteGroupSummary.from_json(json)
# print the JSON string representation of the object
print(FavoriteGroupSummary.to_json())

# convert the object into a dict
favorite_group_summary_dict = favorite_group_summary_instance.to_dict()
# create an instance of FavoriteGroupSummary from a dict
favorite_group_summary_from_dict = FavoriteGroupSummary.from_dict(favorite_group_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


