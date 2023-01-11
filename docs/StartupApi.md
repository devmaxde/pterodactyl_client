# pterodactyl_client.StartupApi

All URIs are relative to *https://example.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**client_serversserver_id_startup_get**](StartupApi.md#client_serversserver_id_startup_get) | **GET** /client/servers/{server_id}/startup | [ / ] List Variables
[**client_serversserver_id_startup_variable_put**](StartupApi.md#client_serversserver_id_startup_variable_put) | **PUT** /client/servers/{server_id}/startup/variable | [ /variable ] Update Variable


# **client_serversserver_id_startup_get**
> bool, date, datetime, dict, float, int, list, str, none_type client_serversserver_id_startup_get(accept, server_id)

[ / ] List Variables

Lists all variables on the server  <!-- RESPONSE 200 --> {   \"object\": \"list\",   \"data\": [     {       \"object\": \"egg_variable\",       \"attributes\": {         \"name\": \"Server Jar File\",         \"description\": \"The name of the server jarfile to run the server with.\",         \"env_variable\": \"SERVER_JARFILE\",         \"default_value\": \"server.jar\",         \"server_value\": \"server.jar\",         \"is_editable\": true,         \"rules\": \"required|regex:/^([\\\\w\\\\d._-]+)(\\\\.jar)$/\"       }     },     {       \"object\": \"egg_variable\",       \"attributes\": {         \"name\": \"Server Version\",         \"description\": \"The version of Minecraft Vanilla to install. Use \\\"latest\\\" to install the latest version.\",         \"env_variable\": \"VANILLA_VERSION\",         \"default_value\": \"latest\",         \"server_value\": \"latest\",         \"is_editable\": true,         \"rules\": \"required|string|between:3,15\"       }     }   ],   \"meta\": {     \"startup_command\": \"java -Xms128M -Xmx512M -jar server.jar\",     \"raw_startup_command\": \"java -Xms128M -Xmx\\{\\{ SERVER_MEMORY }}M -jar {\\{ SERVER_JARFILE }}\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import startup_api
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
    api_instance = startup_api.StartupApi(api_client)
    accept = "application/json" # str | 
    server_id = "server_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ / ] List Variables
        api_response = api_instance.client_serversserver_id_startup_get(accept, server_id)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling StartupApi->client_serversserver_id_startup_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
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

# **client_serversserver_id_startup_variable_put**
> bool, date, datetime, dict, float, int, list, str, none_type client_serversserver_id_startup_variable_put(accept, server_id, client_servers_server_id_startup_variable_put_request)

[ /variable ] Update Variable

Updates the specified variable  <!-- RESPONSE 200 --> {   \"object\": \"egg_variable\",   \"attributes\": {     \"name\": \"Server Jar File\",     \"description\": \"The name of the server jarfile to run the server with.\",     \"env_variable\": \"SERVER_JARFILE\",     \"default_value\": \"server.jar\",     \"server_value\": \"server.jar\",     \"is_editable\": true,     \"rules\": \"required|regex:/^([\\\\w\\\\d._-]+)(\\\\.jar)$/\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import startup_api
from pterodactyl_client.model.client_servers_server_id_startup_variable_put_request import ClientServersServerIdStartupVariablePutRequest
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
    api_instance = startup_api.StartupApi(api_client)
    accept = "application/json" # str | 
    server_id = "server_id_example" # str | 
    client_servers_server_id_startup_variable_put_request = ClientServersServerIdStartupVariablePutRequest(None) # ClientServersServerIdStartupVariablePutRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ /variable ] Update Variable
        api_response = api_instance.client_serversserver_id_startup_variable_put(accept, server_id, client_servers_server_id_startup_variable_put_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling StartupApi->client_serversserver_id_startup_variable_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **server_id** | **str**|  |
 **client_servers_server_id_startup_variable_put_request** | [**ClientServersServerIdStartupVariablePutRequest**](ClientServersServerIdStartupVariablePutRequest.md)|  |

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

