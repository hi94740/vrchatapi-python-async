# ProductPurchaseRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** |  | 
**balance** | **int** |  | 
**var_date** | **datetime** |  | 
**from_user_display_name** | **str** |  | 
**listing_display_name** | **str** |  | 
**listing_type** | [**ProductListingType**](ProductListingType.md) |  | [default to ProductListingType.SUBSCRIPTION]
**platform** | **str** | Where (first- or third-party) the purchase was made | 
**purchase_id** | **str** |  | 
**reason** | **int** |  | 
**reason_label** | **str** |  | 
**transaction_id** | **int** |  | 
**transaction_line_id** | **int** |  | 

## Example

```python
from vrchatapi.models.product_purchase_record import ProductPurchaseRecord

# TODO update the JSON string below
json = "{}"
# create an instance of ProductPurchaseRecord from a JSON string
product_purchase_record_instance = ProductPurchaseRecord.from_json(json)
# print the JSON string representation of the object
print(ProductPurchaseRecord.to_json())

# convert the object into a dict
product_purchase_record_dict = product_purchase_record_instance.to_dict()
# create an instance of ProductPurchaseRecord from a dict
product_purchase_record_from_dict = ProductPurchaseRecord.from_dict(product_purchase_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


