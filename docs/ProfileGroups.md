# ProfileGroups


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**list** | [**List[ProfileGroup]**](ProfileGroup.md) |  | [optional] 

## Example

```python
from vrchatapi.models.profile_groups import ProfileGroups

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileGroups from a JSON string
profile_groups_instance = ProfileGroups.from_json(json)
# print the JSON string representation of the object
print(ProfileGroups.to_json())

# convert the object into a dict
profile_groups_dict = profile_groups_instance.to_dict()
# create an instance of ProfileGroups from a dict
profile_groups_from_dict = ProfileGroups.from_dict(profile_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


