# RewardRedemptionData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badge** | [**RewardBadge**](RewardBadge.md) |  | [optional] 
**item** | [**InventoryTemplate**](InventoryTemplate.md) |  | [optional] 

## Example

```python
from vrchatapi.models.reward_redemption_data import RewardRedemptionData

# TODO update the JSON string below
json = "{}"
# create an instance of RewardRedemptionData from a JSON string
reward_redemption_data_instance = RewardRedemptionData.from_json(json)
# print the JSON string representation of the object
print(RewardRedemptionData.to_json())

# convert the object into a dict
reward_redemption_data_dict = reward_redemption_data_instance.to_dict()
# create an instance of RewardRedemptionData from a dict
reward_redemption_data_from_dict = RewardRedemptionData.from_dict(reward_redemption_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


