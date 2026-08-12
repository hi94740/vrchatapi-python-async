# InfoPushDataArticle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | [**InfoPushDataArticleContent**](InfoPushDataArticleContent.md) |  | [optional] 

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


