# APIConfigConstantsLANGUAGE

Language-related constants

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spoken_language_options** | **Dict[str, str]** | Supported spoken language options | [optional] 

## Example

```python
from vrchatapi.models.api_config_constants_language import APIConfigConstantsLANGUAGE

# TODO update the JSON string below
json = "{}"
# create an instance of APIConfigConstantsLANGUAGE from a JSON string
api_config_constants_language_instance = APIConfigConstantsLANGUAGE.from_json(json)
# print the JSON string representation of the object
print(APIConfigConstantsLANGUAGE.to_json())

# convert the object into a dict
api_config_constants_language_dict = api_config_constants_language_instance.to_dict()
# create an instance of APIConfigConstantsLANGUAGE from a dict
api_config_constants_language_from_dict = APIConfigConstantsLANGUAGE.from_dict(api_config_constants_language_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


