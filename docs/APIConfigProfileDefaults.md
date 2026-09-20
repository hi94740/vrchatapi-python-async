# APIConfigProfileDefaults

Default profile theme colours, each a hex RGB triplet without a leading `#`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**background_gradient_bottom** | **str** | Six hexadecimal digits, without a leading &#x60;#&#x60;. May be empty. | [optional] 
**background_gradient_top** | **str** | Six hexadecimal digits, without a leading &#x60;#&#x60;. May be empty. | [optional] 
**theme_button_color** | **str** | Six hexadecimal digits, without a leading &#x60;#&#x60;. May be empty. | [optional] 
**theme_icon_color** | **str** | Six hexadecimal digits, without a leading &#x60;#&#x60;. May be empty. | [optional] 
**theme_subtext_color** | **str** | Six hexadecimal digits, without a leading &#x60;#&#x60;. May be empty. | [optional] 

## Example

```python
from vrchatapi.models.api_config_profile_defaults import APIConfigProfileDefaults

# TODO update the JSON string below
json = "{}"
# create an instance of APIConfigProfileDefaults from a JSON string
api_config_profile_defaults_instance = APIConfigProfileDefaults.from_json(json)
# print the JSON string representation of the object
print(APIConfigProfileDefaults.to_json())

# convert the object into a dict
api_config_profile_defaults_dict = api_config_profile_defaults_instance.to_dict()
# create an instance of APIConfigProfileDefaults from a dict
api_config_profile_defaults_from_dict = APIConfigProfileDefaults.from_dict(api_config_profile_defaults_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


