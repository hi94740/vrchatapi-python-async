# InventoryTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**collections** | **List[str]** |  | 
**created_at** | **datetime** |  | 
**default_attributes** | **object** |  | 
**description** | **str** |  | 
**equip_slots** | **List[str]** |  | 
**flags** | **List[str]** |  | 
**id** | **str** |  | 
**image_url** | **str** |  | 
**item_type** | [**InventoryItemType**](InventoryItemType.md) |  | [default to InventoryItemType.BUNDLE]
**item_type_label** | **str** |  | 
**metadata** | [**InventoryMetadata**](InventoryMetadata.md) |  | [optional] 
**name** | **str** |  | 
**notification_details** | [**InventoryNotificationDetails**](InventoryNotificationDetails.md) |  | [optional] 
**status** | **str** |  | 
**tags** | **List[str]** |  | 
**updated_at** | **datetime** |  | 
**validate_user_attributes** | **bool** |  | 

## Example

```python
from vrchatapi.models.inventory_template import InventoryTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryTemplate from a JSON string
inventory_template_instance = InventoryTemplate.from_json(json)
# print the JSON string representation of the object
print(InventoryTemplate.to_json())

# convert the object into a dict
inventory_template_dict = inventory_template_instance.to_dict()
# create an instance of InventoryTemplate from a dict
inventory_template_from_dict = InventoryTemplate.from_dict(inventory_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


