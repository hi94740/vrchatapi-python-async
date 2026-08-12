# InfoPushDataArticleContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_url** | **str** |  | [optional] 
**on_pressed** | [**InfoPushDataClickable**](InfoPushDataClickable.md) |  | [optional] 
**text** | **str** |  | [optional] 

## Example

```python
from vrchatapi.models.info_push_data_article_content import InfoPushDataArticleContent

# TODO update the JSON string below
json = "{}"
# create an instance of InfoPushDataArticleContent from a JSON string
info_push_data_article_content_instance = InfoPushDataArticleContent.from_json(json)
# print the JSON string representation of the object
print(InfoPushDataArticleContent.to_json())

# convert the object into a dict
info_push_data_article_content_dict = info_push_data_article_content_instance.to_dict()
# create an instance of InfoPushDataArticleContent from a dict
info_push_data_article_content_from_dict = InfoPushDataArticleContent.from_dict(info_push_data_article_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


