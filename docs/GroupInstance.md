# GroupInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_id** | **str** | InstanceID can be \&quot;offline\&quot; on User profiles if you are not friends with that user and \&quot;private\&quot; if you are friends and user is in private instance. | 
**location** | **str** | Represents a unique location, consisting of a world identifier and an instance identifier, or \&quot;offline\&quot; if the user is not on your friends list. | 
**member_count** | **int** |  | 
**world** | [**World**](World.md) |  | 

## Example

```python
from vrchatapi.models.group_instance import GroupInstance

# TODO update the JSON string below
json = "{}"
# create an instance of GroupInstance from a JSON string
group_instance_instance = GroupInstance.from_json(json)
# print the JSON string representation of the object
print(GroupInstance.to_json())

# convert the object into a dict
group_instance_dict = group_instance_instance.to_dict()
# create an instance of GroupInstance from a dict
group_instance_from_dict = GroupInstance.from_dict(group_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


