# AddFavoriteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**favorite_id** | **str** | Must be either AvatarID, WorldID or UserID. | 
**tags** | **List[str]** | Tags indicate which group this favorite belongs to. Adding multiple groups makes it show up in all. Removing it from one in that case removes it from all. | 
**type** | [**FavoriteType**](FavoriteType.md) |  | [default to FavoriteType.FRIEND]

## Example

```python
from vrchatapi.models.add_favorite_request import AddFavoriteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddFavoriteRequest from a JSON string
add_favorite_request_instance = AddFavoriteRequest.from_json(json)
# print the JSON string representation of the object
print(AddFavoriteRequest.to_json())

# convert the object into a dict
add_favorite_request_dict = add_favorite_request_instance.to_dict()
# create an instance of AddFavoriteRequest from a dict
add_favorite_request_from_dict = AddFavoriteRequest.from_dict(add_favorite_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


