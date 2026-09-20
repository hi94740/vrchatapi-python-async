# InfoPushEmbeddedLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | **List[str]** |  | [optional] 
**command** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from vrchatapi.models.info_push_embedded_link import InfoPushEmbeddedLink

# TODO update the JSON string below
json = "{}"
# create an instance of InfoPushEmbeddedLink from a JSON string
info_push_embedded_link_instance = InfoPushEmbeddedLink.from_json(json)
# print the JSON string representation of the object
print(InfoPushEmbeddedLink.to_json())

# convert the object into a dict
info_push_embedded_link_dict = info_push_embedded_link_instance.to_dict()
# create an instance of InfoPushEmbeddedLink from a dict
info_push_embedded_link_from_dict = InfoPushEmbeddedLink.from_dict(info_push_embedded_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


