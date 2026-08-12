# GroupTransferableRequirements


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_not_monetized** | **bool** |  | [default to False]
**has_vrc_plus** | **bool** |  | [default to False]
**has_verified_email** | **bool** |  | [default to False]
**target_can_own_more_groups** | **bool** |  | [default to False]
**target_is_group_member** | **bool** |  | [default to False]

## Example

```python
from vrchatapi.models.group_transferable_requirements import GroupTransferableRequirements

# TODO update the JSON string below
json = "{}"
# create an instance of GroupTransferableRequirements from a JSON string
group_transferable_requirements_instance = GroupTransferableRequirements.from_json(json)
# print the JSON string representation of the object
print(GroupTransferableRequirements.to_json())

# convert the object into a dict
group_transferable_requirements_dict = group_transferable_requirements_instance.to_dict()
# create an instance of GroupTransferableRequirements from a dict
group_transferable_requirements_from_dict = GroupTransferableRequirements.from_dict(group_transferable_requirements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


