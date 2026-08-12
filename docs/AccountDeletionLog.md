# AccountDeletionLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_time** | **datetime** | Date and time of the deletion request. | [optional] 
**deletion_scheduled** | **datetime** | When the deletion is scheduled to happen, standard is 14 days after the request. | [optional] 
**message** | **str** | Typically \&quot;Deletion requested\&quot; or \&quot;Deletion canceled\&quot;. Other messages like \&quot;Deletion completed\&quot; may exist, but are these are not possible to see as a regular user. | [optional] [default to 'Deletion requested']

## Example

```python
from vrchatapi.models.account_deletion_log import AccountDeletionLog

# TODO update the JSON string below
json = "{}"
# create an instance of AccountDeletionLog from a JSON string
account_deletion_log_instance = AccountDeletionLog.from_json(json)
# print the JSON string representation of the object
print(AccountDeletionLog.to_json())

# convert the object into a dict
account_deletion_log_dict = account_deletion_log_instance.to_dict()
# create an instance of AccountDeletionLog from a dict
account_deletion_log_from_dict = AccountDeletionLog.from_dict(account_deletion_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


