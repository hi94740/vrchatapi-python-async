# AccountStanding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issue_clear_days** | **int** |  | 
**sanctions** | **List[object]** |  | 
**standing** | **str** |  | 

## Example

```python
from vrchatapi.models.account_standing import AccountStanding

# TODO update the JSON string below
json = "{}"
# create an instance of AccountStanding from a JSON string
account_standing_instance = AccountStanding.from_json(json)
# print the JSON string representation of the object
print(AccountStanding.to_json())

# convert the object into a dict
account_standing_dict = account_standing_instance.to_dict()
# create an instance of AccountStanding from a dict
account_standing_from_dict = AccountStanding.from_dict(account_standing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


