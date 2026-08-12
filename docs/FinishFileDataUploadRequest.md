# FinishFileDataUploadRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**etags** | **List[str]** | Array of ETags uploaded. | [optional] 
**max_parts** | **str** | Always a zero in string form, despite how many parts uploaded. | [default to '0']
**next_part_number** | **str** | Always a zero in string form, despite how many parts uploaded. | [default to '0']

## Example

```python
from vrchatapi.models.finish_file_data_upload_request import FinishFileDataUploadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FinishFileDataUploadRequest from a JSON string
finish_file_data_upload_request_instance = FinishFileDataUploadRequest.from_json(json)
# print the JSON string representation of the object
print(FinishFileDataUploadRequest.to_json())

# convert the object into a dict
finish_file_data_upload_request_dict = finish_file_data_upload_request_instance.to_dict()
# create an instance of FinishFileDataUploadRequest from a dict
finish_file_data_upload_request_from_dict = FinishFileDataUploadRequest.from_dict(finish_file_data_upload_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


