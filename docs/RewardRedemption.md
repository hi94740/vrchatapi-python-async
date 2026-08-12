# RewardRedemption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**RewardRedemptionData**](RewardRedemptionData.md) |  | 
**type** | **str** | One of &#x60;badge&#x60;, &#x60;item&#x60;, ... | 

## Example

```python
from vrchatapi.models.reward_redemption import RewardRedemption

# TODO update the JSON string below
json = "{}"
# create an instance of RewardRedemption from a JSON string
reward_redemption_instance = RewardRedemption.from_json(json)
# print the JSON string representation of the object
print(RewardRedemption.to_json())

# convert the object into a dict
reward_redemption_dict = reward_redemption_instance.to_dict()
# create an instance of RewardRedemption from a dict
reward_redemption_from_dict = RewardRedemption.from_dict(reward_redemption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


