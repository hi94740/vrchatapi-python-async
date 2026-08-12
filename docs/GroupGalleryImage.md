# GroupGalleryImage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approved** | **bool** |  | [optional] [default to False]
**approved_at** | **datetime** |  | [optional] 
**approved_by_user_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 
**created_at** | **datetime** |  | [optional] 
**file_id** | **str** |  | [optional] 
**gallery_id** | **str** |  | [optional] 
**group_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**submitted_by_user_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 

## Example

```python
from vrchatapi.models.group_gallery_image import GroupGalleryImage

# TODO update the JSON string below
json = "{}"
# create an instance of GroupGalleryImage from a JSON string
group_gallery_image_instance = GroupGalleryImage.from_json(json)
# print the JSON string representation of the object
print(GroupGalleryImage.to_json())

# convert the object into a dict
group_gallery_image_dict = group_gallery_image_instance.to_dict()
# create an instance of GroupGalleryImage from a dict
group_gallery_image_from_dict = GroupGalleryImage.from_dict(group_gallery_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


