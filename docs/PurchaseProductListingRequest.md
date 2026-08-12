# PurchaseProductListingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_data** | [**PurchaseContextData**](PurchaseContextData.md) |  | [optional] 
**listing_id** | **str** |  | 
**listing_variant_id** | **str** |  | [optional] 
**quantity** | **int** |  | [default to 1]
**receiver_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 
**stackable** | **bool** |  | [optional] 
**total_price** | **int** |  | 

## Example

```python
from vrchatapi.models.purchase_product_listing_request import PurchaseProductListingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseProductListingRequest from a JSON string
purchase_product_listing_request_instance = PurchaseProductListingRequest.from_json(json)
# print the JSON string representation of the object
print(PurchaseProductListingRequest.to_json())

# convert the object into a dict
purchase_product_listing_request_dict = purchase_product_listing_request_instance.to_dict()
# create an instance of PurchaseProductListingRequest from a dict
purchase_product_listing_request_from_dict = PurchaseProductListingRequest.from_dict(purchase_product_listing_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


