# ReportReason

A reason used for reporting users

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | The label or name of the report reason | 
**tooltip** | **str** | A brief explanation of what this reason entails | 

## Example

```python
from vrchatapi.models.report_reason import ReportReason

# TODO update the JSON string below
json = "{}"
# create an instance of ReportReason from a JSON string
report_reason_instance = ReportReason.from_json(json)
# print the JSON string representation of the object
print(ReportReason.to_json())

# convert the object into a dict
report_reason_dict = report_reason_instance.to_dict()
# create an instance of ReportReason from a dict
report_reason_from_dict = ReportReason.from_dict(report_reason_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


