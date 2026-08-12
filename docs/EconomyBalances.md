# EconomyBalances


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance** | **int** |  | 
**earnings** | **int** |  | 
**standard** | **int** |  | 

## Example

```python
from vrchatapi.models.economy_balances import EconomyBalances

# TODO update the JSON string below
json = "{}"
# create an instance of EconomyBalances from a JSON string
economy_balances_instance = EconomyBalances.from_json(json)
# print the JSON string representation of the object
print(EconomyBalances.to_json())

# convert the object into a dict
economy_balances_dict = economy_balances_instance.to_dict()
# create an instance of EconomyBalances from a dict
economy_balances_from_dict = EconomyBalances.from_dict(economy_balances_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


