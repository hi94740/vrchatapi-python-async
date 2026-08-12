# ReportCategory

A category used for reporting content

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the report category | [optional] 
**text** | **str** | The label of the report category | 
**title** | **str** | The title of the report category | [optional] 
**tooltip** | **str** | The tooltip that describes the category | 

## Example

```python
from vrchatapi.models.report_category import ReportCategory

# TODO update the JSON string below
json = "{}"
# create an instance of ReportCategory from a JSON string
report_category_instance = ReportCategory.from_json(json)
# print the JSON string representation of the object
print(ReportCategory.to_json())

# convert the object into a dict
report_category_dict = report_category_instance.to_dict()
# create an instance of ReportCategory from a dict
report_category_from_dict = ReportCategory.from_dict(report_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


