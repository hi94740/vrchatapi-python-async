# LimitedUserGroups


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**banner_id** | **str** |  | [optional] 
**banner_url** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**discriminator** | **str** |  | [optional] 
**group_id** | **str** |  | [optional] 
**icon_id** | **str** |  | [optional] 
**icon_url** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**is_representing** | **bool** |  | [optional] 
**last_post_created_at** | **datetime** |  | [optional] 
**last_post_read_at** | **datetime** |  | [optional] 
**member_count** | **int** |  | [optional] 
**member_visibility** | **str** |  | [optional] 
**mutual_group** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**owner_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 
**privacy** | **str** |  | [optional] 
**short_code** | **str** |  | [optional] 

## Example

```python
from vrchatapi.models.limited_user_groups import LimitedUserGroups

# TODO update the JSON string below
json = "{}"
# create an instance of LimitedUserGroups from a JSON string
limited_user_groups_instance = LimitedUserGroups.from_json(json)
# print the JSON string representation of the object
print(LimitedUserGroups.to_json())

# convert the object into a dict
limited_user_groups_dict = limited_user_groups_instance.to_dict()
# create an instance of LimitedUserGroups from a dict
limited_user_groups_from_dict = LimitedUserGroups.from_dict(limited_user_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


