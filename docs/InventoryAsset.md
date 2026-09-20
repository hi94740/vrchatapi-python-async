# InventoryAsset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** |  | [optional] 
**frame_count** | **int** |  | [optional] 
**frames_per_second** | **float** |  | [optional] 
**loop_count** | **int** |  | [optional] 
**total_duration_ms** | **int** |  | [optional] 
**type** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from vrchatapi.models.inventory_asset import InventoryAsset

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryAsset from a JSON string
inventory_asset_instance = InventoryAsset.from_json(json)
# print the JSON string representation of the object
print(InventoryAsset.to_json())

# convert the object into a dict
inventory_asset_dict = inventory_asset_instance.to_dict()
# create an instance of InventoryAsset from a dict
inventory_asset_from_dict = InventoryAsset.from_dict(inventory_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


