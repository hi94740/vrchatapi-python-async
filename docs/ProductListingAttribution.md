# ProductListingAttribution

Attribution shown alongside a listing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collaboration_id** | **str** |  | [optional] 
**creator** | [**ProductListingAttributionCreator**](ProductListingAttributionCreator.md) |  | [optional] 
**publisher** | [**ProductListingAttributionCreator**](ProductListingAttributionCreator.md) |  | [optional] 

## Example

```python
from vrchatapi.models.product_listing_attribution import ProductListingAttribution

# TODO update the JSON string below
json = "{}"
# create an instance of ProductListingAttribution from a JSON string
product_listing_attribution_instance = ProductListingAttribution.from_json(json)
# print the JSON string representation of the object
print(ProductListingAttribution.to_json())

# convert the object into a dict
product_listing_attribution_dict = product_listing_attribution_instance.to_dict()
# create an instance of ProductListingAttribution from a dict
product_listing_attribution_from_dict = ProductListingAttribution.from_dict(product_listing_attribution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


