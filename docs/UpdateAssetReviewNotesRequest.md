# UpdateAssetReviewNotesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**review_notes** | **str** |  | 

## Example

```python
from vrchatapi.models.update_asset_review_notes_request import UpdateAssetReviewNotesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAssetReviewNotesRequest from a JSON string
update_asset_review_notes_request_instance = UpdateAssetReviewNotesRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAssetReviewNotesRequest.to_json())

# convert the object into a dict
update_asset_review_notes_request_dict = update_asset_review_notes_request_instance.to_dict()
# create an instance of UpdateAssetReviewNotesRequest from a dict
update_asset_review_notes_request_from_dict = UpdateAssetReviewNotesRequest.from_dict(update_asset_review_notes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


