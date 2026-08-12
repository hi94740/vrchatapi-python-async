# GroupGalleryFileOrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gallery_id** | **str** |  | 
**ids** | **List[str]** |  | 

## Example

```python
from vrchatapi.models.group_gallery_file_order_request import GroupGalleryFileOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupGalleryFileOrderRequest from a JSON string
group_gallery_file_order_request_instance = GroupGalleryFileOrderRequest.from_json(json)
# print the JSON string representation of the object
print(GroupGalleryFileOrderRequest.to_json())

# convert the object into a dict
group_gallery_file_order_request_dict = group_gallery_file_order_request_instance.to_dict()
# create an instance of GroupGalleryFileOrderRequest from a dict
group_gallery_file_order_request_from_dict = GroupGalleryFileOrderRequest.from_dict(group_gallery_file_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


