# CreateInstanceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age_gate** | **bool** |  | [optional] [default to False]
**calendar_entry_id** | **str** |  | [optional] 
**can_request_invite** | **bool** | Makes a private instance invite+. A friends instance is rejected. | [optional] [default to False]
**category_id** | **str** |  | [optional] 
**closed_at** | **datetime** | The time after which users won&#39;t be allowed to join the instance. This doesn&#39;t work for public instances. | [optional] 
**content_settings** | [**InstanceContentSettings**](InstanceContentSettings.md) |  | [optional] 
**description** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**group_access_type** | [**GroupAccessType**](GroupAccessType.md) |  | [optional] [default to GroupAccessType.MEMBERS]
**hard_close** | **bool** | Currently unused, but will eventually be a flag to set if the closing of the instance should kick people. | [optional] [default to False]
**instance_persistence_enabled** | **bool** |  | [optional] 
**invite_only** | **bool** |  | [optional] [default to False]
**owner_id** | **str** | A groupId if the instance type is \&quot;group\&quot;, null if instance type is public, or a userId otherwise | [optional] 
**player_persistence_enabled** | **bool** |  | [optional] 
**queue_enabled** | **bool** |  | [optional] [default to False]
**region** | [**InstanceRegion**](InstanceRegion.md) |  | [default to InstanceRegion.US]
**role_ids** | **List[str]** | Group roleIds that are allowed to join if the type is \&quot;group\&quot; and groupAccessType is \&quot;member\&quot; | [optional] 
**type** | [**InstanceType**](InstanceType.md) |  | 
**vibe_ids** | **List[str]** |  | [optional] 
**world_id** | **str** | WorldID be \&quot;offline\&quot; on User profiles if you are not friends with that user. | 

## Example

```python
from vrchatapi.models.create_instance_request import CreateInstanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInstanceRequest from a JSON string
create_instance_request_instance = CreateInstanceRequest.from_json(json)
# print the JSON string representation of the object
print(CreateInstanceRequest.to_json())

# convert the object into a dict
create_instance_request_dict = create_instance_request_instance.to_dict()
# create an instance of CreateInstanceRequest from a dict
create_instance_request_from_dict = CreateInstanceRequest.from_dict(create_instance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


