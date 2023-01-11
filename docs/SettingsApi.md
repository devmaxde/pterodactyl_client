# pterodactyl_client.SettingsApi

All URIs are relative to *https://example.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**client_serversserver_id_settings_reinstall_post**](SettingsApi.md#client_serversserver_id_settings_reinstall_post) | **POST** /client/servers/{server_id}/settings/reinstall | [ /reinstall ] Reinstall server
[**client_serversserver_id_settings_rename_post**](SettingsApi.md#client_serversserver_id_settings_rename_post) | **POST** /client/servers/{server_id}/settings/rename | [ /rename ] Rename server


# **client_serversserver_id_settings_reinstall_post**
> bool, date, datetime, dict, float, int, list, str, none_type client_serversserver_id_settings_reinstall_post(accept, server_id)

[ /reinstall ] Reinstall server

Renames the server  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import settings_api
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
    api_instance = settings_api.SettingsApi(api_client)
    accept = "application/json" # str | 
    server_id = "server_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /reinstall ] Reinstall server
        api_response = api_instance.client_serversserver_id_settings_reinstall_post(accept, server_id)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling SettingsApi->client_serversserver_id_settings_reinstall_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **server_id** | **str**|  |
 **content_type** | **str**|  | defaults to "application/json"

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

# **client_serversserver_id_settings_rename_post**
> bool, date, datetime, dict, float, int, list, str, none_type client_serversserver_id_settings_rename_post(accept, server_id, client_servers_server_id_settings_rename_post_request)

[ /rename ] Rename server

Renames the server  # Fields | Name | Required? | Type   | Description             | Rules | |------|-----------|--------|-------------------------|-------| | name | required  | string | New name for the server |       |  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import settings_api
from pterodactyl_client.model.client_servers_server_id_settings_rename_post_request import ClientServersServerIdSettingsRenamePostRequest
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
    api_instance = settings_api.SettingsApi(api_client)
    accept = "application/json" # str | 
    server_id = "server_id_example" # str | 
    client_servers_server_id_settings_rename_post_request = ClientServersServerIdSettingsRenamePostRequest(None) # ClientServersServerIdSettingsRenamePostRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ /rename ] Rename server
        api_response = api_instance.client_serversserver_id_settings_rename_post(accept, server_id, client_servers_server_id_settings_rename_post_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling SettingsApi->client_serversserver_id_settings_rename_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **server_id** | **str**|  |
 **client_servers_server_id_settings_rename_post_request** | [**ClientServersServerIdSettingsRenamePostRequest**](ClientServersServerIdSettingsRenamePostRequest.md)|  |

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

