# ProfileTheme


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**button_color** | **str** | Six hexadecimal digits, without a leading &#x60;#&#x60;. May be empty. | 
**icon_color** | **str** | Six hexadecimal digits, without a leading &#x60;#&#x60;. May be empty. | 
**id** | **str** |  | 
**name** | **str** |  | 
**subtext_color** | **str** | Six hexadecimal digits, without a leading &#x60;#&#x60;. May be empty. | 

## Example

```python
from vrchatapi.models.profile_theme import ProfileTheme

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileTheme from a JSON string
profile_theme_instance = ProfileTheme.from_json(json)
# print the JSON string representation of the object
print(ProfileTheme.to_json())

# convert the object into a dict
profile_theme_dict = profile_theme_instance.to_dict()
# create an instance of ProfileTheme from a dict
profile_theme_from_dict = ProfileTheme.from_dict(profile_theme_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


