# pterodactyl_client.UsersUsersApi

All URIs are relative to *https://example.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**__create_user1**](UsersUsersApi.md#__create_user1) | **POST** /client/servers/1a7ce997/users | [ / ] Create User1
[**__createuser**](UsersUsersApi.md#__createuser) | **POST** /application/users | [ / ] Create user
[**__external_external_id_userdetails**](UsersUsersApi.md#__external_external_id_userdetails) | **GET** /application/users/external/RemoteId1 | [ /external/{external_id} ] User details
[**__list_users1**](UsersUsersApi.md#__list_users1) | **GET** /client/servers/1a7ce997/users | [ / ] List Users1
[**__listusers**](UsersUsersApi.md#__listusers) | **GET** /application/users | [ / ] List users
[**__subuser_deleteuser**](UsersUsersApi.md#__subuser_deleteuser) | **DELETE** /client/servers/1a7ce997/users/60a7aec3-e17d-4aa9-abb3-56d944d204b4 | [ /{subuser} ] Delete user
[**__subuser_updateuser**](UsersUsersApi.md#__subuser_updateuser) | **POST** /client/servers/1a7ce997/users/60a7aec3-e17d-4aa9-abb3-56d944d204b4 | [ /{subuser} ] Update user
[**__subuser_userdetails**](UsersUsersApi.md#__subuser_userdetails) | **GET** /client/servers/1a7ce997/users/60a7aec3-e17d-4aa9-abb3-56d944d204b4 | [ /{subuser} ] User details
[**__updateuser**](UsersUsersApi.md#__updateuser) | **PATCH** /application/users/9 | [ / ] Update user
[**__user_deleteuser**](UsersUsersApi.md#__user_deleteuser) | **DELETE** /application/users/8 | [ /{user} ] Delete user
[**__user_userdetails**](UsersUsersApi.md#__user_userdetails) | **GET** /application/users/1 | [ /{user} ] User details


# **__create_user1**
> bool, date, datetime, dict, float, int, list, str, none_type __create_user1(accept, create_user1_request)

[ / ] Create User1

Adds a user to the server  # Fields | Name        | Required? | Type   | Description                        | Rules | |-------------|-----------|--------|------------------------------------|-------| | email       | required  | string | Email address of the user          |       | | permissions | required  | object | Permissions that user is permitted |       |  <!-- RESPONSE 200 --> {   \"object\": \"server_subuser\",   \"attributes\": {     \"uuid\": \"60a7aec3-e17d-4aa9-abb3-56d944d204b4\",     \"username\": \"subuser2jvc\",     \"email\": \"subuser2@example.com\",     \"image\": \"https://gravatar.com/avatar/3bb1c751a8b3488f4a4c70eddfe898d8\",     \"2fa_enabled\": false,     \"created_at\": \"2020-06-12T23:31:41+01:00\",     \"permissions\": [       \"control.console\",       \"control.start\",       \"websocket.connect\"     ]   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import users_users_api
from pterodactyl_client.model.create_user1_request import CreateUser1Request
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
    create_user1_request = CreateUser1Request(None) # CreateUser1Request | 

    # example passing only required values which don't have defaults set
    try:
        # [ / ] Create User1
        api_response = api_instance.__create_user1(accept, create_user1_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling UsersUsersApi->__create_user1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **create_user1_request** | [**CreateUser1Request**](CreateUser1Request.md)|  |

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

# **__external_external_id_userdetails**
> bool, date, datetime, dict, float, int, list, str, none_type __external_external_id_userdetails(accept, content_type)

[ /external/{external_id} ] User details

Retrieves the specified user by its external ID  ## Available include parameters | Parameter | Description                            | |-----------|----------------------------------------| | servers   | List of servers the user has access to |  <!-- RESPONSE 200 --> {   \"object\": \"user\",   \"attributes\": {     \"id\": 1,     \"external_id\": \"RemoteId1\",     \"uuid\": \"4de5a357-ed95-426b-aec1-8c328cfe9751\",     \"username\": \"admin\",     \"email\": \"example@example.com\",     \"first_name\": \"Admin\",     \"last_name\": \"User\",     \"language\": \"en\",     \"root_admin\": true,     \"2fa\": false,     \"created_at\": \"2019-12-22T04:43:29+00:00\",     \"updated_at\": \"2020-07-13T13:10:23+00:00\"   } } <!-- ENDRESPONSE -->

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
        # [ /external/{external_id} ] User details
        api_response = api_instance.__external_external_id_userdetails(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling UsersUsersApi->__external_external_id_userdetails: %s\n" % e)
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

# **__list_users1**
> bool, date, datetime, dict, float, int, list, str, none_type __list_users1(accept, content_type)

[ / ] List Users1

Lists all users added to the server, along with details about them and their permissions  <!-- RESPONSE 200 --> {   \"object\": \"list\",   \"data\": [     {       \"object\": \"server_subuser\",       \"attributes\": {         \"uuid\": \"73f233ca-99e0-47a9-bd46-efd3296d7ad9\",         \"username\": \"subuser1uxk\",         \"email\": \"subuser1@example.com\",         \"image\": \"https://gravatar.com/avatar/c0da5391b64449c1ecbfd4349184377c\",         \"2fa_enabled\": false,         \"created_at\": \"2020-06-12T23:18:43+01:00\",         \"permissions\": [           \"control.console\",           \"control.start\",           \"control.stop\",           \"control.restart\",           \"user.create\",           \"user.update\",           \"user.delete\",           \"user.read\",           \"file.create\",           \"file.read\",           \"file.update\",           \"file.delete\",           \"file.archive\",           \"file.sftp\",           \"backup.create\",           \"backup.read\",           \"backup.delete\",           \"backup.update\",           \"backup.download\",           \"allocation.update\",           \"startup.update\",           \"startup.read\",           \"database.create\",           \"database.read\",           \"database.update\",           \"database.delete\",           \"database.view_password\",           \"schedule.create\",           \"schedule.read\",           \"schedule.update\",           \"settings.rename\",           \"schedule.delete\",           \"settings.reinstall\",           \"websocket.connect\"         ]       }     },     {       \"object\": \"server_subuser\",       \"attributes\": {         \"uuid\": \"60a7aec3-e17d-4aa9-abb3-56d944d204b4\",         \"username\": \"subuser2jvc\",         \"email\": \"subuser2@example.com\",         \"image\": \"https://gravatar.com/avatar/3bb1c751a8b3488f4a4c70eddfe898d8\",         \"2fa_enabled\": false,         \"created_at\": \"2020-06-12T23:31:41+01:00\",         \"permissions\": [           \"control.console\",           \"control.start\",           \"websocket.connect\"         ]       }     },     {       \"object\": \"server_subuser\",       \"attributes\": {         \"uuid\": \"1287632d-9224-40c0-906e-f543423400bc\",         \"username\": \"subuser3bvo\",         \"email\": \"subuser3@example.com\",         \"image\": \"https://gravatar.com/avatar/8b28d32aaa64a1564450d16f71a81f65\",         \"2fa_enabled\": false,         \"created_at\": \"2020-07-13T14:27:46+01:00\",         \"permissions\": [           \"control.console\",           \"control.start\",           \"websocket.connect\"         ]       }     },     {       \"object\": \"server_subuser\",       \"attributes\": {         \"uuid\": \"2fcb6f7e-342a-423a-93a4-6111a237c0c7\",         \"username\": \"geboc70057d6r\",         \"email\": \"geboc70057@djemail.net\",         \"image\": \"https://gravatar.com/avatar/354d25d88e2c73b9f8d8e9bb8f1bf15e\",         \"2fa_enabled\": false,         \"created_at\": \"2020-07-13T14:36:44+01:00\",         \"permissions\": [           \"control.console\",           \"control.start\",           \"websocket.connect\"         ]       }     },     {       \"object\": \"server_subuser\",       \"attributes\": {         \"uuid\": \"b20e4e11-550f-4c52-893d-94fc8bc46a06\",         \"username\": \"testidq\",         \"email\": \"test@example.com\",         \"image\": \"https://gravatar.com/avatar/55502f40dc8b7c769880b10874abc9d0\",         \"2fa_enabled\": false,         \"created_at\": \"2020-07-19T13:48:38+01:00\",         \"permissions\": [           \"control.*\",           \"websocket.connect\"         ]       }     }   ] } <!-- ENDRESPONSE -->

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
        # [ / ] List Users1
        api_response = api_instance.__list_users1(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling UsersUsersApi->__list_users1: %s\n" % e)
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

# **__subuser_deleteuser**
> bool, date, datetime, dict, float, int, list, str, none_type __subuser_deleteuser(accept, content_type)

[ /{subuser} ] Delete user

Removes the specified user from the server  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

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
        # [ /{subuser} ] Delete user
        api_response = api_instance.__subuser_deleteuser(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling UsersUsersApi->__subuser_deleteuser: %s\n" % e)
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

# **__subuser_updateuser**
> bool, date, datetime, dict, float, int, list, str, none_type __subuser_updateuser(accept, subuser_updateuser_request)

[ /{subuser} ] Update user

Updates the specified user  # Fields | Name        | Required? | Type   | Description                        | Rules | |-------------|-----------|--------|------------------------------------|-------| | permissions | required  | object | Permissions that user is permitted |       |  <!-- RESPONSE 200 --> {   \"object\": \"server_subuser\",   \"attributes\": {     \"uuid\": \"60a7aec3-e17d-4aa9-abb3-56d944d204b4\",     \"username\": \"subuser2jvc\",     \"email\": \"subuser2@example.com\",     \"image\": \"https://gravatar.com/avatar/3bb1c751a8b3488f4a4c70eddfe898d8\",     \"2fa_enabled\": false,     \"created_at\": \"2020-06-12T23:31:41+01:00\",     \"permissions\": [       \"control.console\",       \"control.start\",       \"websocket.connect\"     ]   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import users_users_api
from pterodactyl_client.model.subuser_updateuser_request import SubuserUpdateuserRequest
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
    subuser_updateuser_request = SubuserUpdateuserRequest(None) # SubuserUpdateuserRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{subuser} ] Update user
        api_response = api_instance.__subuser_updateuser(accept, subuser_updateuser_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling UsersUsersApi->__subuser_updateuser: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **subuser_updateuser_request** | [**SubuserUpdateuserRequest**](SubuserUpdateuserRequest.md)|  |

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

# **__subuser_userdetails**
> bool, date, datetime, dict, float, int, list, str, none_type __subuser_userdetails(accept, content_type)

[ /{subuser} ] User details

Retrieves information about a specific user  <!-- RESPONSE 200 --> {   \"object\": \"server_subuser\",   \"attributes\": {     \"uuid\": \"60a7aec3-e17d-4aa9-abb3-56d944d204b4\",     \"username\": \"subuser2jvc\",     \"email\": \"subuser2@example.com\",     \"image\": \"https://gravatar.com/avatar/3bb1c751a8b3488f4a4c70eddfe898d8\",     \"2fa_enabled\": false,     \"created_at\": \"2020-06-12T23:31:41+01:00\",     \"permissions\": [       \"control.console\",       \"control.start\",       \"websocket.connect\"     ]   } } <!-- ENDRESPONSE -->

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
        # [ /{subuser} ] User details
        api_response = api_instance.__subuser_userdetails(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling UsersUsersApi->__subuser_userdetails: %s\n" % e)
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

# **__updateuser**
> bool, date, datetime, dict, float, int, list, str, none_type __updateuser(accept, updateuser_request)

[ / ] Update user

Updates the user information  <!-- RESPONSE 200 --> {   \"object\": \"user\",   \"attributes\": {     \"id\": 9,     \"external_id\": null,     \"uuid\": \"dac03ece-fd51-4e4b-bd4f-a79e3b2794f9\",     \"username\": \"exampleuser\",     \"email\": \"example10@example.com\",     \"first_name\": \"Example\",     \"last_name\": \"User\",     \"language\": \"en\",     \"root_admin\": false,     \"2fa\": false,     \"created_at\": \"2020-10-29T01:25:12+00:00\",     \"updated_at\": \"2020-10-29T01:28:29+00:00\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import users_users_api
from pterodactyl_client.model.updateuser_request import UpdateuserRequest
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
    updateuser_request = UpdateuserRequest(None) # UpdateuserRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ / ] Update user
        api_response = api_instance.__updateuser(accept, updateuser_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling UsersUsersApi->__updateuser: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **updateuser_request** | [**UpdateuserRequest**](UpdateuserRequest.md)|  |

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

# **__user_deleteuser**
> bool, date, datetime, dict, float, int, list, str, none_type __user_deleteuser(accept, content_type)

[ /{user} ] Delete user

Deletes the specified user  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

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
        # [ /{user} ] Delete user
        api_response = api_instance.__user_deleteuser(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling UsersUsersApi->__user_deleteuser: %s\n" % e)
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

# **__user_userdetails**
> bool, date, datetime, dict, float, int, list, str, none_type __user_userdetails(accept, content_type)

[ /{user} ] User details

Retrieves the specified user  ## Available include parameters | Parameter | Description                            | |-----------|----------------------------------------| | servers   | List of servers the user has access to |  <!-- RESPONSE 200 --> {   \"object\": \"user\",   \"attributes\": {     \"id\": 1,     \"external_id\": \"RemoteId1\",     \"uuid\": \"4de5a357-ed95-426b-aec1-8c328cfe9751\",     \"username\": \"admin\",     \"email\": \"example@example.com\",     \"first_name\": \"Admin\",     \"last_name\": \"User\",     \"language\": \"en\",     \"root_admin\": true,     \"2fa\": false,     \"created_at\": \"2019-12-22T04:43:29+00:00\",     \"updated_at\": \"2020-07-13T13:10:23+00:00\"   } } <!-- ENDRESPONSE -->

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
        # [ /{user} ] User details
        api_response = api_instance.__user_userdetails(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling UsersUsersApi->__user_userdetails: %s\n" % e)
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

