# APIHealth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_version_tag** | **str** |  | 
**ok** | **bool** |  | 
**server_name** | **str** |  | 

## Example

```python
from vrchatapi.models.api_health import APIHealth

# TODO update the JSON string below
json = "{}"
# create an instance of APIHealth from a JSON string
api_health_instance = APIHealth.from_json(json)
# print the JSON string representation of the object
print(APIHealth.to_json())

# convert the object into a dict
api_health_dict = api_health_instance.to_dict()
# create an instance of APIHealth from a dict
api_health_from_dict = APIHealth.from_dict(api_health_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


