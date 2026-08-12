# RewardBadge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**created_by** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**description** | **str** |  | 
**file_name** | **str** |  | 
**hidden** | **bool** |  | 
**id** | **str** |  | 
**image_url** | **str** |  | 
**is_localization_enabled** | **bool** |  | 
**machine_name** | **str** |  | [optional] 
**name** | **str** |  | 
**type** | **str** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from vrchatapi.models.reward_badge import RewardBadge

# TODO update the JSON string below
json = "{}"
# create an instance of RewardBadge from a JSON string
reward_badge_instance = RewardBadge.from_json(json)
# print the JSON string representation of the object
print(RewardBadge.to_json())

# convert the object into a dict
reward_badge_dict = reward_badge_instance.to_dict()
# create an instance of RewardBadge from a dict
reward_badge_from_dict = RewardBadge.from_dict(reward_badge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


