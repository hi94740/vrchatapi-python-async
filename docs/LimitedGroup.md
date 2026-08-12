# LimitedGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**banner_id** | **str** |  | [optional] 
**banner_url** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**discriminator** | **str** |  | [optional] 
**galleries** | [**List[GroupGallery]**](GroupGallery.md) |   | [optional] 
**icon_id** | **str** |  | [optional] 
**icon_url** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**is_searchable** | **bool** |  | [optional] 
**member_count** | **int** |  | [optional] 
**membership_status** | [**GroupMemberStatus**](GroupMemberStatus.md) |  | [optional] [default to GroupMemberStatus.INACTIVE]
**name** | **str** |  | [optional] 
**owner_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 
**rules** | **str** |  | [optional] 
**short_code** | **str** |  | [optional] 
**tags** | **List[str]** |   | [optional] 

## Example

```python
from vrchatapi.models.limited_group import LimitedGroup

# TODO update the JSON string below
json = "{}"
# create an instance of LimitedGroup from a JSON string
limited_group_instance = LimitedGroup.from_json(json)
# print the JSON string representation of the object
print(LimitedGroup.to_json())

# convert the object into a dict
limited_group_dict = limited_group_instance.to_dict()
# create an instance of LimitedGroup from a dict
limited_group_from_dict = LimitedGroup.from_dict(limited_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


