# PlatformHistoryEntry

A platform the user was recorded on, and when.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_mobile** | **bool** |  | [optional] 
**platform** | **str** | This is normally &#x60;android&#x60;, &#x60;ios&#x60;, &#x60;standalonewindows&#x60;, &#x60;web&#x60;, or the empty value &#x60;&#x60;, but also supposedly can be any random Unity version such as &#x60;2019.2.4-801-Release&#x60; or &#x60;2019.2.2-772-Release&#x60; or even &#x60;unknownplatform&#x60;. | [optional] 
**recorded** | **datetime** |  | [optional] 

## Example

```python
from vrchatapi.models.platform_history_entry import PlatformHistoryEntry

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformHistoryEntry from a JSON string
platform_history_entry_instance = PlatformHistoryEntry.from_json(json)
# print the JSON string representation of the object
print(PlatformHistoryEntry.to_json())

# convert the object into a dict
platform_history_entry_dict = platform_history_entry_instance.to_dict()
# create an instance of PlatformHistoryEntry from a dict
platform_history_entry_from_dict = PlatformHistoryEntry.from_dict(platform_history_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


