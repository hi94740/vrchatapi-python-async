# AvatarStyle



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**style_name** | **str** |  | 

## Example

```python
from vrchatapi.models.avatar_style import AvatarStyle

# TODO update the JSON string below
json = "{}"
# create an instance of AvatarStyle from a JSON string
avatar_style_instance = AvatarStyle.from_json(json)
# print the JSON string representation of the object
print(AvatarStyle.to_json())

# convert the object into a dict
avatar_style_dict = avatar_style_instance.to_dict()
# create an instance of AvatarStyle from a dict
avatar_style_from_dict = AvatarStyle.from_dict(avatar_style_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


