# BanGroupMemberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 

## Example

```python
from vrchatapi.models.ban_group_member_request import BanGroupMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BanGroupMemberRequest from a JSON string
ban_group_member_request_instance = BanGroupMemberRequest.from_json(json)
# print the JSON string representation of the object
print(BanGroupMemberRequest.to_json())

# convert the object into a dict
ban_group_member_request_dict = ban_group_member_request_instance.to_dict()
# create an instance of BanGroupMemberRequest from a dict
ban_group_member_request_from_dict = BanGroupMemberRequest.from_dict(ban_group_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


