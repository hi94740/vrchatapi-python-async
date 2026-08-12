# CreateListingRequest

Observed create-listing payload fields. Additional fields may exist.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**description** | **str** |  | 
**display_name** | **str** |  | 
**image_id** | **str** |  | 
**listing_type** | [**ProductListingType**](ProductListingType.md) |  | [default to ProductListingType.SUBSCRIPTION]
**price_tokens** | **int** |  | 
**product_ids** | **List[str]** |  | 
**store_ids** | **List[str]** |  | 

## Example

```python
from vrchatapi.models.create_listing_request import CreateListingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateListingRequest from a JSON string
create_listing_request_instance = CreateListingRequest.from_json(json)
# print the JSON string representation of the object
print(CreateListingRequest.to_json())

# convert the object into a dict
create_listing_request_dict = create_listing_request_instance.to_dict()
# create an instance of CreateListingRequest from a dict
create_listing_request_from_dict = CreateListingRequest.from_dict(create_listing_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


