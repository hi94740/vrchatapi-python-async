# UpdateAvatarRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_url** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**release_status** | [**ReleaseStatus**](ReleaseStatus.md) |  | [optional] [default to ReleaseStatus.PUBLIC]
**tags** | **List[str]** |   | [optional] 
**unity_package_url** | **str** |  | [optional] 
**unity_version** | **str** |  | [optional] [default to '5.3.4p1']
**version** | **int** |  | [optional] [default to 1]

## Example

```python
from vrchatapi.models.update_avatar_request import UpdateAvatarRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAvatarRequest from a JSON string
update_avatar_request_instance = UpdateAvatarRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAvatarRequest.to_json())

# convert the object into a dict
update_avatar_request_dict = update_avatar_request_instance.to_dict()
# create an instance of UpdateAvatarRequest from a dict
update_avatar_request_from_dict = UpdateAvatarRequest.from_dict(update_avatar_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


