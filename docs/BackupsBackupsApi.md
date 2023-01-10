# pterodactyl_client.BackupsBackupsApi

All URIs are relative to *https://example.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**__backup_backupdetails**](BackupsBackupsApi.md#__backup_backupdetails) | **GET** /client/servers/1a7ce997/backups/904df120-a66f-4375-a4ae-40eedbeae630 | [ /{backup} ] Backup details
[**__backup_deletebackup**](BackupsBackupsApi.md#__backup_deletebackup) | **DELETE** /client/servers/1a7ce997/backups/63087048-eada-419c-ad72-803c1c949cac | [ /{backup} ] Delete backup
[**__backup_download_downloadbackup**](BackupsBackupsApi.md#__backup_download_downloadbackup) | **GET** /client/servers/1a7ce997/backups/904df120-a66f-4375-a4ae-40eedbeae630/download | [ /{backup}/download ] Download backup
[**__createbackup**](BackupsBackupsApi.md#__createbackup) | **POST** /client/servers/1a7ce997/backups | [ / ] Create backup
[**__listbackups**](BackupsBackupsApi.md#__listbackups) | **GET** /client/servers/1a7ce997/backups | [ / ] List backups


# **__backup_backupdetails**
> bool, date, datetime, dict, float, int, list, str, none_type __backup_backupdetails(accept, content_type)

[ /{backup} ] Backup details

Retrieves information about the specified backup  <!-- RESPONSE 200 --> {   \"object\": \"backup\",   \"attributes\": {     \"uuid\": \"904df120-a66f-4375-a4ae-40eedbeae630\",     \"name\": \"Quick Backup\",     \"ignored_files\": [],     \"sha256_hash\": \"7c20d6a269b441a9dfd044e3f8ad13d77c09c83af8832d29ad603084a9a63726\",     \"bytes\": 114402862,     \"created_at\": \"2020-06-13T05:21:01+01:00\",     \"completed_at\": \"2020-06-13T05:21:04+01:00\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import backups_backups_api
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
    api_instance = backups_backups_api.BackupsBackupsApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{backup} ] Backup details
        api_response = api_instance.__backup_backupdetails(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling BackupsBackupsApi->__backup_backupdetails: %s\n" % e)
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

# **__backup_deletebackup**
> bool, date, datetime, dict, float, int, list, str, none_type __backup_deletebackup(accept, content_type)

[ /{backup} ] Delete backup

Deletes the specified backup  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import backups_backups_api
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
    api_instance = backups_backups_api.BackupsBackupsApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{backup} ] Delete backup
        api_response = api_instance.__backup_deletebackup(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling BackupsBackupsApi->__backup_deletebackup: %s\n" % e)
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

# **__backup_download_downloadbackup**
> bool, date, datetime, dict, float, int, list, str, none_type __backup_download_downloadbackup(accept, content_type)

[ /{backup}/download ] Download backup

Generates a download link for a backup  <!-- RESPONSE 200 --> {   \"object\": \"signed_url\",   \"attributes\": {     \"url\": \"https://pterodactyl.file.properties:8080/download/backup?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImp0aSI6IjdkYzAxNzVjODU4MTE5MDRlMjJjNTcxNjBhMjkwMjgwZGFjMDMzM2I2ZmJhMTE3YTI4YjdhMDM5Y2U1OTg0YzcifQ.eyJpc3MiOiJodHRwczpcL1wvcHRlcm9kYWN0eWwuZmlsZS5wcm9wZXJ0aWVzIiwiYXVkIjoiaHR0cHM6XC9cL3B0ZXJvZGFjdHlsLmZpbGUucHJvcGVydGllczo4MDgwIiwianRpIjoiN2RjMDE3NWM4NTgxMTkwNGUyMmM1NzE2MGEyOTAyODBkYWMwMzMzYjZmYmExMTdhMjhiN2EwMzljZTU5ODRjNyIsImlhdCI6MTU5NTE3MjEyNSwibmJmIjoxNTk1MTcxODI1LCJleHAiOjE1OTUxNzMwMjUsImJhY2t1cF91dWlkIjoiOTA0ZGYxMjAtYTY2Zi00Mzc1LWE0YWUtNDBlZWRiZWFlNjMwIiwic2VydmVyX3V1aWQiOiIxYTdjZTk5Ny0yNTliLTQ1MmUtOGI0ZS1jZWNjNDY0MTQyY2EiLCJ1bmlxdWVfaWQiOiJKN1lIQUFUZzVoYVg4M1VOIn0.0zSozCFyjsYjGjUiPS76wM1WXX09FecNxdSZnj6rNt4\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import backups_backups_api
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
    api_instance = backups_backups_api.BackupsBackupsApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{backup}/download ] Download backup
        api_response = api_instance.__backup_download_downloadbackup(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling BackupsBackupsApi->__backup_download_downloadbackup: %s\n" % e)
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

# **__createbackup**
> bool, date, datetime, dict, float, int, list, str, none_type __createbackup(accept, content_type)

[ / ] Create backup

Creates a new backup  <!-- RESPONSE 200 --> {   \"object\": \"backup\",   \"attributes\": {     \"uuid\": \"63087048-eada-419c-ad72-803c1c949cac\",     \"name\": \"Backup at 2020-07-19 16:21:34\",     \"ignored_files\": [],     \"sha256_hash\": null,     \"bytes\": 0,     \"created_at\": \"2020-07-19T16:21:34+01:00\",     \"completed_at\": null   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import backups_backups_api
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
    api_instance = backups_backups_api.BackupsBackupsApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ / ] Create backup
        api_response = api_instance.__createbackup(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling BackupsBackupsApi->__createbackup: %s\n" % e)
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

# **__listbackups**
> bool, date, datetime, dict, float, int, list, str, none_type __listbackups(accept, content_type)

[ / ] List backups

Retrieves a list of backups  <!-- RESPONSE 200 --> {   \"object\": \"list\",   \"data\": [     {       \"object\": \"backup\",       \"attributes\": {         \"uuid\": \"904df120-a66f-4375-a4ae-40eedbeae630\",         \"name\": \"Quick Backup\",         \"ignored_files\": [],         \"sha256_hash\": \"7c20d6a269b441a9dfd044e3f8ad13d77c09c83af8832d29ad603084a9a63726\",         \"bytes\": 114402862,         \"created_at\": \"2020-06-13T05:21:01+01:00\",         \"completed_at\": \"2020-06-13T05:21:04+01:00\"       }     },     {       \"object\": \"backup\",       \"attributes\": {         \"uuid\": \"63087048-eada-419c-ad72-803c1c949cac\",         \"name\": \"Backup at 2020-07-19 16:21:34\",         \"ignored_files\": [],         \"sha256_hash\": \"39bf93b9d8aee45316fa7ec8bbed0530904558851fa8e712452845c969873b16\",         \"bytes\": 114567250,         \"created_at\": \"2020-07-19T16:21:34+01:00\",         \"completed_at\": \"2020-07-19T16:21:35+01:00\"       }     }   ],   \"meta\": {     \"pagination\": {       \"total\": 2,       \"count\": 2,       \"per_page\": 20,       \"current_page\": 1,       \"total_pages\": 1,       \"links\": {}     }   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import backups_backups_api
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
    api_instance = backups_backups_api.BackupsBackupsApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ / ] List backups
        api_response = api_instance.__listbackups(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling BackupsBackupsApi->__listbackups: %s\n" % e)
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

