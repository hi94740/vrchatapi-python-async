# InstanceCategory

A category an instance can be listed under.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted** | **bool** |  | 
**icon_url** | **str** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**order** | **int** |  | 

## Example

```python
from vrchatapi.models.instance_category import InstanceCategory

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceCategory from a JSON string
instance_category_instance = InstanceCategory.from_json(json)
# print the JSON string representation of the object
print(InstanceCategory.to_json())

# convert the object into a dict
instance_category_dict = instance_category_instance.to_dict()
# create an instance of InstanceCategory from a dict
instance_category_from_dict = InstanceCategory.from_dict(instance_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


