# InfoPushDataPresentation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**layout** | **str** |  | 
**pinned_description** | **str** |  | [optional] 
**social_display** | **str** |  | [optional] 

## Example

```python
from vrchatapi.models.info_push_data_presentation import InfoPushDataPresentation

# TODO update the JSON string below
json = "{}"
# create an instance of InfoPushDataPresentation from a JSON string
info_push_data_presentation_instance = InfoPushDataPresentation.from_json(json)
# print the JSON string representation of the object
print(InfoPushDataPresentation.to_json())

# convert the object into a dict
info_push_data_presentation_dict = info_push_data_presentation_instance.to_dict()
# create an instance of InfoPushDataPresentation from a dict
info_push_data_presentation_from_dict = InfoPushDataPresentation.from_dict(info_push_data_presentation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


