# CreateGroupGalleryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the gallery. | [optional] 
**members_only** | **bool** | Whether the gallery is members only. | [optional] [default to False]
**name** | **str** | Name of the gallery. | 
**role_ids_to_auto_approve** | **List[str]** |   | [optional] 
**role_ids_to_manage** | **List[str]** |   | [optional] 
**role_ids_to_submit** | **List[str]** |   | [optional] 
**role_ids_to_view** | **List[str]** |   | [optional] 

## Example

```python
from vrchatapi.models.create_group_gallery_request import CreateGroupGalleryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGroupGalleryRequest from a JSON string
create_group_gallery_request_instance = CreateGroupGalleryRequest.from_json(json)
# print the JSON string representation of the object
print(CreateGroupGalleryRequest.to_json())

# convert the object into a dict
create_group_gallery_request_dict = create_group_gallery_request_instance.to_dict()
# create an instance of CreateGroupGalleryRequest from a dict
create_group_gallery_request_from_dict = CreateGroupGalleryRequest.from_dict(create_group_gallery_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


