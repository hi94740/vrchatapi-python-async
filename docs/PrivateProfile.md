# PrivateProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**PrivateProfileActivity**](PrivateProfileActivity.md) |  | [optional] 
**id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 
**is_friend** | **bool** |  | [optional] 
**note** | **str** |  | [optional] 
**status** | [**UserStatus**](UserStatus.md) |  | [optional] [default to UserStatus.OFFLINE]
**status_description** | **str** |  | [optional] 

## Example

```python
from vrchatapi.models.private_profile import PrivateProfile

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateProfile from a JSON string
private_profile_instance = PrivateProfile.from_json(json)
# print the JSON string representation of the object
print(PrivateProfile.to_json())

# convert the object into a dict
private_profile_dict = private_profile_instance.to_dict()
# create an instance of PrivateProfile from a dict
private_profile_from_dict = PrivateProfile.from_dict(private_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


