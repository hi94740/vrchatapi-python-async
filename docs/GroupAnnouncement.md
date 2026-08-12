# GroupAnnouncement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 
**created_at** | **datetime** |  | [optional] 
**group_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**image_id** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from vrchatapi.models.group_announcement import GroupAnnouncement

# TODO update the JSON string below
json = "{}"
# create an instance of GroupAnnouncement from a JSON string
group_announcement_instance = GroupAnnouncement.from_json(json)
# print the JSON string representation of the object
print(GroupAnnouncement.to_json())

# convert the object into a dict
group_announcement_dict = group_announcement_instance.to_dict()
# create an instance of GroupAnnouncement from a dict
group_announcement_from_dict = GroupAnnouncement.from_dict(group_announcement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


