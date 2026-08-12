# PropPublishStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_publish** | **bool** |  | [optional] [default to False]

## Example

```python
from vrchatapi.models.prop_publish_status import PropPublishStatus

# TODO update the JSON string below
json = "{}"
# create an instance of PropPublishStatus from a JSON string
prop_publish_status_instance = PropPublishStatus.from_json(json)
# print the JSON string representation of the object
print(PropPublishStatus.to_json())

# convert the object into a dict
prop_publish_status_dict = prop_publish_status_instance.to_dict()
# create an instance of PropPublishStatus from a dict
prop_publish_status_from_dict = PropPublishStatus.from_dict(prop_publish_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


