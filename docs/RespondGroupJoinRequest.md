# RespondGroupJoinRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**GroupJoinRequestAction**](GroupJoinRequestAction.md) |  | 
**block** | **bool** | Whether to block the user from requesting again | [optional] 

## Example

```python
from vrchatapi.models.respond_group_join_request import RespondGroupJoinRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RespondGroupJoinRequest from a JSON string
respond_group_join_request_instance = RespondGroupJoinRequest.from_json(json)
# print the JSON string representation of the object
print(RespondGroupJoinRequest.to_json())

# convert the object into a dict
respond_group_join_request_dict = respond_group_join_request_instance.to_dict()
# create an instance of RespondGroupJoinRequest from a dict
respond_group_join_request_from_dict = RespondGroupJoinRequest.from_dict(respond_group_join_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


