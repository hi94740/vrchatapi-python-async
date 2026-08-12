# File



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**animation_style** | [**ImageAnimationStyle**](ImageAnimationStyle.md) |  | [optional] 
**extension** | **str** |  | 
**frames** | **int** | The number of frames for animated spritesheet images. | [optional] 
**frames_over_time** | **int** | The frames per second for animated spritesheet images. | [optional] 
**id** | **str** |  | 
**loop_style** | [**ImageLoopStyle**](ImageLoopStyle.md) |  | [optional] [default to ImageLoopStyle.LINEAR]
**mask_tag** | [**ImageMask**](ImageMask.md) |  | [optional] [default to ImageMask.SQUARE]
**mime_type** | [**MIMEType**](MIMEType.md) |  | [default to MIMEType.IMAGE_SLASH_JPEG]
**modified_thumbnail_file_name** | **str** |  | [optional] 
**name** | **str** |  | 
**owner_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**tags** | **List[str]** |   | 
**versions** | [**List[FileVersion]**](FileVersion.md) |   | 

## Example

```python
from vrchatapi.models.file import File

# TODO update the JSON string below
json = "{}"
# create an instance of File from a JSON string
file_instance = File.from_json(json)
# print the JSON string representation of the object
print(File.to_json())

# convert the object into a dict
file_dict = file_instance.to_dict()
# create an instance of File from a dict
file_from_dict = File.from_dict(file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


