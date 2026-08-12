# Feedback


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commenter_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**commenter_name** | **str** |  | 
**content_author_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**content_author_name** | **str** |  | 
**content_id** | **str** |  | 
**content_name** | **str** |  | [optional] 
**content_type** | **str** |  | 
**content_version** | **int** |  | 
**description** | **str** |  | [optional] 
**id** | **str** |  | 
**reason** | **str** |  | 
**tags** | **List[str]** |  | 
**type** | **str** |  | 

## Example

```python
from vrchatapi.models.feedback import Feedback

# TODO update the JSON string below
json = "{}"
# create an instance of Feedback from a JSON string
feedback_instance = Feedback.from_json(json)
# print the JSON string representation of the object
print(Feedback.to_json())

# convert the object into a dict
feedback_dict = feedback_instance.to_dict()
# create an instance of Feedback from a dict
feedback_from_dict = Feedback.from_dict(feedback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


