# RequestInviteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_slot** | **int** |  | [optional] 

## Example

```python
from vrchatapi.models.request_invite_request import RequestInviteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RequestInviteRequest from a JSON string
request_invite_request_instance = RequestInviteRequest.from_json(json)
# print the JSON string representation of the object
print(RequestInviteRequest.to_json())

# convert the object into a dict
request_invite_request_dict = request_invite_request_instance.to_dict()
# create an instance of RequestInviteRequest from a dict
request_invite_request_from_dict = RequestInviteRequest.from_dict(request_invite_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


