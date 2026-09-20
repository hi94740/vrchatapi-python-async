# InfoPushDataCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** |  | [optional] 
**ips_query** | [**InfoPushIpsQuery**](InfoPushIpsQuery.md) |  | [optional] 
**max_cells** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from vrchatapi.models.info_push_data_category import InfoPushDataCategory

# TODO update the JSON string below
json = "{}"
# create an instance of InfoPushDataCategory from a JSON string
info_push_data_category_instance = InfoPushDataCategory.from_json(json)
# print the JSON string representation of the object
print(InfoPushDataCategory.to_json())

# convert the object into a dict
info_push_data_category_dict = info_push_data_category_instance.to_dict()
# create an instance of InfoPushDataCategory from a dict
info_push_data_category_from_dict = InfoPushDataCategory.from_dict(info_push_data_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


