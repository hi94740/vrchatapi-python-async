# NotificationDetailVoteToKick


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initiator_user_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**user_to_kick_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 

## Example

```python
from vrchatapi.models.notification_detail_vote_to_kick import NotificationDetailVoteToKick

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationDetailVoteToKick from a JSON string
notification_detail_vote_to_kick_instance = NotificationDetailVoteToKick.from_json(json)
# print the JSON string representation of the object
print(NotificationDetailVoteToKick.to_json())

# convert the object into a dict
notification_detail_vote_to_kick_dict = notification_detail_vote_to_kick_instance.to_dict()
# create an instance of NotificationDetailVoteToKick from a dict
notification_detail_vote_to_kick_from_dict = NotificationDetailVoteToKick.from_dict(notification_detail_vote_to_kick_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


