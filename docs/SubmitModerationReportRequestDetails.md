# SubmitModerationReportRequestDetails

Relevant details specific to the type of the report. `fileId` is for the image file attached to an inventory item, such as an emoji. `holderId` is for the user who owns an inventory item, such as a emoji.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **str** |  | [optional] 
**holder_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | [optional] 
**image_type** | **str** | Relevant detail for reports about image content, such as emoji. | [optional] 
**instance_age_gated** | **bool** | Relevant detail for reports taking place from within an instance. | [optional] 
**instance_type** | **str** | Relevant detail for reports taking place from within an instance. | [optional] 
**suggested_warnings** | [**List[ContentFilter]**](ContentFilter.md) | Relevant detail for reports about content that might not be tagged properly. | [optional] 
**user_in_same_instance** | **bool** | Relevant detail for reports involving another user in the same instance world. | [optional] 

## Example

```python
from vrchatapi.models.submit_moderation_report_request_details import SubmitModerationReportRequestDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitModerationReportRequestDetails from a JSON string
submit_moderation_report_request_details_instance = SubmitModerationReportRequestDetails.from_json(json)
# print the JSON string representation of the object
print(SubmitModerationReportRequestDetails.to_json())

# convert the object into a dict
submit_moderation_report_request_details_dict = submit_moderation_report_request_details_instance.to_dict()
# create an instance of SubmitModerationReportRequestDetails from a dict
submit_moderation_report_request_details_from_dict = SubmitModerationReportRequestDetails.from_dict(submit_moderation_report_request_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


