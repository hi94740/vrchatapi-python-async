# APIConfigDownloadURLList

Download links for various development assets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bootstrap** | **str** | Download link for ??? | 
**sdk2** | **str** | Download link for legacy SDK2 | 
**sdk3_avatars** | **str** | Download link for SDK3 for Avatars | 
**sdk3_worlds** | **str** | Download link for SDK3 for Worlds | 
**vcc** | **str** | Download link for the Creator Companion | 

## Example

```python
from vrchatapi.models.api_config_download_url_list import APIConfigDownloadURLList

# TODO update the JSON string below
json = "{}"
# create an instance of APIConfigDownloadURLList from a JSON string
api_config_download_url_list_instance = APIConfigDownloadURLList.from_json(json)
# print the JSON string representation of the object
print(APIConfigDownloadURLList.to_json())

# convert the object into a dict
api_config_download_url_list_dict = api_config_download_url_list_instance.to_dict()
# create an instance of APIConfigDownloadURLList from a dict
api_config_download_url_list_from_dict = APIConfigDownloadURLList.from_dict(api_config_download_url_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


