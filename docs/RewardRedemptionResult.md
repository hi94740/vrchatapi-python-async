# RewardRedemptionResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redeemed_rewards** | [**List[RewardRedemption]**](RewardRedemption.md) |  | 
**redemption_code** | **str** |  | 

## Example

```python
from vrchatapi.models.reward_redemption_result import RewardRedemptionResult

# TODO update the JSON string below
json = "{}"
# create an instance of RewardRedemptionResult from a JSON string
reward_redemption_result_instance = RewardRedemptionResult.from_json(json)
# print the JSON string representation of the object
print(RewardRedemptionResult.to_json())

# convert the object into a dict
reward_redemption_result_dict = reward_redemption_result_instance.to_dict()
# create an instance of RewardRedemptionResult from a dict
reward_redemption_result_from_dict = RewardRedemptionResult.from_dict(reward_redemption_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


