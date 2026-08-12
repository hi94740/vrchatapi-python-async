# PrivateProfileActivity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_id** | **str** | InstanceID can be \&quot;offline\&quot; on User profiles if you are not friends with that user and \&quot;private\&quot; if you are friends and user is in private instance. | [optional] 
**last_activity** | **str** | Either a date-time or an empty string. | [optional] 
**last_login** | **str** | Either a date-time or an empty string. | [optional] 
**location** | **str** | Represents a unique location, consisting of a world identifier and an instance identifier, or \&quot;offline\&quot; if the user is not on your friends list. | [optional] 
**platform** | **str** | This is normally &#x60;android&#x60;, &#x60;ios&#x60;, &#x60;standalonewindows&#x60;, &#x60;web&#x60;, or the empty value &#x60;&#x60;, but also supposedly can be any random Unity version such as &#x60;2019.2.4-801-Release&#x60; or &#x60;2019.2.2-772-Release&#x60; or even &#x60;unknownplatform&#x60;. | [optional] 
**state** | [**UserState**](UserState.md) |  | [optional] [default to UserState.OFFLINE]
**traveling_to_instance** | **str** |  | [optional] 
**traveling_to_location** | **str** |  | [optional] 
**traveling_to_world** | **str** |  | [optional] 
**world_id** | **str** | WorldID be \&quot;offline\&quot; on User profiles if you are not friends with that user. | [optional] 

## Example

```python
from vrchatapi.models.private_profile_activity import PrivateProfileActivity

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateProfileActivity from a JSON string
private_profile_activity_instance = PrivateProfileActivity.from_json(json)
# print the JSON string representation of the object
print(PrivateProfileActivity.to_json())

# convert the object into a dict
private_profile_activity_dict = private_profile_activity_instance.to_dict()
# create an instance of PrivateProfileActivity from a dict
private_profile_activity_from_dict = PrivateProfileActivity.from_dict(private_profile_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


