# AvatarStyles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary** | **str** |  | [optional] 
**secondary** | **str** |  | [optional] 
**supplementary** | **List[str]** |  | [optional] 

## Example

```python
from vrchatapi.models.avatar_styles import AvatarStyles

# TODO update the JSON string below
json = "{}"
# create an instance of AvatarStyles from a JSON string
avatar_styles_instance = AvatarStyles.from_json(json)
# print the JSON string representation of the object
print(AvatarStyles.to_json())

# convert the object into a dict
avatar_styles_dict = avatar_styles_instance.to_dict()
# create an instance of AvatarStyles from a dict
avatar_styles_from_dict = AvatarStyles.from_dict(avatar_styles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


