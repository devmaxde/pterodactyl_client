# pterodactyl_client.DatabasesApi

All URIs are relative to *https://example.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**client_serversserver_id_databases_get**](DatabasesApi.md#client_serversserver_id_databases_get) | **GET** /client/servers/{server_id}/databases | [ / ] List databases
[**client_serversserver_id_databases_post**](DatabasesApi.md#client_serversserver_id_databases_post) | **POST** /client/servers/{server_id}/databases | [ / ] Create database
[**client_serversserver_id_databasesdatabase_id_delete**](DatabasesApi.md#client_serversserver_id_databasesdatabase_id_delete) | **DELETE** /client/servers/{server_id}/databases/{database_id} | [ /{database} ] Delete database
[**client_serversserver_id_databasesdatabase_id_rotate_password_post**](DatabasesApi.md#client_serversserver_id_databasesdatabase_id_rotate_password_post) | **POST** /client/servers/{server_id}/databases/{database_id}/rotate-password | [ /{database}/rotate-password ] Rotate password


# **client_serversserver_id_databases_get**
> bool, date, datetime, dict, float, int, list, str, none_type client_serversserver_id_databases_get(accept, content_type, server_id)

[ / ] List databases

Lists all databases on a server  ## Include parameters | Parameter | Description                         | |-----------|-------------------------------------| | password  | Includes the database user password |  <!-- RESPONSE 200 --> {   \"object\": \"list\",   \"data\": [     {       \"object\": \"server_database\",       \"attributes\": {         \"id\": \"bEY4yAD5\",         \"host\": {           \"address\": \"127.0.0.1\",           \"port\": 3306         },         \"name\": \"s5_perms\",         \"username\": \"u5_QsIAp1jhvS\",         \"connections_from\": \"%\",         \"max_connections\": 0       }     },     {       \"object\": \"server_database\",       \"attributes\": {         \"id\": \"E0A0Rw42\",         \"host\": {           \"address\": \"127.0.0.1\",           \"port\": 3306         },         \"name\": \"s5_coreprotect\",         \"username\": \"u5_2jtJx1nO1d\",         \"connections_from\": \"%\",         \"max_connections\": 0       }     }   ] } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import databases_api
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
    api_instance = databases_api.DatabasesApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 
    server_id = "server_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ / ] List databases
        api_response = api_instance.client_serversserver_id_databases_get(accept, content_type, server_id)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling DatabasesApi->client_serversserver_id_databases_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **content_type** | **str**|  |
 **server_id** | **str**|  |

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

# **client_serversserver_id_databases_post**
> bool, date, datetime, dict, float, int, list, str, none_type client_serversserver_id_databases_post(accept, server_id, client_servers_server_id_databases_post_request)

[ / ] Create database

Creates a new database  <!-- RESPONSE 200 --> {   \"object\": \"server_database\",   \"attributes\": {     \"id\": \"y9YVxO4V\",     \"host\": {       \"address\": \"127.0.0.1\",       \"port\": 3306     },     \"name\": \"s5_punishments\",     \"username\": \"u5_aeZqbGdCM9\",     \"connections_from\": \"%\",     \"max_connections\": 0,     \"relationships\": {       \"password\": {         \"object\": \"database_password\",         \"attributes\": {           \"password\": \"=lR2orDOcwfKkM=BXb.BVF.C\"         }       }     }   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import databases_api
from pterodactyl_client.model.client_servers_server_id_databases_post_request import ClientServersServerIdDatabasesPostRequest
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
    api_instance = databases_api.DatabasesApi(api_client)
    accept = "application/json" # str | 
    server_id = "server_id_example" # str | 
    client_servers_server_id_databases_post_request = ClientServersServerIdDatabasesPostRequest(None) # ClientServersServerIdDatabasesPostRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ / ] Create database
        api_response = api_instance.client_serversserver_id_databases_post(accept, server_id, client_servers_server_id_databases_post_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling DatabasesApi->client_serversserver_id_databases_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **server_id** | **str**|  |
 **client_servers_server_id_databases_post_request** | [**ClientServersServerIdDatabasesPostRequest**](ClientServersServerIdDatabasesPostRequest.md)|  |

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

# **client_serversserver_id_databasesdatabase_id_delete**
> bool, date, datetime, dict, float, int, list, str, none_type client_serversserver_id_databasesdatabase_id_delete(accept, content_type, server_id, database_id)

[ /{database} ] Delete database

Deletes the specified database  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import databases_api
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
    api_instance = databases_api.DatabasesApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 
    server_id = "server_id_example" # str | 
    database_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{database} ] Delete database
        api_response = api_instance.client_serversserver_id_databasesdatabase_id_delete(accept, content_type, server_id, database_id)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling DatabasesApi->client_serversserver_id_databasesdatabase_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **content_type** | **str**|  |
 **server_id** | **str**|  |
 **database_id** | **int**|  |

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

# **client_serversserver_id_databasesdatabase_id_rotate_password_post**
> bool, date, datetime, dict, float, int, list, str, none_type client_serversserver_id_databasesdatabase_id_rotate_password_post(accept, server_id, database_id)

[ /{database}/rotate-password ] Rotate password

Changes the password of a specified database  <!-- RESPONSE 200 --> {   \"object\": \"server_database\",   \"attributes\": {     \"id\": \"y9YVxO4V\",     \"host\": {       \"address\": \"127.0.0.1\",       \"port\": 3306     },     \"name\": \"s5_punishments\",     \"username\": \"u5_aeZqbGdCM9\",     \"connections_from\": \"%\",     \"max_connections\": 0,     \"relationships\": {       \"password\": {         \"object\": \"database_password\",         \"attributes\": {           \"password\": \"vnFKXlJ.p77!EiGR+Kd3muB.\"         }       }     }   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import databases_api
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
    api_instance = databases_api.DatabasesApi(api_client)
    accept = "application/json" # str | 
    server_id = "server_id_example" # str | 
    database_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{database}/rotate-password ] Rotate password
        api_response = api_instance.client_serversserver_id_databasesdatabase_id_rotate_password_post(accept, server_id, database_id)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling DatabasesApi->client_serversserver_id_databasesdatabase_id_rotate_password_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **server_id** | **str**|  |
 **database_id** | **int**|  |

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

