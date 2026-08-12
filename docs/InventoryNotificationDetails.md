# InventoryNotificationDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** |  | 
**image_url** | **str** |  | 
**title** | **str** |  | 

## Example

```python
from vrchatapi.models.inventory_notification_details import InventoryNotificationDetails

# TODO update the JSON string below
json = "{}"
# create an instance of InventoryNotificationDetails from a JSON string
inventory_notification_details_instance = InventoryNotificationDetails.from_json(json)
# print the JSON string representation of the object
print(InventoryNotificationDetails.to_json())

# convert the object into a dict
inventory_notification_details_dict = inventory_notification_details_instance.to_dict()
# create an instance of InventoryNotificationDetails from a dict
inventory_notification_details_from_dict = InventoryNotificationDetails.from_dict(inventory_notification_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


