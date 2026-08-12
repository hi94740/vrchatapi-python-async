# CreateGroupAnnouncementRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_id** | **str** |  | [optional] 
**send_notification** | **bool** | Send notification to group members. | [optional] [default to False]
**text** | **str** | Announcement text | [optional] 
**title** | **str** | Announcement title | 

## Example

```python
from vrchatapi.models.create_group_announcement_request import CreateGroupAnnouncementRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGroupAnnouncementRequest from a JSON string
create_group_announcement_request_instance = CreateGroupAnnouncementRequest.from_json(json)
# print the JSON string representation of the object
print(CreateGroupAnnouncementRequest.to_json())

# convert the object into a dict
create_group_announcement_request_dict = create_group_announcement_request_instance.to_dict()
# create an instance of CreateGroupAnnouncementRequest from a dict
create_group_announcement_request_from_dict = CreateGroupAnnouncementRequest.from_dict(create_group_announcement_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


