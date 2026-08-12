# GetUserGroupInstances200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fetched_at** | **datetime** |  | [optional] 
**instances** | [**List[Instance]**](Instance.md) |  | [optional] 

## Example

```python
from vrchatapi.models.get_user_group_instances200_response import GetUserGroupInstances200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserGroupInstances200Response from a JSON string
get_user_group_instances200_response_instance = GetUserGroupInstances200Response.from_json(json)
# print the JSON string representation of the object
print(GetUserGroupInstances200Response.to_json())

# convert the object into a dict
get_user_group_instances200_response_dict = get_user_group_instances200_response_instance.to_dict()
# create an instance of GetUserGroupInstances200Response from a dict
get_user_group_instances200_response_from_dict = GetUserGroupInstances200Response.from_dict(get_user_group_instances200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


