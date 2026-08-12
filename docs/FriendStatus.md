# FriendStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**incoming_request** | **bool** |  | [default to False]
**is_friend** | **bool** |  | [default to False]
**outgoing_request** | **bool** |  | [default to False]

## Example

```python
from vrchatapi.models.friend_status import FriendStatus

# TODO update the JSON string below
json = "{}"
# create an instance of FriendStatus from a JSON string
friend_status_instance = FriendStatus.from_json(json)
# print the JSON string representation of the object
print(FriendStatus.to_json())

# convert the object into a dict
friend_status_dict = friend_status_instance.to_dict()
# create an instance of FriendStatus from a dict
friend_status_from_dict = FriendStatus.from_dict(friend_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


