# CreateFileVersionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_md5** | **str** |  | [optional] 
**file_size_in_bytes** | **int** |  | [optional] 
**signature_md5** | **str** |  | 
**signature_size_in_bytes** | **int** |  | 

## Example

```python
from vrchatapi.models.create_file_version_request import CreateFileVersionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFileVersionRequest from a JSON string
create_file_version_request_instance = CreateFileVersionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateFileVersionRequest.to_json())

# convert the object into a dict
create_file_version_request_dict = create_file_version_request_instance.to_dict()
# create an instance of CreateFileVersionRequest from a dict
create_file_version_request_from_dict = CreateFileVersionRequest.from_dict(create_file_version_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


