# InfoPush



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_min_version** | **object** |  | [optional] 
**created_at** | **datetime** |  | 
**data** | [**InfoPushData**](InfoPushData.md) |  | 
**end_date** | **datetime** |  | [optional] 
**experiment** | [**InfoPushExperiment**](InfoPushExperiment.md) |  | [optional] 
**hash** | **str** | Unknown usage, MD5 | 
**id** | **str** |  | 
**is_enabled** | **bool** |  | [default to True]
**priority** | **int** |  | 
**regions** | **List[str]** |  | [optional] 
**release_status** | [**ReleaseStatus**](ReleaseStatus.md) |  | [default to ReleaseStatus.PUBLIC]
**require_client_tags** | **List[str]** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**tags** | **List[str]** |   | 
**updated_at** | **datetime** |  | 

## Example

```python
from vrchatapi.models.info_push import InfoPush

# TODO update the JSON string below
json = "{}"
# create an instance of InfoPush from a JSON string
info_push_instance = InfoPush.from_json(json)
# print the JSON string representation of the object
print(InfoPush.to_json())

# convert the object into a dict
info_push_dict = info_push_instance.to_dict()
# create an instance of InfoPush from a dict
info_push_from_dict = InfoPush.from_dict(info_push_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


