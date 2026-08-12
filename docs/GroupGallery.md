# GroupGallery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**description** | **str** | Description of the gallery. | [optional] 
**id** | **str** |  | [optional] 
**members_only** | **bool** | Whether the gallery is members only. | [optional] [default to False]
**name** | **str** | Name of the gallery. | [optional] 
**role_ids_to_auto_approve** | **List[str]** |   | [optional] 
**role_ids_to_manage** | **List[str]** |   | [optional] 
**role_ids_to_submit** | **List[str]** |   | [optional] 
**role_ids_to_view** | **List[str]** |   | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from vrchatapi.models.group_gallery import GroupGallery

# TODO update the JSON string below
json = "{}"
# create an instance of GroupGallery from a JSON string
group_gallery_instance = GroupGallery.from_json(json)
# print the JSON string representation of the object
print(GroupGallery.to_json())

# convert the object into a dict
group_gallery_dict = group_gallery_instance.to_dict()
# create an instance of GroupGallery from a dict
group_gallery_from_dict = GroupGallery.from_dict(group_gallery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


