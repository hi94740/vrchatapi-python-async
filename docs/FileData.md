# FileData



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [default to 'queued']
**file_name** | **str** |  | 
**md5** | **str** |  | [optional] 
**size_in_bytes** | **int** |  | 
**status** | [**FileStatus**](FileStatus.md) |  | [default to FileStatus.WAITING]
**upload_id** | **str** |  | [default to '']
**url** | **str** |  | 

## Example

```python
from vrchatapi.models.file_data import FileData

# TODO update the JSON string below
json = "{}"
# create an instance of FileData from a JSON string
file_data_instance = FileData.from_json(json)
# print the JSON string representation of the object
print(FileData.to_json())

# convert the object into a dict
file_data_dict = file_data_instance.to_dict()
# create an instance of FileData from a dict
file_data_from_dict = FileData.from_dict(file_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


