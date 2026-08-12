# GetGroupPosts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**posts** | [**List[GroupPost]**](GroupPost.md) |  | [optional] 

## Example

```python
from vrchatapi.models.get_group_posts200_response import GetGroupPosts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetGroupPosts200Response from a JSON string
get_group_posts200_response_instance = GetGroupPosts200Response.from_json(json)
# print the JSON string representation of the object
print(GetGroupPosts200Response.to_json())

# convert the object into a dict
get_group_posts200_response_dict = get_group_posts200_response_instance.to_dict()
# create an instance of GetGroupPosts200Response from a dict
get_group_posts200_response_from_dict = GetGroupPosts200Response.from_dict(get_group_posts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


