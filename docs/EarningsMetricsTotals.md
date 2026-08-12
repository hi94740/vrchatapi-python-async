# EarningsMetricsTotals


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**otp_earnings** | **int** |  | 
**otp_purchase_count** | **int** |  | 
**subscriber_earnings** | **int** |  | 
**subscriber_months** | **int** |  | 
**total_earnings** | **int** |  | 

## Example

```python
from vrchatapi.models.earnings_metrics_totals import EarningsMetricsTotals

# TODO update the JSON string below
json = "{}"
# create an instance of EarningsMetricsTotals from a JSON string
earnings_metrics_totals_instance = EarningsMetricsTotals.from_json(json)
# print the JSON string representation of the object
print(EarningsMetricsTotals.to_json())

# convert the object into a dict
earnings_metrics_totals_dict = earnings_metrics_totals_instance.to_dict()
# create an instance of EarningsMetricsTotals from a dict
earnings_metrics_totals_from_dict = EarningsMetricsTotals.from_dict(earnings_metrics_totals_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


