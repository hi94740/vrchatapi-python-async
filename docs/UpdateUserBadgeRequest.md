# UpdateUserBadgeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hidden** | **bool** |  | [optional] 
**showcased** | **bool** |  | [optional] 

## Example

```python
from vrchatapi.models.update_user_badge_request import UpdateUserBadgeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserBadgeRequest from a JSON string
update_user_badge_request_instance = UpdateUserBadgeRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateUserBadgeRequest.to_json())

# convert the object into a dict
update_user_badge_request_dict = update_user_badge_request_instance.to_dict()
# create an instance of UpdateUserBadgeRequest from a dict
update_user_badge_request_from_dict = UpdateUserBadgeRequest.from_dict(update_user_badge_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


