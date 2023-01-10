# pterodactyl_client.DatabasesApi

All URIs are relative to *http://example.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_client_servers_server_id_databases_database_id_delete**](DatabasesApi.md#api_client_servers_server_id_databases_database_id_delete) | **DELETE** /api/client/servers/{server_id}/databases/{database_id} | 
[**api_client_servers_server_id_databases_get**](DatabasesApi.md#api_client_servers_server_id_databases_get) | **GET** /api/client/servers/{server_id}/databases | 
[**api_client_servers_server_id_databases_post**](DatabasesApi.md#api_client_servers_server_id_databases_post) | **POST** /api/client/servers/{server_id}/databases | 


# **api_client_servers_server_id_databases_database_id_delete**
> api_client_servers_server_id_databases_database_id_delete(server_id, database_id)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import databases_api
from pprint import pprint
# Defining the host is optional and defaults to http://example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pterodactyl_client.Configuration(
    host = "http://example.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with pterodactyl_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databases_api.DatabasesApi(api_client)
    server_id = "server_id_example" # str | 
    database_id = "database_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_databases_database_id_delete(server_id, database_id)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling DatabasesApi->api_client_servers_server_id_databases_database_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  |
 **database_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_client_servers_server_id_databases_get**
> api_client_servers_server_id_databases_get(server_id)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import databases_api
from pprint import pprint
# Defining the host is optional and defaults to http://example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pterodactyl_client.Configuration(
    host = "http://example.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with pterodactyl_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databases_api.DatabasesApi(api_client)
    server_id = "server_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_databases_get(server_id)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling DatabasesApi->api_client_servers_server_id_databases_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_client_servers_server_id_databases_post**
> api_client_servers_server_id_databases_post(server_id, api_client_servers_server_id_databases_get_request)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import databases_api
from pterodactyl_client.model.api_client_servers_server_id_databases_get_request import ApiClientServersServerIdDatabasesGetRequest
from pprint import pprint
# Defining the host is optional and defaults to http://example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pterodactyl_client.Configuration(
    host = "http://example.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with pterodactyl_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = databases_api.DatabasesApi(api_client)
    server_id = "server_id_example" # str | 
    api_client_servers_server_id_databases_get_request = ApiClientServersServerIdDatabasesGetRequest(
        database="database_example",
        remote="remote_example",
    ) # ApiClientServersServerIdDatabasesGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_databases_post(server_id, api_client_servers_server_id_databases_get_request)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling DatabasesApi->api_client_servers_server_id_databases_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  |
 **api_client_servers_server_id_databases_get_request** | [**ApiClientServersServerIdDatabasesGetRequest**](ApiClientServersServerIdDatabasesGetRequest.md)|  |

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

