# GetGroupGalleryImages200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[GroupGalleryImage]**](GroupGalleryImage.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from vrchatapi.models.get_group_gallery_images200_response import GetGroupGalleryImages200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetGroupGalleryImages200Response from a JSON string
get_group_gallery_images200_response_instance = GetGroupGalleryImages200Response.from_json(json)
# print the JSON string representation of the object
print(GetGroupGalleryImages200Response.to_json())

# convert the object into a dict
get_group_gallery_images200_response_dict = get_group_gallery_images200_response_instance.to_dict()
# create an instance of GetGroupGalleryImages200Response from a dict
get_group_gallery_images200_response_from_dict = GetGroupGalleryImages200Response.from_dict(get_group_gallery_images200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


