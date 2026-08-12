# FavoriteLimits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_max_favorite_groups** | **int** |  | 
**default_max_favorites_per_group** | **int** |  | 
**max_favorite_groups** | [**FavoriteGroupLimits**](FavoriteGroupLimits.md) |  | 
**max_favorites_per_group** | [**FavoriteGroupLimits**](FavoriteGroupLimits.md) |  | 

## Example

```python
from vrchatapi.models.favorite_limits import FavoriteLimits

# TODO update the JSON string below
json = "{}"
# create an instance of FavoriteLimits from a JSON string
favorite_limits_instance = FavoriteLimits.from_json(json)
# print the JSON string representation of the object
print(FavoriteLimits.to_json())

# convert the object into a dict
favorite_limits_dict = favorite_limits_instance.to_dict()
# create an instance of FavoriteLimits from a dict
favorite_limits_from_dict = FavoriteLimits.from_dict(favorite_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


