# UserCreditsEligible


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eligible** | **bool** |  | 
**reason** | **str** |  | [optional] 

## Example

```python
from vrchatapi.models.user_credits_eligible import UserCreditsEligible

# TODO update the JSON string below
json = "{}"
# create an instance of UserCreditsEligible from a JSON string
user_credits_eligible_instance = UserCreditsEligible.from_json(json)
# print the JSON string representation of the object
print(UserCreditsEligible.to_json())

# convert the object into a dict
user_credits_eligible_dict = user_credits_eligible_instance.to_dict()
# create an instance of UserCreditsEligible from a dict
user_credits_eligible_from_dict = UserCreditsEligible.from_dict(user_credits_eligible_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


