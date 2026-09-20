# UserClientConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_reduce_decor_anim** | **bool** |  | 
**config_string** | **str** |  | 

## Example

```python
from vrchatapi.models.user_client_config import UserClientConfig

# TODO update the JSON string below
json = "{}"
# create an instance of UserClientConfig from a JSON string
user_client_config_instance = UserClientConfig.from_json(json)
# print the JSON string representation of the object
print(UserClientConfig.to_json())

# convert the object into a dict
user_client_config_dict = user_client_config_instance.to_dict()
# create an instance of UserClientConfig from a dict
user_client_config_from_dict = UserClientConfig.from_dict(user_client_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


