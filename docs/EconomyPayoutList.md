# EconomyPayoutList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payouts** | [**List[EconomyPayout]**](EconomyPayout.md) |  | 

## Example

```python
from vrchatapi.models.economy_payout_list import EconomyPayoutList

# TODO update the JSON string below
json = "{}"
# create an instance of EconomyPayoutList from a JSON string
economy_payout_list_instance = EconomyPayoutList.from_json(json)
# print the JSON string representation of the object
print(EconomyPayoutList.to_json())

# convert the object into a dict
economy_payout_list_dict = economy_payout_list_instance.to_dict()
# create an instance of EconomyPayoutList from a dict
economy_payout_list_from_dict = EconomyPayoutList.from_dict(economy_payout_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


