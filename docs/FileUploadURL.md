# FileUploadURL



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 

## Example

```python
from vrchatapi.models.file_upload_url import FileUploadURL

# TODO update the JSON string below
json = "{}"
# create an instance of FileUploadURL from a JSON string
file_upload_url_instance = FileUploadURL.from_json(json)
# print the JSON string representation of the object
print(FileUploadURL.to_json())

# convert the object into a dict
file_upload_url_dict = file_upload_url_instance.to_dict()
# create an instance of FileUploadURL from a dict
file_upload_url_from_dict = FileUploadURL.from_dict(file_upload_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


