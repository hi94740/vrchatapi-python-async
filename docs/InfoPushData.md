# InfoPushData



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**article** | [**InfoPushDataArticle**](InfoPushDataArticle.md) |  | [optional] 
**author_name** | **str** |  | [optional] 
**avatar_id** | **str** |  | [optional] 
**banner_image_url** | **str** |  | [optional] 
**categories** | [**List[InfoPushDataCategory]**](InfoPushDataCategory.md) |  | [optional] 
**category** | **str** |  | [optional] 
**content_list** | [**DynamicContentRow**](DynamicContentRow.md) |  | [optional] 
**description** | **str** |  | [optional] 
**disclaimer_text** | **str** |  | [optional] 
**domain_list** | [**List[InfoPushDataDomainListInner]**](InfoPushDataDomainListInner.md) |  | [optional] 
**featured_avatar_category_id** | **str** |  | [optional] 
**final_name** | **str** |  | [optional] 
**hover_to_join** | **bool** |  | [optional] 
**icon_image_url** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**ips_query** | [**InfoPushIpsQuery**](InfoPushIpsQuery.md) |  | [optional] 
**is_new** | **bool** |  | [optional] 
**listing_ids** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**on_pressed** | [**InfoPushDataClickable**](InfoPushDataClickable.md) |  | [optional] 
**override_name** | **object** |  | [optional] 
**rows** | **int** | Number of rows to render. | [optional] 
**search** | [**InfoPushDataSearch**](InfoPushDataSearch.md) |  | [optional] 
**short_name** | **str** |  | [optional] 
**template** | **str** |  | [optional] 
**thumbnail_image_url** | **str** |  | [optional] 
**tooltip_description** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**weight** | **int** |  | [optional] 
**world_tag** | **str** |  | [optional] 

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


