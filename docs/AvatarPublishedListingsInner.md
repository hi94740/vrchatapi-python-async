# AvatarPublishedListingsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**image_id** | **str** |  | [optional] 
**listing_id** | **str** |  | [optional] 
**listing_type** | **str** |  | [optional] 
**price_tokens** | **int** |  | [optional] 

## Example

```python
from vrchatapi.models.avatar_published_listings_inner import AvatarPublishedListingsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AvatarPublishedListingsInner from a JSON string
avatar_published_listings_inner_instance = AvatarPublishedListingsInner.from_json(json)
# print the JSON string representation of the object
print(AvatarPublishedListingsInner.to_json())

# convert the object into a dict
avatar_published_listings_inner_dict = avatar_published_listings_inner_instance.to_dict()
# create an instance of AvatarPublishedListingsInner from a dict
avatar_published_listings_inner_from_dict = AvatarPublishedListingsInner.from_dict(avatar_published_listings_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


