# FileVersion



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**deleted** | **bool** | Usually only present if &#x60;true&#x60; | [optional] [default to True]
**delta** | [**FileData**](FileData.md) |  | [optional] 
**file** | [**FileData**](FileData.md) |  | [optional] 
**signature** | [**FileData**](FileData.md) |  | [optional] 
**status** | [**FileStatus**](FileStatus.md) |  | [default to FileStatus.WAITING]
**version** | **int** | Incremental version counter, can only be increased. | [default to 0]

## Example

```python
from vrchatapi.models.file_version import FileVersion

# TODO update the JSON string below
json = "{}"
# create an instance of FileVersion from a JSON string
file_version_instance = FileVersion.from_json(json)
# print the JSON string representation of the object
print(FileVersion.to_json())

# convert the object into a dict
file_version_dict = file_version_instance.to_dict()
# create an instance of FileVersion from a dict
file_version_from_dict = FileVersion.from_dict(file_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


