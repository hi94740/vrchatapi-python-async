# UserGroupInstanceListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fetched_at** | **datetime** |  | [optional] 
**instances** | [**List[Instance]**](Instance.md) |  | [optional] 

## Example

```python
from vrchatapi.models.user_group_instance_list_response import UserGroupInstanceListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserGroupInstanceListResponse from a JSON string
user_group_instance_list_response_instance = UserGroupInstanceListResponse.from_json(json)
# print the JSON string representation of the object
print(UserGroupInstanceListResponse.to_json())

# convert the object into a dict
user_group_instance_list_response_dict = user_group_instance_list_response_instance.to_dict()
# create an instance of UserGroupInstanceListResponse from a dict
user_group_instance_list_response_from_dict = UserGroupInstanceListResponse.from_dict(user_group_instance_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


