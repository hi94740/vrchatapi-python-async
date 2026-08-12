# PaginatedModerationReportList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_next** | **bool** | Whether there are more results after this page. | [optional] 
**results** | [**List[ModerationReport]**](ModerationReport.md) | The list of moderation reports. | [optional] 
**total_count** | **int** | The total number of results that the query would return if there were no pagination. | [optional] 

## Example

```python
from vrchatapi.models.paginated_moderation_report_list import PaginatedModerationReportList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedModerationReportList from a JSON string
paginated_moderation_report_list_instance = PaginatedModerationReportList.from_json(json)
# print the JSON string representation of the object
print(PaginatedModerationReportList.to_json())

# convert the object into a dict
paginated_moderation_report_list_dict = paginated_moderation_report_list_instance.to_dict()
# create an instance of PaginatedModerationReportList from a dict
paginated_moderation_report_list_from_dict = PaginatedModerationReportList.from_dict(paginated_moderation_report_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


