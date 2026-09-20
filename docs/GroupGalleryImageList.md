# GroupGalleryImageList

A page of a group gallery's images.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[GroupGalleryImage]**](GroupGalleryImage.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from vrchatapi.models.group_gallery_image_list import GroupGalleryImageList

# TODO update the JSON string below
json = "{}"
# create an instance of GroupGalleryImageList from a JSON string
group_gallery_image_list_instance = GroupGalleryImageList.from_json(json)
# print the JSON string representation of the object
print(GroupGalleryImageList.to_json())

# convert the object into a dict
group_gallery_image_list_dict = group_gallery_image_list_instance.to_dict()
# create an instance of GroupGalleryImageList from a dict
group_gallery_image_list_from_dict = GroupGalleryImageList.from_dict(group_gallery_image_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


