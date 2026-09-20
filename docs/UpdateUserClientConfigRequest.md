# UpdateUserClientConfigRequest

Only the settings named are changed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_reduce_decor_anim** | **bool** |  | [optional] 

## Example

```python
from vrchatapi.models.update_user_client_config_request import UpdateUserClientConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserClientConfigRequest from a JSON string
update_user_client_config_request_instance = UpdateUserClientConfigRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateUserClientConfigRequest.to_json())

# convert the object into a dict
update_user_client_config_request_dict = update_user_client_config_request_instance.to_dict()
# create an instance of UpdateUserClientConfigRequest from a dict
update_user_client_config_request_from_dict = UpdateUserClientConfigRequest.from_dict(update_user_client_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


