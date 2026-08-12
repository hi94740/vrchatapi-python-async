# UpdateGroupGalleryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the gallery. | [optional] 
**members_only** | **bool** | Whether the gallery is members only. | [optional] [default to False]
**name** | **str** | Name of the gallery. | [optional] 
**role_ids_to_auto_approve** | **List[str]** |   | [optional] 
**role_ids_to_manage** | **List[str]** |   | [optional] 
**role_ids_to_submit** | **List[str]** |   | [optional] 
**role_ids_to_view** | **List[str]** |   | [optional] 

## Example

```python
from vrchatapi.models.update_group_gallery_request import UpdateGroupGalleryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGroupGalleryRequest from a JSON string
update_group_gallery_request_instance = UpdateGroupGalleryRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateGroupGalleryRequest.to_json())

# convert the object into a dict
update_group_gallery_request_dict = update_group_gallery_request_instance.to_dict()
# create an instance of UpdateGroupGalleryRequest from a dict
update_group_gallery_request_from_dict = UpdateGroupGalleryRequest.from_dict(update_group_gallery_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


