# TokenBundle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | price of the bundle | 
**apple_product_id** | **str** |  | 
**description** | **str** |  | 
**google_product_id** | **str** |  | [optional] 
**id** | **str** |  | 
**image_url** | **str** | direct url to image | 
**oculus_sku** | **str** |  | 
**steam_item_id** | **str** |  | 
**tokens** | **int** | number of tokens received | 

## Example

```python
from vrchatapi.models.token_bundle import TokenBundle

# TODO update the JSON string below
json = "{}"
# create an instance of TokenBundle from a JSON string
token_bundle_instance = TokenBundle.from_json(json)
# print the JSON string representation of the object
print(TokenBundle.to_json())

# convert the object into a dict
token_bundle_dict = token_bundle_instance.to_dict()
# create an instance of TokenBundle from a dict
token_bundle_from_dict = TokenBundle.from_dict(token_bundle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


