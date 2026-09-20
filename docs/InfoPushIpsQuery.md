# InfoPushIpsQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **str** |  | [optional] 
**require** | **str** |  | [optional] 

## Example

```python
from vrchatapi.models.info_push_ips_query import InfoPushIpsQuery

# TODO update the JSON string below
json = "{}"
# create an instance of InfoPushIpsQuery from a JSON string
info_push_ips_query_instance = InfoPushIpsQuery.from_json(json)
# print the JSON string representation of the object
print(InfoPushIpsQuery.to_json())

# convert the object into a dict
info_push_ips_query_dict = info_push_ips_query_instance.to_dict()
# create an instance of InfoPushIpsQuery from a dict
info_push_ips_query_from_dict = InfoPushIpsQuery.from_dict(info_push_ips_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


