# EquipInventoryItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**equip_slot** | [**InventoryEquipSlot**](InventoryEquipSlot.md) |  | [default to InventoryEquipSlot.EMPTY]

## Example

```python
from vrchatapi.models.equip_inventory_item_request import EquipInventoryItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EquipInventoryItemRequest from a JSON string
equip_inventory_item_request_instance = EquipInventoryItemRequest.from_json(json)
# print the JSON string representation of the object
print(EquipInventoryItemRequest.to_json())

# convert the object into a dict
equip_inventory_item_request_dict = equip_inventory_item_request_instance.to_dict()
# create an instance of EquipInventoryItemRequest from a dict
equip_inventory_item_request_from_dict = EquipInventoryItemRequest.from_dict(equip_inventory_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


