# pterodactyl_client.SettingsSettingsApi

All URIs are relative to *https://example.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**__reinstall_reinstallserver**](SettingsSettingsApi.md#__reinstall_reinstallserver) | **POST** /client/servers/1a7ce997/settings/reinstall | [ /reinstall ] Reinstall server
[**__rename_renameserver**](SettingsSettingsApi.md#__rename_renameserver) | **POST** /client/servers/1a7ce997/settings/rename | [ /rename ] Rename server


# **__reinstall_reinstallserver**
> bool, date, datetime, dict, float, int, list, str, none_type __reinstall_reinstallserver(accept)

[ /reinstall ] Reinstall server

Renames the server  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import settings_settings_api
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
    api_instance = settings_settings_api.SettingsSettingsApi(api_client)
    accept = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /reinstall ] Reinstall server
        api_response = api_instance.__reinstall_reinstallserver(accept)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling SettingsSettingsApi->__reinstall_reinstallserver: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
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

# **__rename_renameserver**
> bool, date, datetime, dict, float, int, list, str, none_type __rename_renameserver(accept, rename_renameserver_request)

[ /rename ] Rename server

Renames the server  # Fields | Name | Required? | Type   | Description             | Rules | |------|-----------|--------|-------------------------|-------| | name | required  | string | New name for the server |       |  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import settings_settings_api
from pterodactyl_client.model.rename_renameserver_request import RenameRenameserverRequest
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
    api_instance = settings_settings_api.SettingsSettingsApi(api_client)
    accept = "application/json" # str | 
    rename_renameserver_request = RenameRenameserverRequest(None) # RenameRenameserverRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ /rename ] Rename server
        api_response = api_instance.__rename_renameserver(accept, rename_renameserver_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling SettingsSettingsApi->__rename_renameserver: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **rename_renameserver_request** | [**RenameRenameserverRequest**](RenameRenameserverRequest.md)|  |

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

