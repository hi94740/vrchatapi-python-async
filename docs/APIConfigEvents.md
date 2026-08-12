# APIConfigEvents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distance_close** | **int** | Unknown | 
**distance_factor** | **int** | Unknown | 
**distance_far** | **int** | Unknown | 
**group_distance** | **int** | Unknown | 
**maximum_bunch_size** | **int** | Unknown | 
**not_visible_factor** | **int** | Unknown | 
**player_order_bucket_size** | **int** | Unknown | 
**player_order_factor** | **int** | Unknown | 
**slow_update_factor_threshold** | **int** | Unknown | 
**use_direct_player_serialization** | **bool** | Unknown | 
**view_segment_length** | **int** | Unknown | 

## Example

```python
from vrchatapi.models.api_config_events import APIConfigEvents

# TODO update the JSON string below
json = "{}"
# create an instance of APIConfigEvents from a JSON string
api_config_events_instance = APIConfigEvents.from_json(json)
# print the JSON string representation of the object
print(APIConfigEvents.to_json())

# convert the object into a dict
api_config_events_dict = api_config_events_instance.to_dict()
# create an instance of APIConfigEvents from a dict
api_config_events_from_dict = APIConfigEvents.from_dict(api_config_events_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


