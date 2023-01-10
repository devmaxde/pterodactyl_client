# pterodactyl_client.ServersApi

All URIs are relative to *http://example.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_application_servers_external_remote_id1_get**](ServersApi.md#api_application_servers_external_remote_id1_get) | **GET** /api/application/servers/external/RemoteId1 | 
[**api_application_servers_get**](ServersApi.md#api_application_servers_get) | **GET** /api/application/servers | 
[**api_application_servers_id_delete**](ServersApi.md#api_application_servers_id_delete) | **DELETE** /api/application/servers/{id} | 
[**api_application_servers_id_force_delete**](ServersApi.md#api_application_servers_id_force_delete) | **DELETE** /api/application/servers/{id}/force | 
[**api_application_servers_id_get**](ServersApi.md#api_application_servers_id_get) | **GET** /api/application/servers/{id} | 
[**api_application_servers_id_reinstall_post**](ServersApi.md#api_application_servers_id_reinstall_post) | **POST** /api/application/servers/{id}/reinstall | 
[**api_application_servers_id_suspend_post**](ServersApi.md#api_application_servers_id_suspend_post) | **POST** /api/application/servers/{id}/suspend | 
[**api_application_servers_id_unsuspend_post**](ServersApi.md#api_application_servers_id_unsuspend_post) | **POST** /api/application/servers/{id}/unsuspend | 
[**api_application_servers_post**](ServersApi.md#api_application_servers_post) | **POST** /api/application/servers | 
[**api_client_servers_server_id_backups_backup_id_delete**](ServersApi.md#api_client_servers_server_id_backups_backup_id_delete) | **DELETE** /api/client/servers/{server_id}/backups/{backup_id} | 
[**api_client_servers_server_id_backups_backup_id_download_get**](ServersApi.md#api_client_servers_server_id_backups_backup_id_download_get) | **GET** /api/client/servers/{server_id}/backups/{backup_id}/download | 
[**api_client_servers_server_id_backups_backup_id_get**](ServersApi.md#api_client_servers_server_id_backups_backup_id_get) | **GET** /api/client/servers/{server_id}/backups/{backup_id} | 
[**api_client_servers_server_id_backups_get**](ServersApi.md#api_client_servers_server_id_backups_get) | **GET** /api/client/servers/{server_id}/backups | 
[**api_client_servers_server_id_backups_post**](ServersApi.md#api_client_servers_server_id_backups_post) | **POST** /api/client/servers/{server_id}/backups | 
[**api_client_servers_server_id_command_post**](ServersApi.md#api_client_servers_server_id_command_post) | **POST** /api/client/servers/{server_id}/command | 
[**api_client_servers_server_id_databases_database_id_delete**](ServersApi.md#api_client_servers_server_id_databases_database_id_delete) | **DELETE** /api/client/servers/{server_id}/databases/{database_id} | 
[**api_client_servers_server_id_databases_database_id_rotate_password_post**](ServersApi.md#api_client_servers_server_id_databases_database_id_rotate_password_post) | **POST** /api/client/servers/{server_id}/databases/{database_id}/rotate-password | 
[**api_client_servers_server_id_databases_get**](ServersApi.md#api_client_servers_server_id_databases_get) | **GET** /api/client/servers/{server_id}/databases | 
[**api_client_servers_server_id_databases_post**](ServersApi.md#api_client_servers_server_id_databases_post) | **POST** /api/client/servers/{server_id}/databases | 
[**api_client_servers_server_id_files_compress_post**](ServersApi.md#api_client_servers_server_id_files_compress_post) | **POST** /api/client/servers/{server_id}/files/compress | 
[**api_client_servers_server_id_files_contents_get**](ServersApi.md#api_client_servers_server_id_files_contents_get) | **GET** /api/client/servers/{server_id}/files/contents | 
[**api_client_servers_server_id_files_copy_post**](ServersApi.md#api_client_servers_server_id_files_copy_post) | **POST** /api/client/servers/{server_id}/files/copy | 
[**api_client_servers_server_id_files_create_folder_post**](ServersApi.md#api_client_servers_server_id_files_create_folder_post) | **POST** /api/client/servers/{server_id}/files/create-folder | 
[**api_client_servers_server_id_files_decompress_post**](ServersApi.md#api_client_servers_server_id_files_decompress_post) | **POST** /api/client/servers/{server_id}/files/decompress | 
[**api_client_servers_server_id_files_delete_post**](ServersApi.md#api_client_servers_server_id_files_delete_post) | **POST** /api/client/servers/{server_id}/files/delete | 
[**api_client_servers_server_id_files_download_get**](ServersApi.md#api_client_servers_server_id_files_download_get) | **GET** /api/client/servers/{server_id}/files/download | 
[**api_client_servers_server_id_files_list_get**](ServersApi.md#api_client_servers_server_id_files_list_get) | **GET** /api/client/servers/{server_id}/files/list | 
[**api_client_servers_server_id_files_rename_put**](ServersApi.md#api_client_servers_server_id_files_rename_put) | **PUT** /api/client/servers/{server_id}/files/rename | 
[**api_client_servers_server_id_files_upload_get**](ServersApi.md#api_client_servers_server_id_files_upload_get) | **GET** /api/client/servers/{server_id}/files/upload | 
[**api_client_servers_server_id_files_write_post**](ServersApi.md#api_client_servers_server_id_files_write_post) | **POST** /api/client/servers/{server_id}/files/write | 
[**api_client_servers_server_id_get**](ServersApi.md#api_client_servers_server_id_get) | **GET** /api/client/servers/{server_id} | 
[**api_client_servers_server_id_network_allocations_get**](ServersApi.md#api_client_servers_server_id_network_allocations_get) | **GET** /api/client/servers/{server_id}/network/allocations | 
[**api_client_servers_server_id_network_allocations_id_delete**](ServersApi.md#api_client_servers_server_id_network_allocations_id_delete) | **DELETE** /api/client/servers/{server_id}/network/allocations/{id} | 
[**api_client_servers_server_id_network_allocations_id_post**](ServersApi.md#api_client_servers_server_id_network_allocations_id_post) | **POST** /api/client/servers/{server_id}/network/allocations/{id} | 
[**api_client_servers_server_id_network_allocations_id_primary_post**](ServersApi.md#api_client_servers_server_id_network_allocations_id_primary_post) | **POST** /api/client/servers/{server_id}/network/allocations/{id}/primary | 
[**api_client_servers_server_id_network_allocations_post**](ServersApi.md#api_client_servers_server_id_network_allocations_post) | **POST** /api/client/servers/{server_id}/network/allocations | 
[**api_client_servers_server_id_power_post**](ServersApi.md#api_client_servers_server_id_power_post) | **POST** /api/client/servers/{server_id}/power | 
[**api_client_servers_server_id_resources_get**](ServersApi.md#api_client_servers_server_id_resources_get) | **GET** /api/client/servers/{server_id}/resources | 
[**api_client_servers_server_id_schedules_get**](ServersApi.md#api_client_servers_server_id_schedules_get) | **GET** /api/client/servers/{server_id}/schedules | 
[**api_client_servers_server_id_schedules_id_delete**](ServersApi.md#api_client_servers_server_id_schedules_id_delete) | **DELETE** /api/client/servers/{server_id}/schedules/{id} | 
[**api_client_servers_server_id_schedules_id_get**](ServersApi.md#api_client_servers_server_id_schedules_id_get) | **GET** /api/client/servers/{server_id}/schedules/{id} | 
[**api_client_servers_server_id_schedules_id_post**](ServersApi.md#api_client_servers_server_id_schedules_id_post) | **POST** /api/client/servers/{server_id}/schedules/{id} | 
[**api_client_servers_server_id_schedules_id_tasks_id1_delete**](ServersApi.md#api_client_servers_server_id_schedules_id_tasks_id1_delete) | **DELETE** /api/client/servers/{server_id}/schedules/{id}/tasks/{id1} | 
[**api_client_servers_server_id_schedules_id_tasks_id1_post**](ServersApi.md#api_client_servers_server_id_schedules_id_tasks_id1_post) | **POST** /api/client/servers/{server_id}/schedules/{id}/tasks/{id1} | 
[**api_client_servers_server_id_schedules_id_tasks_post**](ServersApi.md#api_client_servers_server_id_schedules_id_tasks_post) | **POST** /api/client/servers/{server_id}/schedules/{id}/tasks | 
[**api_client_servers_server_id_schedules_post**](ServersApi.md#api_client_servers_server_id_schedules_post) | **POST** /api/client/servers/{server_id}/schedules | 
[**api_client_servers_server_id_settings_reinstall_post**](ServersApi.md#api_client_servers_server_id_settings_reinstall_post) | **POST** /api/client/servers/{server_id}/settings/reinstall | 
[**api_client_servers_server_id_settings_rename_post**](ServersApi.md#api_client_servers_server_id_settings_rename_post) | **POST** /api/client/servers/{server_id}/settings/rename | 
[**api_client_servers_server_id_startup_get**](ServersApi.md#api_client_servers_server_id_startup_get) | **GET** /api/client/servers/{server_id}/startup | 
[**api_client_servers_server_id_startup_variable_put**](ServersApi.md#api_client_servers_server_id_startup_variable_put) | **PUT** /api/client/servers/{server_id}/startup/variable | 
[**api_client_servers_server_id_users_get**](ServersApi.md#api_client_servers_server_id_users_get) | **GET** /api/client/servers/{server_id}/users | 
[**api_client_servers_server_id_users_post**](ServersApi.md#api_client_servers_server_id_users_post) | **POST** /api/client/servers/{server_id}/users | 
[**api_client_servers_server_id_users_user_id_delete**](ServersApi.md#api_client_servers_server_id_users_user_id_delete) | **DELETE** /api/client/servers/{server_id}/users/{user_id} | 
[**api_client_servers_server_id_users_user_id_get**](ServersApi.md#api_client_servers_server_id_users_user_id_get) | **GET** /api/client/servers/{server_id}/users/{user_id} | 
[**api_client_servers_server_id_users_user_id_post**](ServersApi.md#api_client_servers_server_id_users_user_id_post) | **POST** /api/client/servers/{server_id}/users/{user_id} | 
[**api_client_servers_server_id_websocket_get**](ServersApi.md#api_client_servers_server_id_websocket_get) | **GET** /api/client/servers/{server_id}/websocket | 


# **api_application_servers_external_remote_id1_get**
> api_application_servers_external_remote_id1_get()



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.api_application_servers_external_remote_id1_get()
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_application_servers_external_remote_id1_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **api_application_servers_get**
> api_application_servers_get()



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.api_application_servers_get()
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_application_servers_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **api_application_servers_id_delete**
> api_application_servers_id_delete(id)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_application_servers_id_delete(id)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_application_servers_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

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

# **api_application_servers_id_force_delete**
> api_application_servers_id_force_delete(id)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_application_servers_id_force_delete(id)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_application_servers_id_force_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

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

# **api_application_servers_id_get**
> api_application_servers_id_get(id)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_application_servers_id_get(id)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_application_servers_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

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

# **api_application_servers_id_reinstall_post**
> api_application_servers_id_reinstall_post(id)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_application_servers_id_reinstall_post(id)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_application_servers_id_reinstall_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

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

# **api_application_servers_id_suspend_post**
> api_application_servers_id_suspend_post(id)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_application_servers_id_suspend_post(id)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_application_servers_id_suspend_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

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

# **api_application_servers_id_unsuspend_post**
> api_application_servers_id_unsuspend_post(id)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_application_servers_id_unsuspend_post(id)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_application_servers_id_unsuspend_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

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

# **api_application_servers_post**
> api_application_servers_post(api_application_servers_get_request)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
from pterodactyl_client.model.api_application_servers_get_request import ApiApplicationServersGetRequest
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
    api_instance = servers_api.ServersApi(api_client)
    api_application_servers_get_request = ApiApplicationServersGetRequest(
        name="name_example",
        user=3.14,
        egg=3.14,
        docker_image="docker_image_example",
        startup="startup_example",
        environment=ApiApplicationServersGetRequestEnvironment(
            bungee_version="bungee_version_example",
            server_jarfile="server_jarfile_example",
        ),
        limits=ApiApplicationServersGetRequestLimits(
            memory=3.14,
            swap=3.14,
            disk=3.14,
            io=3.14,
            cpu=3.14,
        ),
        feature_limits=ApiApplicationServersGetRequestFeatureLimits(
            databases=3.14,
            backups=3.14,
        ),
        allocation=ApiApplicationServersGetRequestAllocation(
            default=3.14,
        ),
    ) # ApiApplicationServersGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_application_servers_post(api_application_servers_get_request)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_application_servers_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_application_servers_get_request** | [**ApiApplicationServersGetRequest**](ApiApplicationServersGetRequest.md)|  |

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

# **api_client_servers_server_id_backups_backup_id_delete**
> api_client_servers_server_id_backups_backup_id_delete(server_id, backup_id)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    server_id = "server_id_example" # str | 
    backup_id = "backup_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_backups_backup_id_delete(server_id, backup_id)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_backups_backup_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  |
 **backup_id** | **str**|  |

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

# **api_client_servers_server_id_backups_backup_id_download_get**
> api_client_servers_server_id_backups_backup_id_download_get(server_id, backup_id)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    server_id = "server_id_example" # str | 
    backup_id = "backup_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_backups_backup_id_download_get(server_id, backup_id)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_backups_backup_id_download_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  |
 **backup_id** | **str**|  |

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

# **api_client_servers_server_id_backups_backup_id_get**
> api_client_servers_server_id_backups_backup_id_get(server_id, backup_id)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    server_id = "server_id_example" # str | 
    backup_id = "backup_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_backups_backup_id_get(server_id, backup_id)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_backups_backup_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  |
 **backup_id** | **str**|  |

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

# **api_client_servers_server_id_backups_get**
> api_client_servers_server_id_backups_get(server_id)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    server_id = "server_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_backups_get(server_id)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_backups_get: %s\n" % e)
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

# **api_client_servers_server_id_backups_post**
> api_client_servers_server_id_backups_post(server_id)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    server_id = "server_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_backups_post(server_id)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_backups_post: %s\n" % e)
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

# **api_client_servers_server_id_command_post**
> api_client_servers_server_id_command_post(server_id, api_client_servers_server_id_command_post_request)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
from pterodactyl_client.model.api_client_servers_server_id_command_post_request import ApiClientServersServerIdCommandPostRequest
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
    api_instance = servers_api.ServersApi(api_client)
    server_id = "server_id_example" # str | 
    api_client_servers_server_id_command_post_request = ApiClientServersServerIdCommandPostRequest(
        command="command_example",
    ) # ApiClientServersServerIdCommandPostRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_command_post(server_id, api_client_servers_server_id_command_post_request)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_command_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  |
 **api_client_servers_server_id_command_post_request** | [**ApiClientServersServerIdCommandPostRequest**](ApiClientServersServerIdCommandPostRequest.md)|  |

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

# **api_client_servers_server_id_databases_database_id_delete**
> api_client_servers_server_id_databases_database_id_delete(server_id, database_id)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    server_id = "server_id_example" # str | 
    database_id = "database_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_databases_database_id_delete(server_id, database_id)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_databases_database_id_delete: %s\n" % e)
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

# **api_client_servers_server_id_databases_database_id_rotate_password_post**
> api_client_servers_server_id_databases_database_id_rotate_password_post(server_id, database_id)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    server_id = "server_id_example" # str | 
    database_id = "database_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_databases_database_id_rotate_password_post(server_id, database_id)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_databases_database_id_rotate_password_post: %s\n" % e)
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
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    server_id = "server_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_databases_get(server_id)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_databases_get: %s\n" % e)
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
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    server_id = "server_id_example" # str | 
    api_client_servers_server_id_databases_get_request = ApiClientServersServerIdDatabasesGetRequest(
        database="database_example",
        remote="remote_example",
    ) # ApiClientServersServerIdDatabasesGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_databases_post(server_id, api_client_servers_server_id_databases_get_request)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_databases_post: %s\n" % e)
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

# **api_client_servers_server_id_files_compress_post**
> api_client_servers_server_id_files_compress_post(server_id, api_client_servers_server_id_files_compress_post_request)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
from pterodactyl_client.model.api_client_servers_server_id_files_compress_post_request import ApiClientServersServerIdFilesCompressPostRequest
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
    api_instance = servers_api.ServersApi(api_client)
    server_id = "server_id_example" # str | 
    api_client_servers_server_id_files_compress_post_request = ApiClientServersServerIdFilesCompressPostRequest(
        root="root_example",
        files=[
            "files_example",
        ],
    ) # ApiClientServersServerIdFilesCompressPostRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_files_compress_post(server_id, api_client_servers_server_id_files_compress_post_request)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_files_compress_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  |
 **api_client_servers_server_id_files_compress_post_request** | [**ApiClientServersServerIdFilesCompressPostRequest**](ApiClientServersServerIdFilesCompressPostRequest.md)|  |

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

# **api_client_servers_server_id_files_contents_get**
> api_client_servers_server_id_files_contents_get(file, server_id)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    file = "file_example" # str | 
    server_id = "server_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_files_contents_get(file, server_id)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_files_contents_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  |
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

# **api_client_servers_server_id_files_copy_post**
> api_client_servers_server_id_files_copy_post(server_id, api_client_servers_server_id_files_copy_post_request)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
from pterodactyl_client.model.api_client_servers_server_id_files_copy_post_request import ApiClientServersServerIdFilesCopyPostRequest
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
    api_instance = servers_api.ServersApi(api_client)
    server_id = "server_id_example" # str | 
    api_client_servers_server_id_files_copy_post_request = ApiClientServersServerIdFilesCopyPostRequest(
        location="location_example",
    ) # ApiClientServersServerIdFilesCopyPostRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_files_copy_post(server_id, api_client_servers_server_id_files_copy_post_request)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_files_copy_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  |
 **api_client_servers_server_id_files_copy_post_request** | [**ApiClientServersServerIdFilesCopyPostRequest**](ApiClientServersServerIdFilesCopyPostRequest.md)|  |

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

# **api_client_servers_server_id_files_create_folder_post**
> api_client_servers_server_id_files_create_folder_post(server_id, api_client_servers_server_id_files_create_folder_post_request)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
from pterodactyl_client.model.api_client_servers_server_id_files_create_folder_post_request import ApiClientServersServerIdFilesCreateFolderPostRequest
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
    api_instance = servers_api.ServersApi(api_client)
    server_id = "server_id_example" # str | 
    api_client_servers_server_id_files_create_folder_post_request = ApiClientServersServerIdFilesCreateFolderPostRequest(
        root="root_example",
        name="name_example",
    ) # ApiClientServersServerIdFilesCreateFolderPostRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_files_create_folder_post(server_id, api_client_servers_server_id_files_create_folder_post_request)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_files_create_folder_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  |
 **api_client_servers_server_id_files_create_folder_post_request** | [**ApiClientServersServerIdFilesCreateFolderPostRequest**](ApiClientServersServerIdFilesCreateFolderPostRequest.md)|  |

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

# **api_client_servers_server_id_files_decompress_post**
> api_client_servers_server_id_files_decompress_post(server_id, api_client_servers_server_id_files_decompress_post_request)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
from pterodactyl_client.model.api_client_servers_server_id_files_decompress_post_request import ApiClientServersServerIdFilesDecompressPostRequest
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
    api_instance = servers_api.ServersApi(api_client)
    server_id = "server_id_example" # str | 
    api_client_servers_server_id_files_decompress_post_request = ApiClientServersServerIdFilesDecompressPostRequest(
        root="root_example",
        file="file_example",
    ) # ApiClientServersServerIdFilesDecompressPostRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_files_decompress_post(server_id, api_client_servers_server_id_files_decompress_post_request)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_files_decompress_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  |
 **api_client_servers_server_id_files_decompress_post_request** | [**ApiClientServersServerIdFilesDecompressPostRequest**](ApiClientServersServerIdFilesDecompressPostRequest.md)|  |

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

# **api_client_servers_server_id_files_delete_post**
> api_client_servers_server_id_files_delete_post(server_id, api_client_servers_server_id_files_compress_post_request)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
from pterodactyl_client.model.api_client_servers_server_id_files_compress_post_request import ApiClientServersServerIdFilesCompressPostRequest
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
    api_instance = servers_api.ServersApi(api_client)
    server_id = "server_id_example" # str | 
    api_client_servers_server_id_files_compress_post_request = ApiClientServersServerIdFilesCompressPostRequest(
        root="root_example",
        files=[
            "files_example",
        ],
    ) # ApiClientServersServerIdFilesCompressPostRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_files_delete_post(server_id, api_client_servers_server_id_files_compress_post_request)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_files_delete_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  |
 **api_client_servers_server_id_files_compress_post_request** | [**ApiClientServersServerIdFilesCompressPostRequest**](ApiClientServersServerIdFilesCompressPostRequest.md)|  |

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

# **api_client_servers_server_id_files_download_get**
> api_client_servers_server_id_files_download_get(file, server_id)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    file = "file_example" # str | 
    server_id = "server_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_files_download_get(file, server_id)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_files_download_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  |
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

# **api_client_servers_server_id_files_list_get**
> api_client_servers_server_id_files_list_get(directory, server_id)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    directory = "directory_example" # str | 
    server_id = "server_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_files_list_get(directory, server_id)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_files_list_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **directory** | **str**|  |
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

# **api_client_servers_server_id_files_rename_put**
> api_client_servers_server_id_files_rename_put(server_id, api_client_servers_server_id_files_rename_put_request)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
from pterodactyl_client.model.api_client_servers_server_id_files_rename_put_request import ApiClientServersServerIdFilesRenamePutRequest
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
    api_instance = servers_api.ServersApi(api_client)
    server_id = "server_id_example" # str | 
    api_client_servers_server_id_files_rename_put_request = ApiClientServersServerIdFilesRenamePutRequest(
        root="root_example",
        files=[
            ApiClientServersServerIdFilesRenamePutRequestFilesInner(
                _from="_from_example",
                to="to_example",
            ),
        ],
    ) # ApiClientServersServerIdFilesRenamePutRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_files_rename_put(server_id, api_client_servers_server_id_files_rename_put_request)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_files_rename_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  |
 **api_client_servers_server_id_files_rename_put_request** | [**ApiClientServersServerIdFilesRenamePutRequest**](ApiClientServersServerIdFilesRenamePutRequest.md)|  |

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

# **api_client_servers_server_id_files_upload_get**
> api_client_servers_server_id_files_upload_get(server_id)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    server_id = "server_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_files_upload_get(server_id)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_files_upload_get: %s\n" % e)
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

# **api_client_servers_server_id_files_write_post**
> api_client_servers_server_id_files_write_post(file, server_id)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    file = "file_example" # str | 
    server_id = "server_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_files_write_post(file, server_id)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_files_write_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  |
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

# **api_client_servers_server_id_get**
> api_client_servers_server_id_get(server_id)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    server_id = "server_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_get(server_id)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_get: %s\n" % e)
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

# **api_client_servers_server_id_network_allocations_get**
> api_client_servers_server_id_network_allocations_get(server_id)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    server_id = "server_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_network_allocations_get(server_id)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_network_allocations_get: %s\n" % e)
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

# **api_client_servers_server_id_network_allocations_id_delete**
> api_client_servers_server_id_network_allocations_id_delete(id, server_id, body)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    id = "id_example" # str | 
    server_id = "server_id_example" # str | 
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_network_allocations_id_delete(id, server_id, body)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_network_allocations_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **server_id** | **str**|  |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  |

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

# **api_client_servers_server_id_network_allocations_id_post**
> api_client_servers_server_id_network_allocations_id_post(id, server_id, api_client_servers_server_id_network_allocations_id_delete_request)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
from pterodactyl_client.model.api_client_servers_server_id_network_allocations_id_delete_request import ApiClientServersServerIdNetworkAllocationsIdDeleteRequest
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
    api_instance = servers_api.ServersApi(api_client)
    id = "id_example" # str | 
    server_id = "server_id_example" # str | 
    api_client_servers_server_id_network_allocations_id_delete_request = ApiClientServersServerIdNetworkAllocationsIdDeleteRequest(
        notes="notes_example",
    ) # ApiClientServersServerIdNetworkAllocationsIdDeleteRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_network_allocations_id_post(id, server_id, api_client_servers_server_id_network_allocations_id_delete_request)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_network_allocations_id_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **server_id** | **str**|  |
 **api_client_servers_server_id_network_allocations_id_delete_request** | [**ApiClientServersServerIdNetworkAllocationsIdDeleteRequest**](ApiClientServersServerIdNetworkAllocationsIdDeleteRequest.md)|  |

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

# **api_client_servers_server_id_network_allocations_id_primary_post**
> api_client_servers_server_id_network_allocations_id_primary_post(id, server_id, body)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    id = "id_example" # str | 
    server_id = "server_id_example" # str | 
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_network_allocations_id_primary_post(id, server_id, body)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_network_allocations_id_primary_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **server_id** | **str**|  |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  |

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

# **api_client_servers_server_id_network_allocations_post**
> api_client_servers_server_id_network_allocations_post(server_id)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    server_id = "server_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_network_allocations_post(server_id)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_network_allocations_post: %s\n" % e)
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

# **api_client_servers_server_id_power_post**
> api_client_servers_server_id_power_post(server_id, api_client_servers_server_id_power_post_request)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
from pterodactyl_client.model.api_client_servers_server_id_power_post_request import ApiClientServersServerIdPowerPostRequest
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
    api_instance = servers_api.ServersApi(api_client)
    server_id = "server_id_example" # str | 
    api_client_servers_server_id_power_post_request = ApiClientServersServerIdPowerPostRequest(
        signal="signal_example",
    ) # ApiClientServersServerIdPowerPostRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_power_post(server_id, api_client_servers_server_id_power_post_request)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_power_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  |
 **api_client_servers_server_id_power_post_request** | [**ApiClientServersServerIdPowerPostRequest**](ApiClientServersServerIdPowerPostRequest.md)|  |

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

# **api_client_servers_server_id_resources_get**
> api_client_servers_server_id_resources_get(server_id)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    server_id = "server_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_resources_get(server_id)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_resources_get: %s\n" % e)
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

# **api_client_servers_server_id_schedules_get**
> api_client_servers_server_id_schedules_get(server_id)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    server_id = "server_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_schedules_get(server_id)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_schedules_get: %s\n" % e)
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

# **api_client_servers_server_id_schedules_id_delete**
> api_client_servers_server_id_schedules_id_delete(id, server_id)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    id = "id_example" # str | 
    server_id = "server_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_schedules_id_delete(id, server_id)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_schedules_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **api_client_servers_server_id_schedules_id_get**
> api_client_servers_server_id_schedules_id_get(id, server_id)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    id = "id_example" # str | 
    server_id = "server_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_schedules_id_get(id, server_id)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_schedules_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
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

# **api_client_servers_server_id_schedules_id_post**
> api_client_servers_server_id_schedules_id_post(id, server_id, api_client_servers_server_id_schedules_id_delete_request)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
from pterodactyl_client.model.api_client_servers_server_id_schedules_id_delete_request import ApiClientServersServerIdSchedulesIdDeleteRequest
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
    api_instance = servers_api.ServersApi(api_client)
    id = "id_example" # str | 
    server_id = "server_id_example" # str | 
    api_client_servers_server_id_schedules_id_delete_request = ApiClientServersServerIdSchedulesIdDeleteRequest(
        name="name_example",
        minute="minute_example",
        hour="hour_example",
        day_of_month="day_of_month_example",
        day_of_week="day_of_week_example",
    ) # ApiClientServersServerIdSchedulesIdDeleteRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_schedules_id_post(id, server_id, api_client_servers_server_id_schedules_id_delete_request)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_schedules_id_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **server_id** | **str**|  |
 **api_client_servers_server_id_schedules_id_delete_request** | [**ApiClientServersServerIdSchedulesIdDeleteRequest**](ApiClientServersServerIdSchedulesIdDeleteRequest.md)|  |

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

# **api_client_servers_server_id_schedules_id_tasks_id1_delete**
> api_client_servers_server_id_schedules_id_tasks_id1_delete(id, id1, server_id)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    id = "id_example" # str | 
    id1 = "id1_example" # str | 
    server_id = "server_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_schedules_id_tasks_id1_delete(id, id1, server_id)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_schedules_id_tasks_id1_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **id1** | **str**|  |
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

# **api_client_servers_server_id_schedules_id_tasks_id1_post**
> api_client_servers_server_id_schedules_id_tasks_id1_post(id, id1, server_id, api_client_servers_server_id_schedules_id_tasks_post_request)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
from pterodactyl_client.model.api_client_servers_server_id_schedules_id_tasks_post_request import ApiClientServersServerIdSchedulesIdTasksPostRequest
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
    api_instance = servers_api.ServersApi(api_client)
    id = "id_example" # str | 
    id1 = "id1_example" # str | 
    server_id = "server_id_example" # str | 
    api_client_servers_server_id_schedules_id_tasks_post_request = ApiClientServersServerIdSchedulesIdTasksPostRequest(
        action="action_example",
        payload="payload_example",
        time_offset="time_offset_example",
    ) # ApiClientServersServerIdSchedulesIdTasksPostRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_schedules_id_tasks_id1_post(id, id1, server_id, api_client_servers_server_id_schedules_id_tasks_post_request)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_schedules_id_tasks_id1_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **id1** | **str**|  |
 **server_id** | **str**|  |
 **api_client_servers_server_id_schedules_id_tasks_post_request** | [**ApiClientServersServerIdSchedulesIdTasksPostRequest**](ApiClientServersServerIdSchedulesIdTasksPostRequest.md)|  |

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

# **api_client_servers_server_id_schedules_id_tasks_post**
> api_client_servers_server_id_schedules_id_tasks_post(id, server_id, api_client_servers_server_id_schedules_id_tasks_post_request)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
from pterodactyl_client.model.api_client_servers_server_id_schedules_id_tasks_post_request import ApiClientServersServerIdSchedulesIdTasksPostRequest
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
    api_instance = servers_api.ServersApi(api_client)
    id = "id_example" # str | 
    server_id = "server_id_example" # str | 
    api_client_servers_server_id_schedules_id_tasks_post_request = ApiClientServersServerIdSchedulesIdTasksPostRequest(
        action="action_example",
        payload="payload_example",
        time_offset="time_offset_example",
    ) # ApiClientServersServerIdSchedulesIdTasksPostRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_schedules_id_tasks_post(id, server_id, api_client_servers_server_id_schedules_id_tasks_post_request)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_schedules_id_tasks_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **server_id** | **str**|  |
 **api_client_servers_server_id_schedules_id_tasks_post_request** | [**ApiClientServersServerIdSchedulesIdTasksPostRequest**](ApiClientServersServerIdSchedulesIdTasksPostRequest.md)|  |

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

# **api_client_servers_server_id_schedules_post**
> api_client_servers_server_id_schedules_post(server_id, api_client_servers_server_id_schedules_get_request)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
from pterodactyl_client.model.api_client_servers_server_id_schedules_get_request import ApiClientServersServerIdSchedulesGetRequest
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
    api_instance = servers_api.ServersApi(api_client)
    server_id = "server_id_example" # str | 
    api_client_servers_server_id_schedules_get_request = ApiClientServersServerIdSchedulesGetRequest(
        name="name_example",
        minute="minute_example",
        hour="hour_example",
        day_of_month="day_of_month_example",
        day_of_week="day_of_week_example",
        is_active=True,
    ) # ApiClientServersServerIdSchedulesGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_schedules_post(server_id, api_client_servers_server_id_schedules_get_request)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_schedules_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  |
 **api_client_servers_server_id_schedules_get_request** | [**ApiClientServersServerIdSchedulesGetRequest**](ApiClientServersServerIdSchedulesGetRequest.md)|  |

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

# **api_client_servers_server_id_settings_reinstall_post**
> api_client_servers_server_id_settings_reinstall_post(server_id, body)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    server_id = "server_id_example" # str | 
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_settings_reinstall_post(server_id, body)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_settings_reinstall_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  |

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

# **api_client_servers_server_id_settings_rename_post**
> api_client_servers_server_id_settings_rename_post(server_id, api_client_servers_server_id_settings_rename_post_request)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
from pterodactyl_client.model.api_client_servers_server_id_settings_rename_post_request import ApiClientServersServerIdSettingsRenamePostRequest
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
    api_instance = servers_api.ServersApi(api_client)
    server_id = "server_id_example" # str | 
    api_client_servers_server_id_settings_rename_post_request = ApiClientServersServerIdSettingsRenamePostRequest(
        name="name_example",
    ) # ApiClientServersServerIdSettingsRenamePostRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_settings_rename_post(server_id, api_client_servers_server_id_settings_rename_post_request)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_settings_rename_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  |
 **api_client_servers_server_id_settings_rename_post_request** | [**ApiClientServersServerIdSettingsRenamePostRequest**](ApiClientServersServerIdSettingsRenamePostRequest.md)|  |

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

# **api_client_servers_server_id_startup_get**
> api_client_servers_server_id_startup_get(server_id)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    server_id = "server_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_startup_get(server_id)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_startup_get: %s\n" % e)
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

# **api_client_servers_server_id_startup_variable_put**
> api_client_servers_server_id_startup_variable_put(server_id, api_client_servers_server_id_startup_variable_put_request)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
from pterodactyl_client.model.api_client_servers_server_id_startup_variable_put_request import ApiClientServersServerIdStartupVariablePutRequest
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
    api_instance = servers_api.ServersApi(api_client)
    server_id = "server_id_example" # str | 
    api_client_servers_server_id_startup_variable_put_request = ApiClientServersServerIdStartupVariablePutRequest(
        key="key_example",
        value="value_example",
    ) # ApiClientServersServerIdStartupVariablePutRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_startup_variable_put(server_id, api_client_servers_server_id_startup_variable_put_request)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_startup_variable_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  |
 **api_client_servers_server_id_startup_variable_put_request** | [**ApiClientServersServerIdStartupVariablePutRequest**](ApiClientServersServerIdStartupVariablePutRequest.md)|  |

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

# **api_client_servers_server_id_users_get**
> api_client_servers_server_id_users_get(server_id)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    server_id = "server_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_users_get(server_id)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_users_get: %s\n" % e)
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

# **api_client_servers_server_id_users_post**
> api_client_servers_server_id_users_post(server_id, api_client_servers_server_id_users_get_request)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
from pterodactyl_client.model.api_client_servers_server_id_users_get_request import ApiClientServersServerIdUsersGetRequest
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
    api_instance = servers_api.ServersApi(api_client)
    server_id = "server_id_example" # str | 
    api_client_servers_server_id_users_get_request = ApiClientServersServerIdUsersGetRequest(
        email="email_example",
        permissions=[
            "permissions_example",
        ],
    ) # ApiClientServersServerIdUsersGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_users_post(server_id, api_client_servers_server_id_users_get_request)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_users_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  |
 **api_client_servers_server_id_users_get_request** | [**ApiClientServersServerIdUsersGetRequest**](ApiClientServersServerIdUsersGetRequest.md)|  |

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

# **api_client_servers_server_id_users_user_id_delete**
> api_client_servers_server_id_users_user_id_delete(server_id, user_id)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    server_id = "server_id_example" # str | 
    user_id = "user_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_users_user_id_delete(server_id, user_id)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_users_user_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  |
 **user_id** | **str**|  |

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

# **api_client_servers_server_id_users_user_id_get**
> api_client_servers_server_id_users_user_id_get(server_id, user_id)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    server_id = "server_id_example" # str | 
    user_id = "user_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_users_user_id_get(server_id, user_id)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_users_user_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  |
 **user_id** | **str**|  |

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

# **api_client_servers_server_id_users_user_id_post**
> api_client_servers_server_id_users_user_id_post(server_id, user_id, api_client_servers_server_id_users_user_id_delete_request)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
from pterodactyl_client.model.api_client_servers_server_id_users_user_id_delete_request import ApiClientServersServerIdUsersUserIdDeleteRequest
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
    api_instance = servers_api.ServersApi(api_client)
    server_id = "server_id_example" # str | 
    user_id = "user_id_example" # str | 
    api_client_servers_server_id_users_user_id_delete_request = ApiClientServersServerIdUsersUserIdDeleteRequest(
        permissions=[
            "permissions_example",
        ],
    ) # ApiClientServersServerIdUsersUserIdDeleteRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_users_user_id_post(server_id, user_id, api_client_servers_server_id_users_user_id_delete_request)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_users_user_id_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**|  |
 **user_id** | **str**|  |
 **api_client_servers_server_id_users_user_id_delete_request** | [**ApiClientServersServerIdUsersUserIdDeleteRequest**](ApiClientServersServerIdUsersUserIdDeleteRequest.md)|  |

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

# **api_client_servers_server_id_websocket_get**
> api_client_servers_server_id_websocket_get(server_id)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    server_id = "server_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_servers_server_id_websocket_get(server_id)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->api_client_servers_server_id_websocket_get: %s\n" % e)
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

