# ProductPurchasePurchaseContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_type** | **str** |  | [optional] 
**world_id** | **str** | WorldID be \&quot;offline\&quot; on User profiles if you are not friends with that user. | [optional] 
**world_name** | **str** |  | [optional] 

## Example

```python
from vrchatapi.models.product_purchase_purchase_context import ProductPurchasePurchaseContext

# TODO update the JSON string below
json = "{}"
# create an instance of ProductPurchasePurchaseContext from a JSON string
product_purchase_purchase_context_instance = ProductPurchasePurchaseContext.from_json(json)
# print the JSON string representation of the object
print(ProductPurchasePurchaseContext.to_json())

# convert the object into a dict
product_purchase_purchase_context_dict = product_purchase_purchase_context_instance.to_dict()
# create an instance of ProductPurchasePurchaseContext from a dict
product_purchase_purchase_context_from_dict = ProductPurchasePurchaseContext.from_dict(product_purchase_purchase_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


