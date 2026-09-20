# Beta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | 
**beta_app_id** | **str** |  | [optional] 
**beta_group_id** | **str** |  | [optional] 
**beta_name** | **str** |  | 
**created_at** | **datetime** |  | 
**id** | **str** |  | 
**last_synchronized_at** | **datetime** |  | [optional] 
**type** | **str** |  | 
**updated_at** | **datetime** |  | 
**user_fields** | [**Dict[str, BetaUserField]**](BetaUserField.md) | The fields a registration must supply, keyed by field name. | 

## Example

```python
from vrchatapi.models.beta import Beta

# TODO update the JSON string below
json = "{}"
# create an instance of Beta from a JSON string
beta_instance = Beta.from_json(json)
# print the JSON string representation of the object
print(Beta.to_json())

# convert the object into a dict
beta_dict = beta_instance.to_dict()
# create an instance of Beta from a dict
beta_from_dict = Beta.from_dict(beta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


