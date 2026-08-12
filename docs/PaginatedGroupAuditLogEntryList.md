# PaginatedGroupAuditLogEntryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_next** | **bool** | Whether there are more results after this page. | [optional] 
**results** | [**List[GroupAuditLogEntry]**](GroupAuditLogEntry.md) |   | [optional] 
**total_count** | **int** | The total number of results that the query would return if there were no pagination. | [optional] 

## Example

```python
from vrchatapi.models.paginated_group_audit_log_entry_list import PaginatedGroupAuditLogEntryList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGroupAuditLogEntryList from a JSON string
paginated_group_audit_log_entry_list_instance = PaginatedGroupAuditLogEntryList.from_json(json)
# print the JSON string representation of the object
print(PaginatedGroupAuditLogEntryList.to_json())

# convert the object into a dict
paginated_group_audit_log_entry_list_dict = paginated_group_audit_log_entry_list_instance.to_dict()
# create an instance of PaginatedGroupAuditLogEntryList from a dict
paginated_group_audit_log_entry_list_from_dict = PaginatedGroupAuditLogEntryList.from_dict(paginated_group_audit_log_entry_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


