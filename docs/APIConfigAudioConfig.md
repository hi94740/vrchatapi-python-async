# APIConfigAudioConfig

Global configuration for Steam Audio

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eq** | **float** | Unknown | 
**near_field_ild_nudge** | **float** | Unknown | 
**near_field_ild_nudge_distance** | **float** | Unknown | 
**near_field_ild_nudge_ear_radius** | **float** | Unknown | 
**per_ear_directionality_ear_radius** | **float** | Unknown | 
**per_ear_directionality_fade_distance** | **float** | Unknown | 
**per_ear_directionality_max_scale** | **float** | Unknown | 
**per_ear_directionality_pc_factor** | **float** | Unknown | 
**tracking_scale_max** | **float** | Unknown | 
**tracking_scale_min** | **float** | Unknown | 
**tracking_scale_multiplier** | **float** | Unknown | 

## Example

```python
from vrchatapi.models.api_config_audio_config import APIConfigAudioConfig

# TODO update the JSON string below
json = "{}"
# create an instance of APIConfigAudioConfig from a JSON string
api_config_audio_config_instance = APIConfigAudioConfig.from_json(json)
# print the JSON string representation of the object
print(APIConfigAudioConfig.to_json())

# convert the object into a dict
api_config_audio_config_dict = api_config_audio_config_instance.to_dict()
# create an instance of APIConfigAudioConfig from a dict
api_config_audio_config_from_dict = APIConfigAudioConfig.from_dict(api_config_audio_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


