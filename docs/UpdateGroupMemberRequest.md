# UpdateGroupMemberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_subscribed_to_announcements** | **bool** |  | [optional] 
**is_subscribed_to_event_announcements** | **bool** |  | [optional] 
**manager_notes** | **str** |  | [optional] 
**visibility** | [**GroupUserVisibility**](GroupUserVisibility.md) |  | [optional] 

## Example

```python
from vrchatapi.models.update_group_member_request import UpdateGroupMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGroupMemberRequest from a JSON string
update_group_member_request_instance = UpdateGroupMemberRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateGroupMemberRequest.to_json())

# convert the object into a dict
update_group_member_request_dict = update_group_member_request_instance.to_dict()
# create an instance of UpdateGroupMemberRequest from a dict
update_group_member_request_from_dict = UpdateGroupMemberRequest.from_dict(update_group_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


