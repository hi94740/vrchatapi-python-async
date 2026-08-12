# APIConfigIosVersion

Current version for iOS

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**major** | **int** |  | 
**minor** | **int** |  | 

## Example

```python
from vrchatapi.models.api_config_ios_version import APIConfigIosVersion

# TODO update the JSON string below
json = "{}"
# create an instance of APIConfigIosVersion from a JSON string
api_config_ios_version_instance = APIConfigIosVersion.from_json(json)
# print the JSON string representation of the object
print(APIConfigIosVersion.to_json())

# convert the object into a dict
api_config_ios_version_dict = api_config_ios_version_instance.to_dict()
# create an instance of APIConfigIosVersion from a dict
api_config_ios_version_from_dict = APIConfigIosVersion.from_dict(api_config_ios_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


