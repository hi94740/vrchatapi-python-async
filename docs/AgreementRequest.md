# AgreementRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agreement_code** | [**AgreementCode**](AgreementCode.md) |  | [default to AgreementCode.CONTENT_DOT_COPYRIGHT_DOT_OWNED]
**agreement_fulltext** | **str** | The full text of the agreement (currently &#x60;By clicking OK, I certify that I have the necessary rights to upload this content and that it will not infringe on any third-party legal or intellectual property rights.&#x60;). | 
**content_id** | **str** | The id of the content being uploaded, such as a WorldID, AvatarID, or PropID. | 
**version** | **int** | The version of the agreement (currently &#x60;1&#x60;). | 

## Example

```python
from vrchatapi.models.agreement_request import AgreementRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgreementRequest from a JSON string
agreement_request_instance = AgreementRequest.from_json(json)
# print the JSON string representation of the object
print(AgreementRequest.to_json())

# convert the object into a dict
agreement_request_dict = agreement_request_instance.to_dict()
# create an instance of AgreementRequest from a dict
agreement_request_from_dict = AgreementRequest.from_dict(agreement_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


