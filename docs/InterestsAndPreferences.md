# InterestsAndPreferences

Interests and preferences the current user has turned on. A key is present only while its value is `true`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anime** | **bool** |  | [optional] 
**art** | **bool** |  | [optional] 
**avatars** | **bool** |  | [optional] 
**big_group** | **bool** |  | [optional] 
**explore** | **bool** |  | [optional] 
**fantasy** | **bool** |  | [optional] 
**fashion** | **bool** |  | [optional] 
**find_avatars** | **bool** |  | [optional] 
**furries** | **bool** |  | [optional] 
**horror** | **bool** |  | [optional] 
**language_learning** | **bool** |  | [optional] 
**meet_people** | **bool** |  | [optional] 
**music** | **bool** |  | [optional] 
**mystery** | **bool** |  | [optional] 
**sci_fi** | **bool** |  | [optional] 
**small_group** | **bool** |  | [optional] 
**surprise** | **bool** |  | [optional] 

## Example

```python
from vrchatapi.models.interests_and_preferences import InterestsAndPreferences

# TODO update the JSON string below
json = "{}"
# create an instance of InterestsAndPreferences from a JSON string
interests_and_preferences_instance = InterestsAndPreferences.from_json(json)
# print the JSON string representation of the object
print(InterestsAndPreferences.to_json())

# convert the object into a dict
interests_and_preferences_dict = interests_and_preferences_instance.to_dict()
# create an instance of InterestsAndPreferences from a dict
interests_and_preferences_from_dict = InterestsAndPreferences.from_dict(interests_and_preferences_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


