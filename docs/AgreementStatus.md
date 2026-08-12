# AgreementStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agreed** | **bool** | Whether the user has agreed for this content. | 
**agreement_code** | [**AgreementCode**](AgreementCode.md) |  | [default to AgreementCode.CONTENT_DOT_COPYRIGHT_DOT_OWNED]
**content_id** | **str** | The id of the content being uploaded, such as a WorldID, AvatarID, or PropID. | 
**user_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**version** | **int** | The version of the agreement. | 

## Example

```python
from vrchatapi.models.agreement_status import AgreementStatus

# TODO update the JSON string below
json = "{}"
# create an instance of AgreementStatus from a JSON string
agreement_status_instance = AgreementStatus.from_json(json)
# print the JSON string representation of the object
print(AgreementStatus.to_json())

# convert the object into a dict
agreement_status_dict = agreement_status_instance.to_dict()
# create an instance of AgreementStatus from a dict
agreement_status_from_dict = AgreementStatus.from_dict(agreement_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


