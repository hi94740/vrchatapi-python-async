# GroupPostsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**posts** | [**List[GroupPost]**](GroupPost.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from vrchatapi.models.group_posts_response import GroupPostsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GroupPostsResponse from a JSON string
group_posts_response_instance = GroupPostsResponse.from_json(json)
# print the JSON string representation of the object
print(GroupPostsResponse.to_json())

# convert the object into a dict
group_posts_response_dict = group_posts_response_instance.to_dict()
# create an instance of GroupPostsResponse from a dict
group_posts_response_from_dict = GroupPostsResponse.from_dict(group_posts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


