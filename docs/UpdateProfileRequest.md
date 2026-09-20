# UpdateProfileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**background_texture_id** | **str** |  | [optional] 
**background_type** | **str** |  | [optional] 
**banner_color** | **str** | Six hexadecimal digits, without a leading &#x60;#&#x60;. May be empty. | [optional] 
**banner_type** | **str** |  | [optional] 
**bio** | **str** |  | [optional] 
**bio_links** | **List[str]** |  | [optional] 
**icon_frame** | **str** |  | [optional] 
**languages** | **List[str]** |  | [optional] 
**nameplate_effect** | **str** |  | [optional] 
**profile_effect** | **str** |  | [optional] 
**theme_id** | **str** |  | [optional] 
**user_icon** | **str** |  | [optional] 

## Example

```python
from vrchatapi.models.update_profile_request import UpdateProfileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProfileRequest from a JSON string
update_profile_request_instance = UpdateProfileRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateProfileRequest.to_json())

# convert the object into a dict
update_profile_request_dict = update_profile_request_instance.to_dict()
# create an instance of UpdateProfileRequest from a dict
update_profile_request_from_dict = UpdateProfileRequest.from_dict(update_profile_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


