# FavoriteGroup



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**owner_display_name** | **str** |  | 
**owner_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**tags** | **List[str]** |   | 
**type** | [**FavoriteType**](FavoriteType.md) |  | [default to FavoriteType.FRIEND]
**visibility** | [**FavoriteGroupVisibility**](FavoriteGroupVisibility.md) |  | [default to FavoriteGroupVisibility.PRIVATE]

## Example

```python
from vrchatapi.models.favorite_group import FavoriteGroup

# TODO update the JSON string below
json = "{}"
# create an instance of FavoriteGroup from a JSON string
favorite_group_instance = FavoriteGroup.from_json(json)
# print the JSON string representation of the object
print(FavoriteGroup.to_json())

# convert the object into a dict
favorite_group_dict = favorite_group_instance.to_dict()
# create an instance of FavoriteGroup from a dict
favorite_group_from_dict = FavoriteGroup.from_dict(favorite_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


