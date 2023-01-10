# pterodactyl_client.ServerDatabaseApi

All URIs are relative to *http://example.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_application_servers_id_databases_get**](ServerDatabaseApi.md#api_application_servers_id_databases_get) | **GET** /api/application/servers/{id}/databases | 
[**api_application_servers_id_databases_id1_delete**](ServerDatabaseApi.md#api_application_servers_id_databases_id1_delete) | **DELETE** /api/application/servers/{id}/databases/{id1} | 
[**api_application_servers_id_databases_id1_get**](ServerDatabaseApi.md#api_application_servers_id_databases_id1_get) | **GET** /api/application/servers/{id}/databases/{id1} | 
[**api_application_servers_id_databases_id1_reset_password_post**](ServerDatabaseApi.md#api_application_servers_id_databases_id1_reset_password_post) | **POST** /api/application/servers/{id}/databases/{id1}/reset-password | 
[**api_application_servers_id_databases_post**](ServerDatabaseApi.md#api_application_servers_id_databases_post) | **POST** /api/application/servers/{id}/databases | 


# **api_application_servers_id_databases_get**
> api_application_servers_id_databases_get(id, include)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import server_database_api
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
    api_instance = server_database_api.ServerDatabaseApi(api_client)
    id = "id_example" # str | 
    include = "include_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_application_servers_id_databases_get(id, include)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServerDatabaseApi->api_application_servers_id_databases_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **include** | **str**|  |

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

# **api_application_servers_id_databases_id1_delete**
> api_application_servers_id_databases_id1_delete(id, id1)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import server_database_api
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
    api_instance = server_database_api.ServerDatabaseApi(api_client)
    id = "id_example" # str | 
    id1 = "id1_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_application_servers_id_databases_id1_delete(id, id1)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServerDatabaseApi->api_application_servers_id_databases_id1_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **id1** | **str**|  |

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

# **api_application_servers_id_databases_id1_get**
> api_application_servers_id_databases_id1_get(id, id1)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import server_database_api
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
    api_instance = server_database_api.ServerDatabaseApi(api_client)
    id = "id_example" # str | 
    id1 = "id1_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_application_servers_id_databases_id1_get(id, id1)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServerDatabaseApi->api_application_servers_id_databases_id1_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **id1** | **str**|  |

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

# **api_application_servers_id_databases_id1_reset_password_post**
> api_application_servers_id_databases_id1_reset_password_post(id, id1)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import server_database_api
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
    api_instance = server_database_api.ServerDatabaseApi(api_client)
    id = "id_example" # str | 
    id1 = "id1_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_application_servers_id_databases_id1_reset_password_post(id, id1)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServerDatabaseApi->api_application_servers_id_databases_id1_reset_password_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **id1** | **str**|  |

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

# **api_application_servers_id_databases_post**
> api_application_servers_id_databases_post(id, api_application_servers_id_databases_get_request)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import server_database_api
from pterodactyl_client.model.api_application_servers_id_databases_get_request import ApiApplicationServersIdDatabasesGetRequest
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
    api_instance = server_database_api.ServerDatabaseApi(api_client)
    id = "id_example" # str | 
    api_application_servers_id_databases_get_request = ApiApplicationServersIdDatabasesGetRequest(
        database="database_example",
        remote="remote_example",
        host=3.14,
    ) # ApiApplicationServersIdDatabasesGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_application_servers_id_databases_post(id, api_application_servers_id_databases_get_request)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServerDatabaseApi->api_application_servers_id_databases_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **api_application_servers_id_databases_get_request** | [**ApiApplicationServersIdDatabasesGetRequest**](ApiApplicationServersIdDatabasesGetRequest.md)|  |

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

