# EconomyStatus

Whether the economy is accepting requests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**economy_online** | **bool** |  | 
**economy_state** | **int** |  | 

## Example

```python
from vrchatapi.models.economy_status import EconomyStatus

# TODO update the JSON string below
json = "{}"
# create an instance of EconomyStatus from a JSON string
economy_status_instance = EconomyStatus.from_json(json)
# print the JSON string representation of the object
print(EconomyStatus.to_json())

# convert the object into a dict
economy_status_dict = economy_status_instance.to_dict()
# create an instance of EconomyStatus from a dict
economy_status_from_dict = EconomyStatus.from_dict(economy_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


