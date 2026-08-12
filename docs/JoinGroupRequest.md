# JoinGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invite_id** | **str** |  | [optional] 

## Example

```python
from vrchatapi.models.join_group_request import JoinGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of JoinGroupRequest from a JSON string
join_group_request_instance = JoinGroupRequest.from_json(json)
# print the JSON string representation of the object
print(JoinGroupRequest.to_json())

# convert the object into a dict
join_group_request_dict = join_group_request_instance.to_dict()
# create an instance of JoinGroupRequest from a dict
join_group_request_from_dict = JoinGroupRequest.from_dict(join_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


