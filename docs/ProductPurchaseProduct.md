# ProductPurchaseProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | 
**id** | **str** |  | 
**image_id** | **str** |  | [optional] 
**license_id** | **str** |  | [optional] 
**product_type** | [**ProductType**](ProductType.md) |  | [default to ProductType.UDON]

## Example

```python
from vrchatapi.models.product_purchase_product import ProductPurchaseProduct

# TODO update the JSON string below
json = "{}"
# create an instance of ProductPurchaseProduct from a JSON string
product_purchase_product_instance = ProductPurchaseProduct.from_json(json)
# print the JSON string representation of the object
print(ProductPurchaseProduct.to_json())

# convert the object into a dict
product_purchase_product_dict = product_purchase_product_instance.to_dict()
# create an instance of ProductPurchaseProduct from a dict
product_purchase_product_from_dict = ProductPurchaseProduct.from_dict(product_purchase_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


