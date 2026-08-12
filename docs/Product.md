# Product


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archived** | **bool** |  | [optional] 
**created** | **datetime** |  | [optional] 
**description** | **str** |  | 
**display_name** | **str** |  | 
**group_access** | **bool** |  | [optional] [default to False]
**group_access_remove** | **bool** |  | [optional] [default to False]
**group_id** | **str** |  | [optional] 
**group_role_id** | **str** |  | [optional] 
**id** | **str** |  | 
**image_id** | **str** |  | 
**image_url** | **str** |  | [optional] 
**parent_listings** | **List[str]** |  | 
**product_type** | [**ProductType**](ProductType.md) |  | [default to ProductType.UDON]
**product_type_label** | **str** |  | [optional] 
**purchase_count** | **int** |  | [optional] 
**purchase_count_quantity** | **int** |  | [optional] 
**seller_display_name** | **str** |  | 
**seller_id** | **str** |  | 
**tags** | **List[str]** |  | 
**updated** | **datetime** |  | [optional] 
**use_for_subscriber_list** | **bool** |  | [optional] [default to False]

## Example

```python
from vrchatapi.models.product import Product

# TODO update the JSON string below
json = "{}"
# create an instance of Product from a JSON string
product_instance = Product.from_json(json)
# print the JSON string representation of the object
print(Product.to_json())

# convert the object into a dict
product_dict = product_instance.to_dict()
# create an instance of Product from a dict
product_from_dict = Product.from_dict(product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


