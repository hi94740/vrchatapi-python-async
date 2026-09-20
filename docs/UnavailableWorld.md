# UnavailableWorld

Stands in for a world the API will not describe. `name` and `authorName` are `???`, `imageUrl` is empty, and the counts are `0`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_name** | **str** |  | 
**capacity** | **int** |  | 
**id** | **str** | WorldID be \&quot;offline\&quot; on User profiles if you are not friends with that user. | 
**image_url** | **str** |  | 
**is_secure** | **bool** |  | 
**name** | **str** |  | 
**occupants** | **int** |  | 
**thumbnail_image_url** | **str** |  | 

## Example

```python
from vrchatapi.models.unavailable_world import UnavailableWorld

# TODO update the JSON string below
json = "{}"
# create an instance of UnavailableWorld from a JSON string
unavailable_world_instance = UnavailableWorld.from_json(json)
# print the JSON string representation of the object
print(UnavailableWorld.to_json())

# convert the object into a dict
unavailable_world_dict = unavailable_world_instance.to_dict()
# create an instance of UnavailableWorld from a dict
unavailable_world_from_dict = UnavailableWorld.from_dict(unavailable_world_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


