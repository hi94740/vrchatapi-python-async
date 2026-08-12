# EarningsMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**breakdown** | **List[object]** |  | 
**seller_id** | **str** | A users unique ID, usually in the form of &#x60;usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469&#x60;. Legacy players can have old IDs in the form of &#x60;8JoV9XEdpo&#x60;. The ID can never be changed. | 
**totals** | [**EarningsMetricsTotals**](EarningsMetricsTotals.md) |  | 

## Example

```python
from vrchatapi.models.earnings_metrics import EarningsMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of EarningsMetrics from a JSON string
earnings_metrics_instance = EarningsMetrics.from_json(json)
# print the JSON string representation of the object
print(EarningsMetrics.to_json())

# convert the object into a dict
earnings_metrics_dict = earnings_metrics_instance.to_dict()
# create an instance of EarningsMetrics from a dict
earnings_metrics_from_dict = EarningsMetrics.from_dict(earnings_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


