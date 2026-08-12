# Mutuals


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**friends** | **int** |  | [default to 0]
**groups** | **int** |  | [default to 0]

## Example

```python
from vrchatapi.models.mutuals import Mutuals

# TODO update the JSON string below
json = "{}"
# create an instance of Mutuals from a JSON string
mutuals_instance = Mutuals.from_json(json)
# print the JSON string representation of the object
print(Mutuals.to_json())

# convert the object into a dict
mutuals_dict = mutuals_instance.to_dict()
# create an instance of Mutuals from a dict
mutuals_from_dict = Mutuals.from_dict(mutuals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


