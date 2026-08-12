# InfoPushDataClickable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | **List[str]** | In case of OpenURL, this would contain the link. | [optional] 
**command** | **str** |  | 

## Example

```python
from vrchatapi.models.info_push_data_clickable import InfoPushDataClickable

# TODO update the JSON string below
json = "{}"
# create an instance of InfoPushDataClickable from a JSON string
info_push_data_clickable_instance = InfoPushDataClickable.from_json(json)
# print the JSON string representation of the object
print(InfoPushDataClickable.to_json())

# convert the object into a dict
info_push_data_clickable_dict = info_push_data_clickable_instance.to_dict()
# create an instance of InfoPushDataClickable from a dict
info_push_data_clickable_from_dict = InfoPushDataClickable.from_dict(info_push_data_clickable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


