# InventoryMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**animated** | **bool** |  | [optional] 
**animation_style** | **str** |  | [optional] 
**asset_bundle_id** | **str** |  | [optional] 
**file_id** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**inventory_items_to_instantiate** | **List[str]** | Only in bundles | [optional] 
**mask_tag** | **str** |  | [optional] 
**prop_id** | **str** |  | [optional] 

## Example

```python
from vrchatapi.models.inventory_metadata import InventoryMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryMetadata from a JSON string
inventory_metadata_instance = InventoryMetadata.from_json(json)
# print the JSON string representation of the object
print(InventoryMetadata.to_json())

# convert the object into a dict
inventory_metadata_dict = inventory_metadata_instance.to_dict()
# create an instance of InventoryMetadata from a dict
inventory_metadata_from_dict = InventoryMetadata.from_dict(inventory_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


