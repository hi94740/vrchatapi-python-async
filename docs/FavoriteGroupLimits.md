# FavoriteGroupLimits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar** | **int** |  | 
**friend** | **int** |  | 
**vrc_plus_world** | **int** |  | 
**world** | **int** |  | 

## Example

```python
from vrchatapi.models.favorite_group_limits import FavoriteGroupLimits

# TODO update the JSON string below
json = "{}"
# create an instance of FavoriteGroupLimits from a JSON string
favorite_group_limits_instance = FavoriteGroupLimits.from_json(json)
# print the JSON string representation of the object
print(FavoriteGroupLimits.to_json())

# convert the object into a dict
favorite_group_limits_dict = favorite_group_limits_instance.to_dict()
# create an instance of FavoriteGroupLimits from a dict
favorite_group_limits_from_dict = FavoriteGroupLimits.from_dict(favorite_group_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


