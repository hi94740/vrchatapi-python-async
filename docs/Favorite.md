# Favorite



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**favorite_id** | **str** | MUST be either AvatarID, UserID or WorldID. | 
**id** | **str** |  | 
**tags** | **List[str]** |   | 
**type** | [**FavoriteType**](FavoriteType.md) |  | [default to FavoriteType.FRIEND]

## Example

```python
from vrchatapi.models.favorite import Favorite

# TODO update the JSON string below
json = "{}"
# create an instance of Favorite from a JSON string
favorite_instance = Favorite.from_json(json)
# print the JSON string representation of the object
print(Favorite.to_json())

# convert the object into a dict
favorite_dict = favorite_instance.to_dict()
# create an instance of Favorite from a dict
favorite_from_dict = Favorite.from_dict(favorite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


