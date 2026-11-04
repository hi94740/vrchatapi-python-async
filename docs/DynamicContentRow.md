# DynamicContentRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**any_style** | **List[str]** |  | [optional] 
**any_tag** | **List[str]** |  | [optional] 
**avatar_specific** | **bool** |  | [optional] 
**banners_tag** | **str** |  | [optional] 
**categories** | **List[str]** |  | [optional] 
**featured_results** | **str** |  | [optional] 
**group_pool** | **str** |  | [optional] 
**index** | **int** |  | [optional] 
**marketplace** | **str** |  | [optional] 
**max_price** | **int** |  | [optional] 
**min_occupants** | **int** |  | [optional] 
**min_price** | **int** |  | [optional] 
**minimum_interest_count** | **int** |  | [optional] 
**minimum_remaining_minutes** | **int** |  | [optional] 
**mode** | **str** |  | [optional] 
**n** | **int** |  | [optional] 
**name** | **object** |  | 
**non_featured_results** | **str** |  | [optional] 
**notag** | **List[str]** |  | [optional] 
**params** | **Dict[str, object]** |  | [optional] 
**personalized_results** | **str** |  | [optional] 
**platform** | **str** | Usually \&quot;ThisPlatformSupported\&quot;, but can also be other values such as \&quot;all\&quot; or platform specific identifiers. | 
**region** | **str** |  | [optional] 
**scope** | **str** |  | [optional] 
**short_name** | **object** |  | [optional] 
**sort_heading** | **str** |  | [optional] 
**sort_order** | **str** |  | [optional] 
**sort_ownership** | **str** |  | [optional] 
**style** | **str** |  | [optional] 
**tag** | **str** | Tag to filter content for this row. Not a &#x60;Tag&#x60;: that type forbids the empty string, which this field uses for a row that is not tag-filtered. | [optional] 
**tags** | **List[str]** |  | [optional] 
**type** | **str** | Type is not present if it is a world. | [optional] 
**upcoming_offset_minutes** | **int** |  | [optional] 
**world_pool** | **str** |  | [optional] 

## Example

```python
from vrchatapi.models.dynamic_content_row import DynamicContentRow

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicContentRow from a JSON string
dynamic_content_row_instance = DynamicContentRow.from_json(json)
# print the JSON string representation of the object
print(DynamicContentRow.to_json())

# convert the object into a dict
dynamic_content_row_dict = dynamic_content_row_instance.to_dict()
# create an instance of DynamicContentRow from a dict
dynamic_content_row_from_dict = DynamicContentRow.from_dict(dynamic_content_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


