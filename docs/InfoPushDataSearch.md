# InfoPushDataSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_content** | **str** |  | [optional] 
**search_in_fields** | **str** |  | [optional] 
**search_query** | **str** |  | [optional] 
**search_tags** | **str** |  | [optional] 
**sort_by** | **str** |  | [optional] 

## Example

```python
from vrchatapi.models.info_push_data_search import InfoPushDataSearch

# TODO update the JSON string below
json = "{}"
# create an instance of InfoPushDataSearch from a JSON string
info_push_data_search_instance = InfoPushDataSearch.from_json(json)
# print the JSON string representation of the object
print(InfoPushDataSearch.to_json())

# convert the object into a dict
info_push_data_search_dict = info_push_data_search_instance.to_dict()
# create an instance of InfoPushDataSearch from a dict
info_push_data_search_from_dict = InfoPushDataSearch.from_dict(info_push_data_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


