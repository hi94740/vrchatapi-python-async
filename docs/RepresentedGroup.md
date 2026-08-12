# RepresentedGroup


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
**is_representing** | **bool** |  | [optional] 
**member_count** | **int** |  | [optional] 
**member_visibility** | [**GroupUserVisibility**](GroupUserVisibility.md) |  | [optional] 
**name** | **str** |  | [optional] 
**owner_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 
**privacy** | [**GroupPrivacy**](GroupPrivacy.md) |  | [optional] [default to GroupPrivacy.DEFAULT]
**short_code** | **str** |  | [optional] 

## Example

```python
from vrchatapi.models.represented_group import RepresentedGroup

# TODO update the JSON string below
json = "{}"
# create an instance of RepresentedGroup from a JSON string
represented_group_instance = RepresentedGroup.from_json(json)
# print the JSON string representation of the object
print(RepresentedGroup.to_json())

# convert the object into a dict
represented_group_dict = represented_group_instance.to_dict()
# create an instance of RepresentedGroup from a dict
represented_group_from_dict = RepresentedGroup.from_dict(represented_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


