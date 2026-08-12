# InventoryDrop


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**created_at** | **datetime** |  | 
**drop_expiry_date** | **datetime** |  | 
**end_drop_date** | **datetime** |  | 
**id** | **str** |  | 
**is_disabled** | **bool** |  | 
**name** | **str** |  | 
**notification_details** | [**InventoryNotificationDetails**](InventoryNotificationDetails.md) |  | 
**start_drop_date** | **datetime** |  | 
**status** | **str** |  | 
**tags** | **List[str]** |  | 
**target_group** | **str** |  | 
**template_ids** | **List[str]** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from vrchatapi.models.inventory_drop import InventoryDrop

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryDrop from a JSON string
inventory_drop_instance = InventoryDrop.from_json(json)
# print the JSON string representation of the object
print(InventoryDrop.to_json())

# convert the object into a dict
inventory_drop_dict = inventory_drop_instance.to_dict()
# create an instance of InventoryDrop from a dict
inventory_drop_from_dict = InventoryDrop.from_dict(inventory_drop_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


