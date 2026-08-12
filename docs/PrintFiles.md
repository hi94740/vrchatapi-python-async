# PrintFiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** |  | [optional] 
**image** | **str** | Link to file, e.g. https://api.vrchat.cloud/api/1/file/file_66fe782d-f2bd-4462-9761-1d766d7b2b26/1/file | [optional] 

## Example

```python
from vrchatapi.models.print_files import PrintFiles

# TODO update the JSON string below
json = "{}"
# create an instance of PrintFiles from a JSON string
print_files_instance = PrintFiles.from_json(json)
# print the JSON string representation of the object
print(PrintFiles.to_json())

# convert the object into a dict
print_files_dict = print_files_instance.to_dict()
# create an instance of PrintFiles from a dict
print_files_from_dict = PrintFiles.from_dict(print_files_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


