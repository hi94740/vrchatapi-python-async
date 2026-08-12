# UpdateFavoriteGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | [optional] 
**tags** | **List[str]** | Tags on FavoriteGroups are believed to do nothing. | [optional] 
**visibility** | [**FavoriteGroupVisibility**](FavoriteGroupVisibility.md) |  | [optional] [default to FavoriteGroupVisibility.PRIVATE]

## Example

```python
from vrchatapi.models.update_favorite_group_request import UpdateFavoriteGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFavoriteGroupRequest from a JSON string
update_favorite_group_request_instance = UpdateFavoriteGroupRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateFavoriteGroupRequest.to_json())

# convert the object into a dict
update_favorite_group_request_dict = update_favorite_group_request_instance.to_dict()
# create an instance of UpdateFavoriteGroupRequest from a dict
update_favorite_group_request_from_dict = UpdateFavoriteGroupRequest.from_dict(update_favorite_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


