# UpdateGroupRepresentationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_representing** | **bool** | Whether the user is representing the group. | 

## Example

```python
from vrchatapi.models.update_group_representation_request import UpdateGroupRepresentationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGroupRepresentationRequest from a JSON string
update_group_representation_request_instance = UpdateGroupRepresentationRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateGroupRepresentationRequest.to_json())

# convert the object into a dict
update_group_representation_request_dict = update_group_representation_request_instance.to_dict()
# create an instance of UpdateGroupRepresentationRequest from a dict
update_group_representation_request_from_dict = UpdateGroupRepresentationRequest.from_dict(update_group_representation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


