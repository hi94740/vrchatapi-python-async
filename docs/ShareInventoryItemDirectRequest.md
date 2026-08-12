# ShareInventoryItemDirectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_id** | **str** |  | 
**users** | **List[str]** |  | 

## Example

```python
from vrchatapi.models.share_inventory_item_direct_request import ShareInventoryItemDirectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ShareInventoryItemDirectRequest from a JSON string
share_inventory_item_direct_request_instance = ShareInventoryItemDirectRequest.from_json(json)
# print the JSON string representation of the object
print(ShareInventoryItemDirectRequest.to_json())

# convert the object into a dict
share_inventory_item_direct_request_dict = share_inventory_item_direct_request_instance.to_dict()
# create an instance of ShareInventoryItemDirectRequest from a dict
share_inventory_item_direct_request_from_dict = ShareInventoryItemDirectRequest.from_dict(share_inventory_item_direct_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


