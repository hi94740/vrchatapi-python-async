# UpdateWorldRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_url** | **str** |  | [optional] 
**asset_version** | **str** |  | [optional] 
**author_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 
**author_name** | **str** |  | [optional] 
**capacity** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**platform** | **str** | This is normally &#x60;android&#x60;, &#x60;ios&#x60;, &#x60;standalonewindows&#x60;, &#x60;web&#x60;, or the empty value &#x60;&#x60;, but also supposedly can be any random Unity version such as &#x60;2019.2.4-801-Release&#x60; or &#x60;2019.2.2-772-Release&#x60; or even &#x60;unknownplatform&#x60;. | [optional] 
**release_status** | [**ReleaseStatus**](ReleaseStatus.md) |  | [optional] [default to ReleaseStatus.PUBLIC]
**tags** | **List[str]** |   | [optional] 
**unity_package_url** | **str** |  | [optional] 
**unity_version** | **str** |  | [optional] [default to '5.3.4p1']

## Example

```python
from vrchatapi.models.update_world_request import UpdateWorldRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWorldRequest from a JSON string
update_world_request_instance = UpdateWorldRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateWorldRequest.to_json())

# convert the object into a dict
update_world_request_dict = update_world_request_instance.to_dict()
# create an instance of UpdateWorldRequest from a dict
update_world_request_from_dict = UpdateWorldRequest.from_dict(update_world_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


