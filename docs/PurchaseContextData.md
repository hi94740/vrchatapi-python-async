# PurchaseContextData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_type** | [**ProductPurchaseLocationType**](ProductPurchaseLocationType.md) |  | [default to ProductPurchaseLocationType.WEB_GROUP_STORE]
**store_id** | **str** |  | [optional] 
**world_id** | **str** | WorldID be \&quot;offline\&quot; on User profiles if you are not friends with that user. | [optional] 

## Example

```python
from vrchatapi.models.purchase_context_data import PurchaseContextData

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseContextData from a JSON string
purchase_context_data_instance = PurchaseContextData.from_json(json)
# print the JSON string representation of the object
print(PurchaseContextData.to_json())

# convert the object into a dict
purchase_context_data_dict = purchase_context_data_instance.to_dict()
# create an instance of PurchaseContextData from a dict
purchase_context_data_from_dict = PurchaseContextData.from_dict(purchase_context_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


