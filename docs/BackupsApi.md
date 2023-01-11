# pterodactyl_client.BackupsApi

All URIs are relative to *https://example.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**client_serversserver_id_backups_get**](BackupsApi.md#client_serversserver_id_backups_get) | **GET** /client/servers/{server_id}/backups | [ / ] List backups
[**client_serversserver_id_backups_post**](BackupsApi.md#client_serversserver_id_backups_post) | **POST** /client/servers/{server_id}/backups | [ / ] Create backup
[**client_serversserver_id_backupsbackup_id_delete**](BackupsApi.md#client_serversserver_id_backupsbackup_id_delete) | **DELETE** /client/servers/{server_id}/backups/{backup_id} | [ /{backup} ] Delete backup
[**client_serversserver_id_backupsbackup_id_download_get**](BackupsApi.md#client_serversserver_id_backupsbackup_id_download_get) | **GET** /client/servers/{server_id}/backups/{backup_id}/download | [ /{backup}/download ] Download backup
[**client_serversserver_id_backupsbackup_id_get**](BackupsApi.md#client_serversserver_id_backupsbackup_id_get) | **GET** /client/servers/{server_id}/backups/{backup_id} | [ /{backup} ] Backup details


# **client_serversserver_id_backups_get**
> bool, date, datetime, dict, float, int, list, str, none_type client_serversserver_id_backups_get(accept, content_type, server_id)

[ / ] List backups

Retrieves a list of backups  <!-- RESPONSE 200 --> {   \"object\": \"list\",   \"data\": [     {       \"object\": \"backup\",       \"attributes\": {         \"uuid\": \"904df120-a66f-4375-a4ae-40eedbeae630\",         \"name\": \"Quick Backup\",         \"ignored_files\": [],         \"sha256_hash\": \"7c20d6a269b441a9dfd044e3f8ad13d77c09c83af8832d29ad603084a9a63726\",         \"bytes\": 114402862,         \"created_at\": \"2020-06-13T05:21:01+01:00\",         \"completed_at\": \"2020-06-13T05:21:04+01:00\"       }     },     {       \"object\": \"backup\",       \"attributes\": {         \"uuid\": \"63087048-eada-419c-ad72-803c1c949cac\",         \"name\": \"Backup at 2020-07-19 16:21:34\",         \"ignored_files\": [],         \"sha256_hash\": \"39bf93b9d8aee45316fa7ec8bbed0530904558851fa8e712452845c969873b16\",         \"bytes\": 114567250,         \"created_at\": \"2020-07-19T16:21:34+01:00\",         \"completed_at\": \"2020-07-19T16:21:35+01:00\"       }     }   ],   \"meta\": {     \"pagination\": {       \"total\": 2,       \"count\": 2,       \"per_page\": 20,       \"current_page\": 1,       \"total_pages\": 1,       \"links\": {}     }   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import backups_api
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
    api_instance = backups_api.BackupsApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 
    server_id = "server_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ / ] List backups
        api_response = api_instance.client_serversserver_id_backups_get(accept, content_type, server_id)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling BackupsApi->client_serversserver_id_backups_get: %s\n" % e)
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

# **client_serversserver_id_backups_post**
> bool, date, datetime, dict, float, int, list, str, none_type client_serversserver_id_backups_post(accept, content_type, server_id)

[ / ] Create backup

Creates a new backup  <!-- RESPONSE 200 --> {   \"object\": \"backup\",   \"attributes\": {     \"uuid\": \"63087048-eada-419c-ad72-803c1c949cac\",     \"name\": \"Backup at 2020-07-19 16:21:34\",     \"ignored_files\": [],     \"sha256_hash\": null,     \"bytes\": 0,     \"created_at\": \"2020-07-19T16:21:34+01:00\",     \"completed_at\": null   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import backups_api
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
    api_instance = backups_api.BackupsApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 
    server_id = "server_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ / ] Create backup
        api_response = api_instance.client_serversserver_id_backups_post(accept, content_type, server_id)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling BackupsApi->client_serversserver_id_backups_post: %s\n" % e)
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

# **client_serversserver_id_backupsbackup_id_delete**
> bool, date, datetime, dict, float, int, list, str, none_type client_serversserver_id_backupsbackup_id_delete(accept, content_type, server_id, backup_id)

[ /{backup} ] Delete backup

Deletes the specified backup  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import backups_api
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
    api_instance = backups_api.BackupsApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 
    server_id = "server_id_example" # str | 
    backup_id = "backup_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{backup} ] Delete backup
        api_response = api_instance.client_serversserver_id_backupsbackup_id_delete(accept, content_type, server_id, backup_id)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling BackupsApi->client_serversserver_id_backupsbackup_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **content_type** | **str**|  |
 **server_id** | **str**|  |
 **backup_id** | **str**|  |

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

# **client_serversserver_id_backupsbackup_id_download_get**
> bool, date, datetime, dict, float, int, list, str, none_type client_serversserver_id_backupsbackup_id_download_get(accept, content_type, server_id, backup_id)

[ /{backup}/download ] Download backup

Generates a download link for a backup  <!-- RESPONSE 200 --> {   \"object\": \"signed_url\",   \"attributes\": {     \"url\": \"https://pterodactyl.file.properties:8080/download/backup?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImp0aSI6IjdkYzAxNzVjODU4MTE5MDRlMjJjNTcxNjBhMjkwMjgwZGFjMDMzM2I2ZmJhMTE3YTI4YjdhMDM5Y2U1OTg0YzcifQ.eyJpc3MiOiJodHRwczpcL1wvcHRlcm9kYWN0eWwuZmlsZS5wcm9wZXJ0aWVzIiwiYXVkIjoiaHR0cHM6XC9cL3B0ZXJvZGFjdHlsLmZpbGUucHJvcGVydGllczo4MDgwIiwianRpIjoiN2RjMDE3NWM4NTgxMTkwNGUyMmM1NzE2MGEyOTAyODBkYWMwMzMzYjZmYmExMTdhMjhiN2EwMzljZTU5ODRjNyIsImlhdCI6MTU5NTE3MjEyNSwibmJmIjoxNTk1MTcxODI1LCJleHAiOjE1OTUxNzMwMjUsImJhY2t1cF91dWlkIjoiOTA0ZGYxMjAtYTY2Zi00Mzc1LWE0YWUtNDBlZWRiZWFlNjMwIiwic2VydmVyX3V1aWQiOiIxYTdjZTk5Ny0yNTliLTQ1MmUtOGI0ZS1jZWNjNDY0MTQyY2EiLCJ1bmlxdWVfaWQiOiJKN1lIQUFUZzVoYVg4M1VOIn0.0zSozCFyjsYjGjUiPS76wM1WXX09FecNxdSZnj6rNt4\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import backups_api
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
    api_instance = backups_api.BackupsApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 
    server_id = "server_id_example" # str | 
    backup_id = "backup_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{backup}/download ] Download backup
        api_response = api_instance.client_serversserver_id_backupsbackup_id_download_get(accept, content_type, server_id, backup_id)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling BackupsApi->client_serversserver_id_backupsbackup_id_download_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **content_type** | **str**|  |
 **server_id** | **str**|  |
 **backup_id** | **str**|  |

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

# **client_serversserver_id_backupsbackup_id_get**
> bool, date, datetime, dict, float, int, list, str, none_type client_serversserver_id_backupsbackup_id_get(accept, content_type, server_id, backup_id)

[ /{backup} ] Backup details

Retrieves information about the specified backup  <!-- RESPONSE 200 --> {   \"object\": \"backup\",   \"attributes\": {     \"uuid\": \"904df120-a66f-4375-a4ae-40eedbeae630\",     \"name\": \"Quick Backup\",     \"ignored_files\": [],     \"sha256_hash\": \"7c20d6a269b441a9dfd044e3f8ad13d77c09c83af8832d29ad603084a9a63726\",     \"bytes\": 114402862,     \"created_at\": \"2020-06-13T05:21:01+01:00\",     \"completed_at\": \"2020-06-13T05:21:04+01:00\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import backups_api
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
    api_instance = backups_api.BackupsApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 
    server_id = "server_id_example" # str | 
    backup_id = "backup_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{backup} ] Backup details
        api_response = api_instance.client_serversserver_id_backupsbackup_id_get(accept, content_type, server_id, backup_id)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling BackupsApi->client_serversserver_id_backupsbackup_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **content_type** | **str**|  |
 **server_id** | **str**|  |
 **backup_id** | **str**|  |

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

