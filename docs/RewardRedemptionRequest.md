# RewardRedemptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 

## Example

```python
from vrchatapi.models.reward_redemption_request import RewardRedemptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RewardRedemptionRequest from a JSON string
reward_redemption_request_instance = RewardRedemptionRequest.from_json(json)
# print the JSON string representation of the object
print(RewardRedemptionRequest.to_json())

# convert the object into a dict
reward_redemption_request_dict = reward_redemption_request_instance.to_dict()
# create an instance of RewardRedemptionRequest from a dict
reward_redemption_request_from_dict = RewardRedemptionRequest.from_dict(reward_redemption_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


