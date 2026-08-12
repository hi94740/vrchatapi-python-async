# Badge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_at** | **datetime** | only present in CurrentUser badges | [optional] 
**badge_description** | **str** |  | 
**badge_id** | **str** |  | 
**badge_image_url** | **str** | direct url to image | 
**badge_name** | **str** |  | 
**hidden** | **bool** | only present in CurrentUser badges | [optional] 
**is_quantifiable** | **bool** |  | [optional] 
**showcased** | **bool** |  | 
**updated_at** | **datetime** | only present in CurrentUser badges | [optional] 

## Example

```python
from vrchatapi.models.badge import Badge

# TODO update the JSON string below
json = "{}"
# create an instance of Badge from a JSON string
badge_instance = Badge.from_json(json)
# print the JSON string representation of the object
print(Badge.to_json())

# convert the object into a dict
badge_dict = badge_instance.to_dict()
# create an instance of Badge from a dict
badge_from_dict = Badge.from_dict(badge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


