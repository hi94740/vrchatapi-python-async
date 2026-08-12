# APIConfigAnnouncement

Public Announcement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Announcement name | 
**text** | **str** | Announcement text | 

## Example

```python
from vrchatapi.models.api_config_announcement import APIConfigAnnouncement

# TODO update the JSON string below
json = "{}"
# create an instance of APIConfigAnnouncement from a JSON string
api_config_announcement_instance = APIConfigAnnouncement.from_json(json)
# print the JSON string representation of the object
print(APIConfigAnnouncement.to_json())

# convert the object into a dict
api_config_announcement_dict = api_config_announcement_instance.to_dict()
# create an instance of APIConfigAnnouncement from a dict
api_config_announcement_from_dict = APIConfigAnnouncement.from_dict(api_config_announcement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


