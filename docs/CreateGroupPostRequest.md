# CreateGroupPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_id** | **str** |  | [optional] 
**role_ids** | **List[str]** |   | [optional] 
**send_notification** | **bool** | Send notification to group members. | [default to False]
**text** | **str** | Post text | 
**title** | **str** | Post title | 
**visibility** | [**GroupPostVisibility**](GroupPostVisibility.md) |  | 

## Example

```python
from vrchatapi.models.create_group_post_request import CreateGroupPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGroupPostRequest from a JSON string
create_group_post_request_instance = CreateGroupPostRequest.from_json(json)
# print the JSON string representation of the object
print(CreateGroupPostRequest.to_json())

# convert the object into a dict
create_group_post_request_dict = create_group_post_request_instance.to_dict()
# create an instance of CreateGroupPostRequest from a dict
create_group_post_request_from_dict = CreateGroupPostRequest.from_dict(create_group_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


