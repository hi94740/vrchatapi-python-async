# LimitedInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [default to True]
**capacity** | **int** |  | 
**category_id** | **str** |  | 
**creation_languages** | **List[object]** |  | 
**description** | **str** |  | 
**disabled_prop_abilities** | **List[object]** |  | 
**display_name** | **str** |  | 
**display_vibe_id** | **str** |  | 
**dominant_language** | **str** |  | 
**full** | **bool** |  | [default to False]
**group_access_type** | [**GroupAccessType**](GroupAccessType.md) |  | [optional] [default to GroupAccessType.MEMBERS]
**id** | **str** | InstanceID can be \&quot;offline\&quot; on User profiles if you are not friends with that user and \&quot;private\&quot; if you are friends and user is in private instance. | 
**instance_id** | **str** | InstanceID can be \&quot;offline\&quot; on User profiles if you are not friends with that user and \&quot;private\&quot; if you are friends and user is in private instance. | 
**language_ratio** | **Dict[str, object]** |  | 
**languages** | **List[str]** | The keys of languageRatio, ordered by their share of the instance. | 
**languages_iso639** | **List[str]** |  | 
**location** | **str** | Represents a unique location, consisting of a world identifier and an instance identifier, or \&quot;offline\&quot; if the user is not on your friends list. | 
**minimum_avatar_performance** | **str** |  | 
**n_users** | **int** |  | 
**owner_id** | **str** | A groupId if the instance type is \&quot;group\&quot;, null if instance type is public, or a userId otherwise | 
**permanent** | **bool** |  | [default to False]
**photon_region** | [**Region**](Region.md) |  | [default to Region.US]
**platforms** | [**InstancePlatforms**](InstancePlatforms.md) |  | 
**queue_enabled** | **bool** |  | 
**queue_size** | **int** |  | 
**recommended_capacity** | **int** |  | 
**region** | [**InstanceRegion**](InstanceRegion.md) |  | [default to InstanceRegion.US]
**role_restricted** | **bool** |  | [optional] 
**short_name** | **str** |  | 
**tags** | **List[str]** | The tags array on Instances usually contain the language tags of the people in the instance.  | 
**type** | [**InstanceType**](InstanceType.md) |  | 
**user_count** | **int** |  | 
**user_icons** | **List[str]** |  | 
**vibe_ids** | **List[str]** |  | 
**world** | [**World**](World.md) |  | 
**world_id** | **str** | WorldID be \&quot;offline\&quot; on User profiles if you are not friends with that user. | 

## Example

```python
from vrchatapi.models.limited_instance import LimitedInstance

# TODO update the JSON string below
json = "{}"
# create an instance of LimitedInstance from a JSON string
limited_instance_instance = LimitedInstance.from_json(json)
# print the JSON string representation of the object
print(LimitedInstance.to_json())

# convert the object into a dict
limited_instance_dict = limited_instance_instance.to_dict()
# create an instance of LimitedInstance from a dict
limited_instance_from_dict = LimitedInstance.from_dict(limited_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


