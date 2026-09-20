# APIConfigEventShelfCampaign

A seasonal campaign a group event can be listed under.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**key** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from vrchatapi.models.api_config_event_shelf_campaign import APIConfigEventShelfCampaign

# TODO update the JSON string below
json = "{}"
# create an instance of APIConfigEventShelfCampaign from a JSON string
api_config_event_shelf_campaign_instance = APIConfigEventShelfCampaign.from_json(json)
# print the JSON string representation of the object
print(APIConfigEventShelfCampaign.to_json())

# convert the object into a dict
api_config_event_shelf_campaign_dict = api_config_event_shelf_campaign_instance.to_dict()
# create an instance of APIConfigEventShelfCampaign from a dict
api_config_event_shelf_campaign_from_dict = APIConfigEventShelfCampaign.from_dict(api_config_event_shelf_campaign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


