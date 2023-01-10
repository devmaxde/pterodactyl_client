# pterodactyl_client.ServerDatabasesDatabaseManagementApi

All URIs are relative to *https://example.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**__createdatabase**](ServerDatabasesDatabaseManagementApi.md#__createdatabase) | **POST** /application/servers/5/databases | [ / ] Create database
[**__database_databasedetails**](ServerDatabasesDatabaseManagementApi.md#__database_databasedetails) | **GET** /application/servers/5/databases/1 | [ /{database} ] Database details
[**__database_deletedatabase**](ServerDatabasesDatabaseManagementApi.md#__database_deletedatabase) | **DELETE** /application/servers/5/databases/1 | [ /{database} ] Delete database
[**__database_reset_password_resetpassword**](ServerDatabasesDatabaseManagementApi.md#__database_reset_password_resetpassword) | **POST** /application/servers/5/databases/1/reset-password | [ /{database}/reset-password ] Reset password
[**__listdatabases**](ServerDatabasesDatabaseManagementApi.md#__listdatabases) | **GET** /application/servers/5/databases | [ / ] List databases


# **__createdatabase**
> bool, date, datetime, dict, float, int, list, str, none_type __createdatabase(accept, createdatabase_request)

[ / ] Create database

Creates a new database on the specified server  ## Fields | Name     | Required? | Type   | Description                                    | Rules | |----------|-----------|--------|------------------------------------------------|-------| | database | required  | string | Name for database                              |       | | remote   | database  | string | Permitted remotes that can access the database |       | | host     | database  | number | ID of the database host to use                 |       |  <!-- RESPONSE 200 --> {   \"object\": \"server_database\",   \"attributes\": {     \"id\": 6,     \"server\": 5,     \"host\": 4,     \"database\": \"s5_matches\",     \"username\": \"u5_LhG3aGWBtk\",     \"remote\": \"%\",     \"max_connections\": null,     \"created_at\": \"2020-11-04T21:00:42+00:00\",     \"updated_at\": \"2020-11-04T21:00:42+00:00\"   },   \"meta\": {     \"resource\": \"https://pterodactyl.file.properties/api/application/servers/5/databases/6\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import server_databases_database_management_api
from pterodactyl_client.model.createdatabase_request import CreatedatabaseRequest
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
    api_instance = server_databases_database_management_api.ServerDatabasesDatabaseManagementApi(api_client)
    accept = "application/json" # str | 
    createdatabase_request = CreatedatabaseRequest(None) # CreatedatabaseRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ / ] Create database
        api_response = api_instance.__createdatabase(accept, createdatabase_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServerDatabasesDatabaseManagementApi->__createdatabase: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **createdatabase_request** | [**CreatedatabaseRequest**](CreatedatabaseRequest.md)|  |

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

# **__database_databasedetails**
> bool, date, datetime, dict, float, int, list, str, none_type __database_databasedetails(accept, content_type)

[ /{database} ] Database details

Retrieves the specified database  ## Available include parameters | Parameter | Description                         | |-----------|-------------------------------------| | password  | Includes the database user password | | host      | Information about the database host |  <!-- RESPONSE 200 --> {   \"object\": \"server_database\",   \"attributes\": {     \"id\": 1,     \"server\": 5,     \"host\": 4,     \"database\": \"s5_perms\",     \"username\": \"u5_QsIAp1jhvS\",     \"remote\": \"%\",     \"max_connections\": 0,     \"created_at\": \"2020-06-12T23:00:13+01:00\",     \"updated_at\": \"2020-06-12T23:00:13+01:00\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import server_databases_database_management_api
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
    api_instance = server_databases_database_management_api.ServerDatabasesDatabaseManagementApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{database} ] Database details
        api_response = api_instance.__database_databasedetails(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServerDatabasesDatabaseManagementApi->__database_databasedetails: %s\n" % e)
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

# **__database_deletedatabase**
> bool, date, datetime, dict, float, int, list, str, none_type __database_deletedatabase(accept, content_type)

[ /{database} ] Delete database

Deletes the specified database  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import server_databases_database_management_api
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
    api_instance = server_databases_database_management_api.ServerDatabasesDatabaseManagementApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{database} ] Delete database
        api_response = api_instance.__database_deletedatabase(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServerDatabasesDatabaseManagementApi->__database_deletedatabase: %s\n" % e)
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

# **__database_reset_password_resetpassword**
> bool, date, datetime, dict, float, int, list, str, none_type __database_reset_password_resetpassword(accept, content_type)

[ /{database}/reset-password ] Reset password

Rotates the password of the database  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import server_databases_database_management_api
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
    api_instance = server_databases_database_management_api.ServerDatabasesDatabaseManagementApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{database}/reset-password ] Reset password
        api_response = api_instance.__database_reset_password_resetpassword(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServerDatabasesDatabaseManagementApi->__database_reset_password_resetpassword: %s\n" % e)
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

# **__listdatabases**
> bool, date, datetime, dict, float, int, list, str, none_type __listdatabases(accept, content_type)

[ / ] List databases

Retrieves all databases on a server  ## Available include parameters | Parameter | Description                         | |-----------|-------------------------------------| | password  | Includes the database user password | | host      | Information about the database host |  <!-- RESPONSE 200 --> {   \"object\": \"list\",   \"data\": [     {       \"object\": \"server_database\",       \"attributes\": {         \"id\": 1,         \"server\": 5,         \"host\": 4,         \"database\": \"s5_perms\",         \"username\": \"u5_QsIAp1jhvS\",         \"remote\": \"%\",         \"max_connections\": 0,         \"created_at\": \"2020-06-12T23:00:13+01:00\",         \"updated_at\": \"2020-06-12T23:00:13+01:00\",         \"relationships\": {           \"password\": {             \"object\": \"database_password\",             \"attributes\": {               \"password\": \".FjJ!5w945L3tuG4DrSxF+T@\"             }           },           \"host\": {             \"object\": \"database_host\",             \"attributes\": {               \"id\": 4,               \"name\": \"MariaDB\",               \"host\": \"127.0.0.1\",               \"port\": 3306,               \"username\": \"pterodactyluser\",               \"node\": 1,               \"created_at\": \"2020-06-12T22:59:25+01:00\",               \"updated_at\": \"2020-06-12T22:59:25+01:00\"             }           }         }       }     },     {       \"object\": \"server_database\",       \"attributes\": {         \"id\": 2,         \"server\": 5,         \"host\": 4,         \"database\": \"s5_coreprotect\",         \"username\": \"u5_2jtJx1nO1d\",         \"remote\": \"%\",         \"max_connections\": 0,         \"created_at\": \"2020-06-12T23:00:20+01:00\",         \"updated_at\": \"2020-06-12T23:00:20+01:00\",         \"relationships\": {           \"password\": {             \"object\": \"database_password\",             \"attributes\": {               \"password\": \"4=rv^0vHuOPSHCfj!tM1OlMC\"             }           },           \"host\": {             \"object\": \"database_host\",             \"attributes\": {               \"id\": 4,               \"name\": \"MariaDB\",               \"host\": \"127.0.0.1\",               \"port\": 3306,               \"username\": \"pterodactyluser\",               \"node\": 1,               \"created_at\": \"2020-06-12T22:59:25+01:00\",               \"updated_at\": \"2020-06-12T22:59:25+01:00\"             }           }         }       }     }   ] } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import server_databases_database_management_api
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
    api_instance = server_databases_database_management_api.ServerDatabasesDatabaseManagementApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 
    include = "password,host" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # [ / ] List databases
        api_response = api_instance.__listdatabases(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServerDatabasesDatabaseManagementApi->__listdatabases: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # [ / ] List databases
        api_response = api_instance.__listdatabases(accept, content_type, include=include)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServerDatabasesDatabaseManagementApi->__listdatabases: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **content_type** | **str**|  |
 **include** | **str**|  | [optional]

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

