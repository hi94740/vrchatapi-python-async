# APIConfigLoadingScreenWeights


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announcement** | **int** |  | [optional] 
**informational** | **int** |  | [optional] 
**promotional** | **int** |  | [optional] 

## Example

```python
from vrchatapi.models.api_config_loading_screen_weights import APIConfigLoadingScreenWeights

# TODO update the JSON string below
json = "{}"
# create an instance of APIConfigLoadingScreenWeights from a JSON string
api_config_loading_screen_weights_instance = APIConfigLoadingScreenWeights.from_json(json)
# print the JSON string representation of the object
print(APIConfigLoadingScreenWeights.to_json())

# convert the object into a dict
api_config_loading_screen_weights_dict = api_config_loading_screen_weights_instance.to_dict()
# create an instance of APIConfigLoadingScreenWeights from a dict
api_config_loading_screen_weights_from_dict = APIConfigLoadingScreenWeights.from_dict(api_config_loading_screen_weights_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


