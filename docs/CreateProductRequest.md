# CreateProductRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**display_name** | **str** |  | 
**image_id** | **str** |  | 
**product_type** | [**ProductType**](ProductType.md) |  | [default to ProductType.UDON]
**tags** | **List[str]** |  | 
**use_for_subscriber_list** | **bool** |  | 

## Example

```python
from vrchatapi.models.create_product_request import CreateProductRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProductRequest from a JSON string
create_product_request_instance = CreateProductRequest.from_json(json)
# print the JSON string representation of the object
print(CreateProductRequest.to_json())

# convert the object into a dict
create_product_request_dict = create_product_request_instance.to_dict()
# create an instance of CreateProductRequest from a dict
create_product_request_from_dict = CreateProductRequest.from_dict(create_product_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


