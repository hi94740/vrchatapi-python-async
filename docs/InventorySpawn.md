# InventorySpawn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | 
**version** | **int** |  | 

## Example

```python
from vrchatapi.models.inventory_spawn import InventorySpawn

# TODO update the JSON string below
json = "{}"
# create an instance of InventorySpawn from a JSON string
inventory_spawn_instance = InventorySpawn.from_json(json)
# print the JSON string representation of the object
print(InventorySpawn.to_json())

# convert the object into a dict
inventory_spawn_dict = inventory_spawn_instance.to_dict()
# create an instance of InventorySpawn from a dict
inventory_spawn_from_dict = InventorySpawn.from_dict(inventory_spawn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


