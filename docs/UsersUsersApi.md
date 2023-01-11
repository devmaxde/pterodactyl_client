# pterodactyl_client.UsersUsersApi

All URIs are relative to *https://example.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**__createuser**](UsersUsersApi.md#__createuser) | **POST** /application/users | [ / ] Create user
[**__listusers**](UsersUsersApi.md#__listusers) | **GET** /application/users | [ / ] List users


# **__createuser**
> bool, date, datetime, dict, float, int, list, str, none_type __createuser(accept, createuser_request)

[ / ] Create user

Creates a new user  <!-- RESPONSE 201 --> {   \"object\": \"user\",   \"attributes\": {     \"id\": 9,     \"external_id\": null,     \"uuid\": \"dac03ece-fd51-4e4b-bd4f-a79e3b2794f9\",     \"username\": \"exampleuser\",     \"email\": \"example10@example.com\",     \"first_name\": \"Example\",     \"last_name\": \"User\",     \"language\": \"en\",     \"root_admin\": false,     \"2fa\": false,     \"created_at\": \"2020-10-29T01:25:12+00:00\",     \"updated_at\": \"2020-10-29T01:25:12+00:00\"   },   \"meta\": {     \"resource\": \"https://pterodactyl.file.properties/api/application/users/9\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import users_users_api
from pterodactyl_client.model.createuser_request import CreateuserRequest
from pprint import pprint
# Defining the host is optional and defaults to https://example.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = pterodactyl_client.Configuration(
    host = "https://example.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = pterodactyl_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pterodactyl_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_users_api.UsersUsersApi(api_client)
    accept = "application/json" # str | 
    createuser_request = CreateuserRequest(None) # CreateuserRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ / ] Create user
        api_response = api_instance.__createuser(accept, createuser_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling UsersUsersApi->__createuser: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **createuser_request** | [**CreateuserRequest**](CreateuserRequest.md)|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **__listusers**
> bool, date, datetime, dict, float, int, list, str, none_type __listusers(accept, content_type)

[ / ] List users

Retrieves all users  ## Available Include parameters | Parameter | Description                            | |-----------|----------------------------------------| | servers   | List of servers the user has access to |  ## Filters | Parameter   | |-------------| | email       | | uuid        | | username    | | external_id |  ## Sort by | Parameter   | |-------------| | id          | | uuid        |  <!-- RESPONSE 200 --> {   \"object\": \"list\",   \"data\": [     {       \"object\": \"user\",       \"attributes\": {         \"id\": 1,         \"external_id\": \"RemoteId1\",         \"uuid\": \"4de5a357-ed95-426b-aec1-8c328cfe9751\",         \"username\": \"admin\",         \"email\": \"example@example.com\",         \"first_name\": \"Admin\",         \"last_name\": \"User\",         \"language\": \"en\",         \"root_admin\": true,         \"2fa\": false,         \"created_at\": \"2019-12-22T04:43:29+00:00\",         \"updated_at\": \"2020-07-13T13:10:23+00:00\"       }     },     {       \"object\": \"user\",       \"attributes\": {         \"id\": 2,         \"external_id\": null,         \"uuid\": \"73f233ca-99e0-47a9-bd46-efd3296d7ad9\",         \"username\": \"subuser1uxk\",         \"email\": \"subuser1@example.com\",         \"first_name\": \"Server\",         \"last_name\": \"Subuser\",         \"language\": \"en\",         \"root_admin\": false,         \"2fa\": false,         \"created_at\": \"2020-06-12T22:18:43+00:00\",         \"updated_at\": \"2020-06-12T22:18:43+00:00\"       }     },     {       \"object\": \"user\",       \"attributes\": {         \"id\": 3,         \"external_id\": null,         \"uuid\": \"60a7aec3-e17d-4aa9-abb3-56d944d204b4\",         \"username\": \"subuser2jvc\",         \"email\": \"subuser2@example.com\",         \"first_name\": \"Server\",         \"last_name\": \"Subuser\",         \"language\": \"en\",         \"root_admin\": false,         \"2fa\": false,         \"created_at\": \"2020-06-12T22:31:41+00:00\",         \"updated_at\": \"2020-06-12T22:31:41+00:00\"       }     },     {       \"object\": \"user\",       \"attributes\": {         \"id\": 4,         \"external_id\": null,         \"uuid\": \"a14e9c5f-9c7a-448f-9106-58e2b5286de6\",         \"username\": \"test\",         \"email\": \"example2@example.com\",         \"first_name\": \"Test\",         \"last_name\": \"Admin\",         \"language\": \"en\",         \"root_admin\": true,         \"2fa\": false,         \"created_at\": \"2020-06-14T00:34:50+00:00\",         \"updated_at\": \"2020-06-14T00:34:50+00:00\"       }     },     {       \"object\": \"user\",       \"attributes\": {         \"id\": 5,         \"external_id\": null,         \"uuid\": \"1287632d-9224-40c0-906e-f543423400bc\",         \"username\": \"subuser3bvo\",         \"email\": \"subuser3@example.com\",         \"first_name\": \"Server\",         \"last_name\": \"Subuser\",         \"language\": \"en\",         \"root_admin\": false,         \"2fa\": false,         \"created_at\": \"2020-07-13T13:27:46+00:00\",         \"updated_at\": \"2020-07-13T13:27:46+00:00\"       }     },     {       \"object\": \"user\",       \"attributes\": {         \"id\": 6,         \"external_id\": null,         \"uuid\": \"2fcb6f7e-342a-423a-93a4-6111a237c0c7\",         \"username\": \"geboc70057d6r\",         \"email\": \"geboc70057@djemail.net\",         \"first_name\": \"Server\",         \"last_name\": \"Subuser\",         \"language\": \"en\",         \"root_admin\": false,         \"2fa\": false,         \"created_at\": \"2020-07-13T13:36:44+00:00\",         \"updated_at\": \"2020-07-13T13:36:44+00:00\"       }     },     {       \"object\": \"user\",       \"attributes\": {         \"id\": 7,         \"external_id\": null,         \"uuid\": \"b20e4e11-550f-4c52-893d-94fc8bc46a06\",         \"username\": \"testidq\",         \"email\": \"test@example.com\",         \"first_name\": \"Server\",         \"last_name\": \"Subuser\",         \"language\": \"en\",         \"root_admin\": false,         \"2fa\": false,         \"created_at\": \"2020-07-19T12:48:38+00:00\",         \"updated_at\": \"2020-07-19T12:48:38+00:00\"       }     }   ],   \"meta\": {     \"pagination\": {       \"total\": 7,       \"count\": 7,       \"per_page\": 50,       \"current_page\": 1,       \"total_pages\": 1,       \"links\": {}     }   } } <!-- ENDRESPONSE -->  <!-- RESPONSE 200 --> // GET /api/application/users?filter%5Bemail%5D=dane%40daneeveritt.com {   \"object\": \"list\",   \"data\": [     {       \"object\": \"user\",       \"attributes\": {         \"id\": 27,         \"external_id\": null,         \"uuid\": \"18528bb9-8f60-45e2-adc6-f72611559fd7\",         \"username\": \"hodor7wm\",         \"email\": \"hodor@example.com\",         \"first_name\": \"Server\",         \"last_name\": \"Subuser\",         \"language\": \"en\",         \"root_admin\": false,         \"2fa\": false,         \"created_at\": \"2020-08-19T03:23:35+00:00\",         \"updated_at\": \"2020-08-19T03:23:35+00:00\"       }     },     {       \"object\": \"user\",       \"attributes\": {         \"id\": 26,         \"external_id\": null,         \"uuid\": \"b83673f6-3387-4a37-97cd-dd3a4f508343\",         \"username\": \"testfz0\",         \"email\": \"test@example.com\",         \"first_name\": \"Server\",         \"last_name\": \"Subuser\",         \"language\": \"en\",         \"root_admin\": false,         \"2fa\": false,         \"created_at\": \"2020-08-19T03:15:51+00:00\",         \"updated_at\": \"2020-08-19T03:15:51+00:00\"       }     }   ],   \"meta\": {     \"pagination\": {       \"total\": 2,       \"count\": 2,       \"per_page\": 100,       \"current_page\": 1,       \"total_pages\": 1,       \"links\": {}     }   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import users_users_api
from pprint import pprint
# Defining the host is optional and defaults to https://example.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = pterodactyl_client.Configuration(
    host = "https://example.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = pterodactyl_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with pterodactyl_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_users_api.UsersUsersApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ / ] List users
        api_response = api_instance.__listusers(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling UsersUsersApi->__listusers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **content_type** | **str**|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

