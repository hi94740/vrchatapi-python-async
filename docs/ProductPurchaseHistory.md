# ProductPurchaseHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date** | **datetime** |  | 
**start_date** | **datetime** |  | 
**transactions** | [**List[ProductPurchaseRecord]**](ProductPurchaseRecord.md) |  | 

## Example

```python
from vrchatapi.models.product_purchase_history import ProductPurchaseHistory

# TODO update the JSON string below
json = "{}"
# create an instance of ProductPurchaseHistory from a JSON string
product_purchase_history_instance = ProductPurchaseHistory.from_json(json)
# print the JSON string representation of the object
print(ProductPurchaseHistory.to_json())

# convert the object into a dict
product_purchase_history_dict = product_purchase_history_instance.to_dict()
# create an instance of ProductPurchaseHistory from a dict
product_purchase_history_from_dict = ProductPurchaseHistory.from_dict(product_purchase_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


