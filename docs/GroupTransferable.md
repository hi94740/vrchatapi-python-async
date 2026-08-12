# GroupTransferable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requirements** | [**GroupTransferableRequirements**](GroupTransferableRequirements.md) |  | 

## Example

```python
from vrchatapi.models.group_transferable import GroupTransferable

# TODO update the JSON string below
json = "{}"
# create an instance of GroupTransferable from a JSON string
group_transferable_instance = GroupTransferable.from_json(json)
# print the JSON string representation of the object
print(GroupTransferable.to_json())

# convert the object into a dict
group_transferable_dict = group_transferable_instance.to_dict()
# create an instance of GroupTransferable from a dict
group_transferable_from_dict = GroupTransferable.from_dict(group_transferable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


