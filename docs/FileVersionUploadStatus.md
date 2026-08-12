# FileVersionUploadStatus



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**etags** | **List[object]** | Unknown | 
**file_name** | **str** |  | 
**max_parts** | **int** |  | 
**next_part_number** | **int** |  | 
**parts** | **List[object]** |  | 
**upload_id** | **str** |  | 

## Example

```python
from vrchatapi.models.file_version_upload_status import FileVersionUploadStatus

# TODO update the JSON string below
json = "{}"
# create an instance of FileVersionUploadStatus from a JSON string
file_version_upload_status_instance = FileVersionUploadStatus.from_json(json)
# print the JSON string representation of the object
print(FileVersionUploadStatus.to_json())

# convert the object into a dict
file_version_upload_status_dict = file_version_upload_status_instance.to_dict()
# create an instance of FileVersionUploadStatus from a dict
file_version_upload_status_from_dict = FileVersionUploadStatus.from_dict(file_version_upload_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


