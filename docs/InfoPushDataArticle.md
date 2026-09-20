# InfoPushDataArticle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**List[InfoPushDataArticleContent]**](InfoPushDataArticleContent.md) |  | [optional] 
**embedded_link_data** | [**List[InfoPushEmbeddedLink]**](InfoPushEmbeddedLink.md) |  | [optional] 
**jump_links** | **List[str]** |  | [optional] 
**more_info_links** | [**List[InfoPushEmbeddedLink]**](InfoPushEmbeddedLink.md) |  | [optional] 
**section_links** | **List[str]** |  | [optional] 

## Example

```python
from vrchatapi.models.info_push_data_article import InfoPushDataArticle

# TODO update the JSON string below
json = "{}"
# create an instance of InfoPushDataArticle from a JSON string
info_push_data_article_instance = InfoPushDataArticle.from_json(json)
# print the JSON string representation of the object
print(InfoPushDataArticle.to_json())

# convert the object into a dict
info_push_data_article_dict = info_push_data_article_instance.to_dict()
# create an instance of InfoPushDataArticle from a dict
info_push_data_article_from_dict = InfoPushDataArticle.from_dict(info_push_data_article_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


