# CreateJamSubmissionRequest

Submit content for a Jam. Both content upload by submitter and jam submission itself must be made within the jam's designated times.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_id** | **str** | The id of the uploaded content (e.g., avatar, world) being submitted. | 
**description** | **str** | A description of the content being submitted. | 

## Example

```python
from vrchatapi.models.create_jam_submission_request import CreateJamSubmissionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateJamSubmissionRequest from a JSON string
create_jam_submission_request_instance = CreateJamSubmissionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateJamSubmissionRequest.to_json())

# convert the object into a dict
create_jam_submission_request_dict = create_jam_submission_request_instance.to_dict()
# create an instance of CreateJamSubmissionRequest from a dict
create_jam_submission_request_from_dict = CreateJamSubmissionRequest.from_dict(create_jam_submission_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


