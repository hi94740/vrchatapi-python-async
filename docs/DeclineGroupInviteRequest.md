# DeclineGroupInviteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block** | **bool** |  | [optional] [default to False]

## Example

```python
from vrchatapi.models.decline_group_invite_request import DeclineGroupInviteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeclineGroupInviteRequest from a JSON string
decline_group_invite_request_instance = DeclineGroupInviteRequest.from_json(json)
# print the JSON string representation of the object
print(DeclineGroupInviteRequest.to_json())

# convert the object into a dict
decline_group_invite_request_dict = decline_group_invite_request_instance.to_dict()
# create an instance of DeclineGroupInviteRequest from a dict
decline_group_invite_request_from_dict = DeclineGroupInviteRequest.from_dict(decline_group_invite_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


