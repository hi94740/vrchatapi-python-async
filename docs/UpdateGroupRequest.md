# UpdateGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**banner_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**icon_id** | **str** |  | [optional] 
**join_state** | [**GroupJoinState**](GroupJoinState.md) |  | [optional] [default to GroupJoinState.OPEN]
**languages** | **List[str]** | 3 letter language code | [optional] 
**links** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**rules** | **str** |  | [optional] 
**short_code** | **str** |  | [optional] 
**tags** | **List[str]** |   | [optional] 

## Example

```python
from vrchatapi.models.update_group_request import UpdateGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGroupRequest from a JSON string
update_group_request_instance = UpdateGroupRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateGroupRequest.to_json())

# convert the object into a dict
update_group_request_dict = update_group_request_instance.to_dict()
# create an instance of UpdateGroupRequest from a dict
update_group_request_from_dict = UpdateGroupRequest.from_dict(update_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


