# InventoryConsumptionResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **List[object]** |  | 
**inventory_items** | [**List[InventoryItem]**](InventoryItem.md) |  | 
**inventory_items_created** | **int** |  | 

## Example

```python
from vrchatapi.models.inventory_consumption_results import InventoryConsumptionResults

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryConsumptionResults from a JSON string
inventory_consumption_results_instance = InventoryConsumptionResults.from_json(json)
# print the JSON string representation of the object
print(InventoryConsumptionResults.to_json())

# convert the object into a dict
inventory_consumption_results_dict = inventory_consumption_results_instance.to_dict()
# create an instance of InventoryConsumptionResults from a dict
inventory_consumption_results_from_dict = InventoryConsumptionResults.from_dict(inventory_consumption_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


