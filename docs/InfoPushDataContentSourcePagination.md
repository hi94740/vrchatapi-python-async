# InfoPushDataContentSourcePagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor_param** | **str** |  | 
**cursor_response_field** | **str** |  | 
**page_size** | **int** |  | 
**page_size_param** | **str** |  | 
**style** | **str** |  | 

## Example

```python
from vrchatapi.models.info_push_data_content_source_pagination import InfoPushDataContentSourcePagination

# TODO update the JSON string below
json = "{}"
# create an instance of InfoPushDataContentSourcePagination from a JSON string
info_push_data_content_source_pagination_instance = InfoPushDataContentSourcePagination.from_json(json)
# print the JSON string representation of the object
print(InfoPushDataContentSourcePagination.to_json())

# convert the object into a dict
info_push_data_content_source_pagination_dict = info_push_data_content_source_pagination_instance.to_dict()
# create an instance of InfoPushDataContentSourcePagination from a dict
info_push_data_content_source_pagination_from_dict = InfoPushDataContentSourcePagination.from_dict(info_push_data_content_source_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


