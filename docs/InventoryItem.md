# InventoryItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collections** | **List[str]** |  | 
**created_at** | **datetime** |  | 
**default_attributes** | [**Dict[str, InventoryDefaultAttributesValue]**](InventoryDefaultAttributesValue.md) |  | 
**description** | **str** |  | 
**equip_slot** | [**InventoryEquipSlot**](InventoryEquipSlot.md) |  | [optional] [default to InventoryEquipSlot.EMPTY]
**equip_slots** | [**List[InventoryEquipSlot]**](InventoryEquipSlot.md) |  | [optional] 
**expiry_date** | **datetime** |  | [optional] 
**flags** | **List[str]** |  | 
**holder_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**id** | **str** |  | 
**image_url** | **str** |  | 
**is_archived** | **bool** |  | 
**is_seen** | **bool** |  | 
**item_type** | [**InventoryItemType**](InventoryItemType.md) |  | [default to InventoryItemType.BUNDLE]
**item_type_label** | **str** |  | 
**metadata** | [**InventoryMetadata**](InventoryMetadata.md) |  | 
**name** | **str** |  | 
**quantifiable** | **bool** |  | 
**tags** | **List[str]** |  | 
**template_id** | **str** |  | 
**template_created_at** | **datetime** |  | 
**template_updated_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**user_attributes** | [**InventoryUserAttributes**](InventoryUserAttributes.md) |  | 
**validate_user_attributes** | **bool** |  | 

## Example

```python
from vrchatapi.models.inventory_item import InventoryItem

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryItem from a JSON string
inventory_item_instance = InventoryItem.from_json(json)
# print the JSON string representation of the object
print(InventoryItem.to_json())

# convert the object into a dict
inventory_item_dict = inventory_item_instance.to_dict()
# create an instance of InventoryItem from a dict
inventory_item_from_dict = InventoryItem.from_dict(inventory_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


