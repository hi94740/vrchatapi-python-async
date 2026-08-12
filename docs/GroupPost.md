# GroupPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 
**created_at** | **datetime** |  | [optional] 
**editor_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 
**group_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**image_id** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**role_id** | **List[str]** |   | [optional] 
**text** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**visibility** | [**GroupPostVisibility**](GroupPostVisibility.md) |  | [optional] 

## Example

```python
from vrchatapi.models.group_post import GroupPost

# TODO update the JSON string below
json = "{}"
# create an instance of GroupPost from a JSON string
group_post_instance = GroupPost.from_json(json)
# print the JSON string representation of the object
print(GroupPost.to_json())

# convert the object into a dict
group_post_dict = group_post_instance.to_dict()
# create an instance of GroupPost from a dict
group_post_from_dict = GroupPost.from_dict(group_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


