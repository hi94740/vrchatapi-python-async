# Agreement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agreement_code** | [**AgreementCode**](AgreementCode.md) |  | [default to AgreementCode.CONTENT_DOT_COPYRIGHT_DOT_OWNED]
**agreement_fulltext** | **str** | The full text of the agreement. | [optional] 
**content_id** | **str** | The id of the content being uploaded, such as a WorldID, AvatarID, or PropID. | 
**created** | **str** | When the agreement was created | 
**id** | **str** | The id of the agreement. | 
**tags** | **List[str]** |  | 
**user_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**version** | **int** | The version of the agreement. | 

## Example

```python
from vrchatapi.models.agreement import Agreement

# TODO update the JSON string below
json = "{}"
# create an instance of Agreement from a JSON string
agreement_instance = Agreement.from_json(json)
# print the JSON string representation of the object
print(Agreement.to_json())

# convert the object into a dict
agreement_dict = agreement_instance.to_dict()
# create an instance of Agreement from a dict
agreement_from_dict = Agreement.from_dict(agreement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


