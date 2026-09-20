# RouteNotImplemented

The body VRChat returns for a route it does not serve. The shape differs from every other error in this description: `error` is a string here, not an `Error` object with `message` and `status_code` inside it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | 
**status_code** | **int** |  | 

## Example

```python
from vrchatapi.models.route_not_implemented import RouteNotImplemented

# TODO update the JSON string below
json = "{}"
# create an instance of RouteNotImplemented from a JSON string
route_not_implemented_instance = RouteNotImplemented.from_json(json)
# print the JSON string representation of the object
print(RouteNotImplemented.to_json())

# convert the object into a dict
route_not_implemented_dict = route_not_implemented_instance.to_dict()
# create an instance of RouteNotImplemented from a dict
route_not_implemented_from_dict = RouteNotImplemented.from_dict(route_not_implemented_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


