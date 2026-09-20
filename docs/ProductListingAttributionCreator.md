# ProductListingAttributionCreator

The creator credited on a listing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_name** | **str** |  | [optional] 
**user_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 

## Example

```python
from vrchatapi.models.product_listing_attribution_creator import ProductListingAttributionCreator

# TODO update the JSON string below
json = "{}"
# create an instance of ProductListingAttributionCreator from a JSON string
product_listing_attribution_creator_instance = ProductListingAttributionCreator.from_json(json)
# print the JSON string representation of the object
print(ProductListingAttributionCreator.to_json())

# convert the object into a dict
product_listing_attribution_creator_dict = product_listing_attribution_creator_instance.to_dict()
# create an instance of ProductListingAttributionCreator from a dict
product_listing_attribution_creator_from_dict = ProductListingAttributionCreator.from_dict(product_listing_attribution_creator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


