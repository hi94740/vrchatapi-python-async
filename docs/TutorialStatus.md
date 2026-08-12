# TutorialStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed** | **bool** |  | 
**completed_any_tutorial** | **bool** |  | 
**completed_tutorials** | **List[str]** |  | 
**tutorial_key** | **str** | The ID of a tutorial, in the format &#x60;{platform}:{tutorial}:{version}&#x60;. &#x60;undefined:undefined:v1&#x60; is used as a null-ish or sentinel value. | [default to 'undefined:undefined:v1']

## Example

```python
from vrchatapi.models.tutorial_status import TutorialStatus

# TODO update the JSON string below
json = "{}"
# create an instance of TutorialStatus from a JSON string
tutorial_status_instance = TutorialStatus.from_json(json)
# print the JSON string representation of the object
print(TutorialStatus.to_json())

# convert the object into a dict
tutorial_status_dict = tutorial_status_instance.to_dict()
# create an instance of TutorialStatus from a dict
tutorial_status_from_dict = TutorialStatus.from_dict(tutorial_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


