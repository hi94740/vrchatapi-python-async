# APIConfigConstants

Constants

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**APIConfigConstantsGROUPS**](APIConfigConstantsGROUPS.md) |  | 
**instance** | [**APIConfigConstantsINSTANCE**](APIConfigConstantsINSTANCE.md) |  | 
**language** | [**APIConfigConstantsLANGUAGE**](APIConfigConstantsLANGUAGE.md) |  | 

## Example

```python
from vrchatapi.models.api_config_constants import APIConfigConstants

# TODO update the JSON string below
json = "{}"
# create an instance of APIConfigConstants from a JSON string
api_config_constants_instance = APIConfigConstants.from_json(json)
# print the JSON string representation of the object
print(APIConfigConstants.to_json())

# convert the object into a dict
api_config_constants_dict = api_config_constants_instance.to_dict()
# create an instance of APIConfigConstants from a dict
api_config_constants_from_dict = APIConfigConstants.from_dict(api_config_constants_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


