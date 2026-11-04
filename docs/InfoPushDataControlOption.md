# InfoPushDataControlOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**label** | [**LocalizedString**](LocalizedString.md) |  | 
**params** | **Dict[str, object]** |  | 

## Example

```python
from vrchatapi.models.info_push_data_control_option import InfoPushDataControlOption

# TODO update the JSON string below
json = "{}"
# create an instance of InfoPushDataControlOption from a JSON string
info_push_data_control_option_instance = InfoPushDataControlOption.from_json(json)
# print the JSON string representation of the object
print(InfoPushDataControlOption.to_json())

# convert the object into a dict
info_push_data_control_option_dict = info_push_data_control_option_instance.to_dict()
# create an instance of InfoPushDataControlOption from a dict
info_push_data_control_option_from_dict = InfoPushDataControlOption.from_dict(info_push_data_control_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


