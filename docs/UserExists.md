# UserExists

Status object representing if a queried user by username or userId exists or not. This model is primarily used by the `/auth/exists` endpoint, which in turn is used during registration. Please see the documentation on that endpoint for more information on usage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name_ok** | **bool** | Is the username valid? | [optional] [default to False]
**user_exists** | **bool** | Status if a user exist with that username or userId. | [default to False]

## Example

```python
from vrchatapi.models.user_exists import UserExists

# TODO update the JSON string below
json = "{}"
# create an instance of UserExists from a JSON string
user_exists_instance = UserExists.from_json(json)
# print the JSON string representation of the object
print(UserExists.to_json())

# convert the object into a dict
user_exists_dict = user_exists_instance.to_dict()
# create an instance of UserExists from a dict
user_exists_from_dict = UserExists.from_dict(user_exists_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


