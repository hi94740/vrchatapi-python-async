# WorldMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | WorldID be \&quot;offline\&quot; on User profiles if you are not friends with that user. | 
**metadata** | **object** |  | 

## Example

```python
from vrchatapi.models.world_metadata import WorldMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of WorldMetadata from a JSON string
world_metadata_instance = WorldMetadata.from_json(json)
# print the JSON string representation of the object
print(WorldMetadata.to_json())

# convert the object into a dict
world_metadata_dict = world_metadata_instance.to_dict()
# create an instance of WorldMetadata from a dict
world_metadata_from_dict = WorldMetadata.from_dict(world_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


