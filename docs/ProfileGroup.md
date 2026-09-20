# ProfileGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**icon_url** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from vrchatapi.models.profile_group import ProfileGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileGroup from a JSON string
profile_group_instance = ProfileGroup.from_json(json)
# print the JSON string representation of the object
print(ProfileGroup.to_json())

# convert the object into a dict
profile_group_dict = profile_group_instance.to_dict()
# create an instance of ProfileGroup from a dict
profile_group_from_dict = ProfileGroup.from_dict(profile_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


