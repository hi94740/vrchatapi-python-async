# FileAnalysis


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avatar_stats** | [**FileAnalysisAvatarStats**](FileAnalysisAvatarStats.md) |  | 
**created_at** | **datetime** |  | [optional] 
**encryption_key** | **str** |  | [optional] 
**file_size** | **int** |  | 
**performance_rating** | **str** |  | [optional] 
**success** | **bool** |  | 
**uncompressed_size** | **int** |  | 

## Example

```python
from vrchatapi.models.file_analysis import FileAnalysis

# TODO update the JSON string below
json = "{}"
# create an instance of FileAnalysis from a JSON string
file_analysis_instance = FileAnalysis.from_json(json)
# print the JSON string representation of the object
print(FileAnalysis.to_json())

# convert the object into a dict
file_analysis_dict = file_analysis_instance.to_dict()
# create an instance of FileAnalysis from a dict
file_analysis_from_dict = FileAnalysis.from_dict(file_analysis_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


