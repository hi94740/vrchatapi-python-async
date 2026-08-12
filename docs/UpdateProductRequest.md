# UpdateProductRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**image_id** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**use_for_subscriber_list** | **bool** |  | [optional] 

## Example

```python
from vrchatapi.models.update_product_request import UpdateProductRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProductRequest from a JSON string
update_product_request_instance = UpdateProductRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateProductRequest.to_json())

# convert the object into a dict
update_product_request_dict = update_product_request_instance.to_dict()
# create an instance of UpdateProductRequest from a dict
update_product_request_from_dict = UpdateProductRequest.from_dict(update_product_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


