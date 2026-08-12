# ProfileRepresentedGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**banner_url** | **str** |  | [optional] 
**icon_url** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from vrchatapi.models.profile_represented_group import ProfileRepresentedGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileRepresentedGroup from a JSON string
profile_represented_group_instance = ProfileRepresentedGroup.from_json(json)
# print the JSON string representation of the object
print(ProfileRepresentedGroup.to_json())

# convert the object into a dict
profile_represented_group_dict = profile_represented_group_instance.to_dict()
# create an instance of ProfileRepresentedGroup from a dict
profile_represented_group_from_dict = ProfileRepresentedGroup.from_dict(profile_represented_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


