# ProductListingVariant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_from** | **datetime** |  | [optional] 
**listing_variant_id** | **str** |  | 
**non_refundable** | **bool** |  | 
**quantity** | **int** |  | 
**seller_variant** | **bool** |  | 
**unit_price_tokens** | **int** |  | 

## Example

```python
from vrchatapi.models.product_listing_variant import ProductListingVariant

# TODO update the JSON string below
json = "{}"
# create an instance of ProductListingVariant from a JSON string
product_listing_variant_instance = ProductListingVariant.from_json(json)
# print the JSON string representation of the object
print(ProductListingVariant.to_json())

# convert the object into a dict
product_listing_variant_dict = product_listing_variant_instance.to_dict()
# create an instance of ProductListingVariant from a dict
product_listing_variant_from_dict = ProductListingVariant.from_dict(product_listing_variant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


