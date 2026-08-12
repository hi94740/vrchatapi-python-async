# ProductListing


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | 
**archived** | **bool** |  | [optional] 
**buyer_refundable** | **bool** |  | 
**created** | **datetime** |  | [optional] 
**description** | **str** |  | 
**display_name** | **str** |  | 
**duration** | **int** |  | [optional] 
**duration_type** | **str** |  | [optional] 
**group_icon** | **str** |  | [optional] 
**group_id** | **str** |  | [optional] 
**group_name** | **str** |  | [optional] 
**has_avatar** | **bool** |  | 
**has_udon** | **bool** |  | 
**hydrated_products** | [**List[Product]**](Product.md) |  | [optional] 
**id** | **str** |  | 
**image_id** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**listing_type** | [**ProductListingType**](ProductListingType.md) |  | [default to ProductListingType.SUBSCRIPTION]
**listing_variants** | [**List[ProductListingVariant]**](ProductListingVariant.md) |  | [optional] 
**permanent** | **bool** |  | [optional] 
**price_tokens** | **int** |  | 
**product_ids** | **List[str]** |  | 
**product_type** | [**ProductType**](ProductType.md) |  | [default to ProductType.UDON]
**products** | **List[object]** |  | 
**purchase_count** | **int** |  | [optional] 
**purchase_count_quantity** | **int** |  | [optional] 
**quantifiable** | **bool** |  | [optional] 
**recurrable** | **bool** |  | 
**refundable** | **bool** |  | 
**seller_display_name** | **str** |  | 
**seller_id** | **str** |  | 
**sold_by_vrc** | **bool** |  | [optional] 
**stackable** | **bool** |  | 
**store_ids** | **List[str]** |  | 
**subtitle** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**updated** | **datetime** |  | [optional] 
**vrc_plus_discount_price** | **int** |  | [optional] 
**when_to_expire** | **datetime** |  | [optional] 

## Example

```python
from vrchatapi.models.product_listing import ProductListing

# TODO update the JSON string below
json = "{}"
# create an instance of ProductListing from a JSON string
product_listing_instance = ProductListing.from_json(json)
# print the JSON string representation of the object
print(ProductListing.to_json())

# convert the object into a dict
product_listing_dict = product_listing_instance.to_dict()
# create an instance of ProductListing from a dict
product_listing_from_dict = ProductListing.from_dict(product_listing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


