# DiscordDetails



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_name** | **str** |  | [optional] 
**id** | **str** | https://discord.com/developers/docs/reference#snowflakes | [optional] 

## Example

```python
from vrchatapi.models.discord_details import DiscordDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DiscordDetails from a JSON string
discord_details_instance = DiscordDetails.from_json(json)
# print the JSON string representation of the object
print(DiscordDetails.to_json())

# convert the object into a dict
discord_details_dict = discord_details_instance.to_dict()
# create an instance of DiscordDetails from a dict
discord_details_from_dict = DiscordDetails.from_dict(discord_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


