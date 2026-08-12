# StoreContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**image_url** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from vrchatapi.models.store_context import StoreContext

# TODO update the JSON string below
json = "{}"
# create an instance of StoreContext from a JSON string
store_context_instance = StoreContext.from_json(json)
# print the JSON string representation of the object
print(StoreContext.to_json())

# convert the object into a dict
store_context_dict = store_context_instance.to_dict()
# create an instance of StoreContext from a dict
store_context_from_dict = StoreContext.from_dict(store_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


