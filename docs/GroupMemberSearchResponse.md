# GroupMemberSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[GroupMember]**](GroupMember.md) |  | [optional] 
**total** | **int** | Number of members returned | [optional] 

## Example

```python
from vrchatapi.models.group_member_search_response import GroupMemberSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GroupMemberSearchResponse from a JSON string
group_member_search_response_instance = GroupMemberSearchResponse.from_json(json)
# print the JSON string representation of the object
print(GroupMemberSearchResponse.to_json())

# convert the object into a dict
group_member_search_response_dict = group_member_search_response_instance.to_dict()
# create an instance of GroupMemberSearchResponse from a dict
group_member_search_response_from_dict = GroupMemberSearchResponse.from_dict(group_member_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


