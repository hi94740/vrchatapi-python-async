# Balance



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | **int** |  | [default to 0]
**no_transactions** | **bool** |  | [optional] 
**tilia_response** | **bool** |  | [optional] 

## Example

```python
from vrchatapi.models.balance import Balance

# TODO update the JSON string below
json = "{}"
# create an instance of Balance from a JSON string
balance_instance = Balance.from_json(json)
# print the JSON string representation of the object
print(Balance.to_json())

# convert the object into a dict
balance_dict = balance_instance.to_dict()
# create an instance of Balance from a dict
balance_from_dict = Balance.from_dict(balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


