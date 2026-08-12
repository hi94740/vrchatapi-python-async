# InfoPushData



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**article** | [**InfoPushDataArticle**](InfoPushDataArticle.md) |  | [optional] 
**content_list** | [**DynamicContentRow**](DynamicContentRow.md) |  | [optional] 
**description** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**on_pressed** | [**InfoPushDataClickable**](InfoPushDataClickable.md) |  | [optional] 
**template** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vrchatapi.models.info_push_data import InfoPushData

# TODO update the JSON string below
json = "{}"
# create an instance of InfoPushData from a JSON string
info_push_data_instance = InfoPushData.from_json(json)
# print the JSON string representation of the object
print(InfoPushData.to_json())

# convert the object into a dict
info_push_data_dict = info_push_data_instance.to_dict()
# create an instance of InfoPushData from a dict
info_push_data_from_dict = InfoPushData.from_dict(info_push_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


