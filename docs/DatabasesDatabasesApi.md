# pterodactyl_client.DatabasesDatabasesApi

All URIs are relative to *https://example.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**__database_rotate_password_rotatepassword**](DatabasesDatabasesApi.md#__database_rotate_password_rotatepassword) | **POST** /client/servers/1a7ce997/databases/bEY4yAD5/rotate-password | [ /{database}/rotate-password ] Rotate password
[**delete__database_deletedatabase**](DatabasesDatabasesApi.md#delete__database_deletedatabase) | **DELETE** /client/servers/1a7ce997/databases/y9YVxO4V | [ /{database} ] Delete database
[**get__listdatabases**](DatabasesDatabasesApi.md#get__listdatabases) | **GET** /client/servers/1a7ce997/databases | [ / ] List databases
[**post__createdatabase**](DatabasesDatabasesApi.md#post__createdatabase) | **POST** /client/servers/1a7ce997/databases | [ / ] Create database


# **__database_rotate_password_rotatepassword**
> bool, date, datetime, dict, float, int, list, str, none_type __database_rotate_password_rotatepassword(accept)

[ /{database}/rotate-password ] Rotate password

Changes the password of a specified database  <!-- RESPONSE 200 --> {   \"object\": \"server_database\",   \"attributes\": {     \"id\": \"y9YVxO4V\",     \"host\": {       \"address\": \"127.0.0.1\",       \"port\": 3306     },     \"name\": \"s5_punishments\",     \"username\": \"u5_aeZqbGdCM9\",     \"connections_from\": \"%\",     \"max_connections\": 0,     \"relationships\": {       \"password\": {         \"object\": \"database_password\",         \"attributes\": {           \"password\": \"vnFKXlJ.p77!EiGR+Kd3muB.\"         }       }     }   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import databases_databases_api
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
    api_instance = databases_databases_api.DatabasesDatabasesApi(api_client)
    accept = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{database}/rotate-password ] Rotate password
        api_response = api_instance.__database_rotate_password_rotatepassword(accept)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling DatabasesDatabasesApi->__database_rotate_password_rotatepassword: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |

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

# **delete__database_deletedatabase**
> bool, date, datetime, dict, float, int, list, str, none_type delete__database_deletedatabase(accept, content_type)

[ /{database} ] Delete database

Deletes the specified database  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import databases_databases_api
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
    api_instance = databases_databases_api.DatabasesDatabasesApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{database} ] Delete database
        api_response = api_instance.delete__database_deletedatabase(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling DatabasesDatabasesApi->delete__database_deletedatabase: %s\n" % e)
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

# **get__listdatabases**
> bool, date, datetime, dict, float, int, list, str, none_type get__listdatabases(accept, content_type)

[ / ] List databases

Lists all databases on a server  ## Include parameters | Parameter | Description                         | |-----------|-------------------------------------| | password  | Includes the database user password |  <!-- RESPONSE 200 --> {   \"object\": \"list\",   \"data\": [     {       \"object\": \"server_database\",       \"attributes\": {         \"id\": \"bEY4yAD5\",         \"host\": {           \"address\": \"127.0.0.1\",           \"port\": 3306         },         \"name\": \"s5_perms\",         \"username\": \"u5_QsIAp1jhvS\",         \"connections_from\": \"%\",         \"max_connections\": 0       }     },     {       \"object\": \"server_database\",       \"attributes\": {         \"id\": \"E0A0Rw42\",         \"host\": {           \"address\": \"127.0.0.1\",           \"port\": 3306         },         \"name\": \"s5_coreprotect\",         \"username\": \"u5_2jtJx1nO1d\",         \"connections_from\": \"%\",         \"max_connections\": 0       }     }   ] } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import databases_databases_api
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
    api_instance = databases_databases_api.DatabasesDatabasesApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ / ] List databases
        api_response = api_instance.get__listdatabases(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling DatabasesDatabasesApi->get__listdatabases: %s\n" % e)
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

# **post__createdatabase**
> bool, date, datetime, dict, float, int, list, str, none_type post__createdatabase(accept, post_createdatabase_request)

[ / ] Create database

Creates a new database  <!-- RESPONSE 200 --> {   \"object\": \"server_database\",   \"attributes\": {     \"id\": \"y9YVxO4V\",     \"host\": {       \"address\": \"127.0.0.1\",       \"port\": 3306     },     \"name\": \"s5_punishments\",     \"username\": \"u5_aeZqbGdCM9\",     \"connections_from\": \"%\",     \"max_connections\": 0,     \"relationships\": {       \"password\": {         \"object\": \"database_password\",         \"attributes\": {           \"password\": \"=lR2orDOcwfKkM=BXb.BVF.C\"         }       }     }   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import databases_databases_api
from pterodactyl_client.model.post_createdatabase_request import PostCreatedatabaseRequest
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
    api_instance = databases_databases_api.DatabasesDatabasesApi(api_client)
    accept = "application/json" # str | 
    post_createdatabase_request = PostCreatedatabaseRequest(None) # PostCreatedatabaseRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ / ] Create database
        api_response = api_instance.post__createdatabase(accept, post_createdatabase_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling DatabasesDatabasesApi->post__createdatabase: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **post_createdatabase_request** | [**PostCreatedatabaseRequest**](PostCreatedatabaseRequest.md)|  |

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

