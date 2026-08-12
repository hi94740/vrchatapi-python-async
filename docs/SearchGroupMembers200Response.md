# SearchGroupMembers200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[GroupMember]**](GroupMember.md) |  | [optional] 
**total** | **int** | Number of members returned | [optional] 

## Example

```python
from vrchatapi.models.search_group_members200_response import SearchGroupMembers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SearchGroupMembers200Response from a JSON string
search_group_members200_response_instance = SearchGroupMembers200Response.from_json(json)
# print the JSON string representation of the object
print(SearchGroupMembers200Response.to_json())

# convert the object into a dict
search_group_members200_response_dict = search_group_members200_response_instance.to_dict()
# create an instance of SearchGroupMembers200Response from a dict
search_group_members200_response_from_dict = SearchGroupMembers200Response.from_dict(search_group_members200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


