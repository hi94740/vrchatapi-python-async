# InfoPushDataControl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**control** | **str** |  | 
**display** | **str** |  | 
**id** | **str** |  | 
**kind** | **str** |  | 
**label** | [**LocalizedString**](LocalizedString.md) |  | 
**options** | [**List[InfoPushDataControlOption]**](InfoPushDataControlOption.md) |  | 
**selection** | **str** |  | 

## Example

```python
from vrchatapi.models.info_push_data_control import InfoPushDataControl

# TODO update the JSON string below
json = "{}"
# create an instance of InfoPushDataControl from a JSON string
info_push_data_control_instance = InfoPushDataControl.from_json(json)
# print the JSON string representation of the object
print(InfoPushDataControl.to_json())

# convert the object into a dict
info_push_data_control_dict = info_push_data_control_instance.to_dict()
# create an instance of InfoPushDataControl from a dict
info_push_data_control_from_dict = InfoPushDataControl.from_dict(info_push_data_control_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


