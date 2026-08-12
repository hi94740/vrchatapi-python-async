# CreateGroupInviteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirm_override_block** | **bool** |  | [optional] [default to True]
**user_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 

## Example

```python
from vrchatapi.models.create_group_invite_request import CreateGroupInviteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGroupInviteRequest from a JSON string
create_group_invite_request_instance = CreateGroupInviteRequest.from_json(json)
# print the JSON string representation of the object
print(CreateGroupInviteRequest.to_json())

# convert the object into a dict
create_group_invite_request_dict = create_group_invite_request_instance.to_dict()
# create an instance of CreateGroupInviteRequest from a dict
create_group_invite_request_from_dict = CreateGroupInviteRequest.from_dict(create_group_invite_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


