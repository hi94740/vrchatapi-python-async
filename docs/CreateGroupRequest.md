# CreateGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**banner_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**icon_id** | **str** |  | [optional] 
**join_state** | [**GroupJoinState**](GroupJoinState.md) |  | [optional] [default to GroupJoinState.OPEN]
**name** | **str** |  | 
**privacy** | [**GroupPrivacy**](GroupPrivacy.md) |  | [optional] [default to GroupPrivacy.DEFAULT]
**role_template** | [**GroupRoleTemplate**](GroupRoleTemplate.md) |  | [default to GroupRoleTemplate.DEFAULT]
**short_code** | **str** |  | 

## Example

```python
from vrchatapi.models.create_group_request import CreateGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGroupRequest from a JSON string
create_group_request_instance = CreateGroupRequest.from_json(json)
# print the JSON string representation of the object
print(CreateGroupRequest.to_json())

# convert the object into a dict
create_group_request_dict = create_group_request_instance.to_dict()
# create an instance of CreateGroupRequest from a dict
create_group_request_from_dict = CreateGroupRequest.from_dict(create_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


