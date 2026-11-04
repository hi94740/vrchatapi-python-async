# InfoPushDataContentSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribution_response_field** | **str** |  | [optional] 
**computed_params** | **Dict[str, str]** |  | 
**endpoint** | **str** |  | 
**kind** | **str** |  | 
**method** | **str** |  | 
**pagination** | [**InfoPushDataContentSourcePagination**](InfoPushDataContentSourcePagination.md) |  | 
**param_modifiability** | **Dict[str, object]** |  | 
**params** | **Dict[str, object]** |  | 
**response_type** | **str** |  | 
**results_field** | **str** |  | 
**schema_version** | **int** |  | 

## Example

```python
from vrchatapi.models.info_push_data_content_source import InfoPushDataContentSource

# TODO update the JSON string below
json = "{}"
# create an instance of InfoPushDataContentSource from a JSON string
info_push_data_content_source_instance = InfoPushDataContentSource.from_json(json)
# print the JSON string representation of the object
print(InfoPushDataContentSource.to_json())

# convert the object into a dict
info_push_data_content_source_dict = info_push_data_content_source_instance.to_dict()
# create an instance of InfoPushDataContentSource from a dict
info_push_data_content_source_from_dict = InfoPushDataContentSource.from_dict(info_push_data_content_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


