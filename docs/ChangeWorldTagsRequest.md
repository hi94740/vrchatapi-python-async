# ChangeWorldTagsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | **List[str]** | The tags being added or removed. | 

## Example

```python
from vrchatapi.models.change_world_tags_request import ChangeWorldTagsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeWorldTagsRequest from a JSON string
change_world_tags_request_instance = ChangeWorldTagsRequest.from_json(json)
# print the JSON string representation of the object
print(ChangeWorldTagsRequest.to_json())

# convert the object into a dict
change_world_tags_request_dict = change_world_tags_request_instance.to_dict()
# create an instance of ChangeWorldTagsRequest from a dict
change_world_tags_request_from_dict = ChangeWorldTagsRequest.from_dict(change_world_tags_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


