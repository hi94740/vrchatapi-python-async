# ChangeUserTagsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | **List[str]** | The tags being added or removed. | 

## Example

```python
from vrchatapi.models.change_user_tags_request import ChangeUserTagsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeUserTagsRequest from a JSON string
change_user_tags_request_instance = ChangeUserTagsRequest.from_json(json)
# print the JSON string representation of the object
print(ChangeUserTagsRequest.to_json())

# convert the object into a dict
change_user_tags_request_dict = change_user_tags_request_instance.to_dict()
# create an instance of ChangeUserTagsRequest from a dict
change_user_tags_request_from_dict = ChangeUserTagsRequest.from_dict(change_user_tags_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


