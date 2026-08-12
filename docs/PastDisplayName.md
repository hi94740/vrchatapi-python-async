# PastDisplayName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from vrchatapi.models.past_display_name import PastDisplayName

# TODO update the JSON string below
json = "{}"
# create an instance of PastDisplayName from a JSON string
past_display_name_instance = PastDisplayName.from_json(json)
# print the JSON string representation of the object
print(PastDisplayName.to_json())

# convert the object into a dict
past_display_name_dict = past_display_name_instance.to_dict()
# create an instance of PastDisplayName from a dict
past_display_name_from_dict = PastDisplayName.from_dict(past_display_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


