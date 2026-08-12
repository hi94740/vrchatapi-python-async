# ModelPrint

Info about a print

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**author_name** | **str** |  | 
**created_at** | **datetime** |  | 
**files** | [**PrintFiles**](PrintFiles.md) |  | 
**id** | **str** |  | 
**note** | **str** |  | 
**owner_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 
**timestamp** | **datetime** |  | 
**world_id** | **str** | WorldID be \&quot;offline\&quot; on User profiles if you are not friends with that user. | 
**world_name** | **str** |  | 

## Example

```python
from vrchatapi.models.model_print import ModelPrint

# TODO update the JSON string below
json = "{}"
# create an instance of ModelPrint from a JSON string
model_print_instance = ModelPrint.from_json(json)
# print the JSON string representation of the object
print(ModelPrint.to_json())

# convert the object into a dict
model_print_dict = model_print_instance.to_dict()
# create an instance of ModelPrint from a dict
model_print_from_dict = ModelPrint.from_dict(model_print_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


