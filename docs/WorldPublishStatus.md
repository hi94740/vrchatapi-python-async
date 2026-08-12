# WorldPublishStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_publish** | **bool** |  | [default to True]

## Example

```python
from vrchatapi.models.world_publish_status import WorldPublishStatus

# TODO update the JSON string below
json = "{}"
# create an instance of WorldPublishStatus from a JSON string
world_publish_status_instance = WorldPublishStatus.from_json(json)
# print the JSON string representation of the object
print(WorldPublishStatus.to_json())

# convert the object into a dict
world_publish_status_dict = world_publish_status_instance.to_dict()
# create an instance of WorldPublishStatus from a dict
world_publish_status_from_dict = WorldPublishStatus.from_dict(world_publish_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


