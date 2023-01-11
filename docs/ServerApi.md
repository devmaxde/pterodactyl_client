# pterodactyl_client.ServerApi

All URIs are relative to *https://example.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**client_serversserver_id_command_post**](ServerApi.md#client_serversserver_id_command_post) | **POST** /client/servers/{server_id}/command | [ /command ] Send command
[**client_serversserver_id_get**](ServerApi.md#client_serversserver_id_get) | **GET** /client/servers/{server_id} | [ / ] Server details
[**client_serversserver_id_power_post**](ServerApi.md#client_serversserver_id_power_post) | **POST** /client/servers/{server_id}/power | [ /power ] Change power state
[**client_serversserver_id_resources_get**](ServerApi.md#client_serversserver_id_resources_get) | **GET** /client/servers/{server_id}/resources | [ /resources ] Resource usage
[**client_serversserver_id_websocket_get**](ServerApi.md#client_serversserver_id_websocket_get) | **GET** /client/servers/{server_id}/websocket | [ /websocket ] Console details


# **client_serversserver_id_command_post**
> bool, date, datetime, dict, float, int, list, str, none_type client_serversserver_id_command_post(accept, server_id, client_servers_server_id_command_post_request)

[ /command ] Send command

Sends a command to the server  The server must be online to send a command to it. You will get HTTP 502 is the server if not online.  ## Fields | Name    | Required? | Type   | Description     | Rules | |---------|-----------|--------|-----------------|-------| | command | required  | string | Command to send |       |  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->  <!-- RESPONSE 502 --> // Server offline {   \"errors\": [     {       \"code\": \"HttpException\",       \"status\": \"502\",       \"detail\": \"An error was encountered while processing this request.\"     }   ] }

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import server_api
from pterodactyl_client.model.client_servers_server_id_command_post_request import ClientServersServerIdCommandPostRequest
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
    api_instance = server_api.ServerApi(api_client)
    accept = "application/json" # str | 
    server_id = "server_id_example" # str | 
    client_servers_server_id_command_post_request = ClientServersServerIdCommandPostRequest(None) # ClientServersServerIdCommandPostRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ /command ] Send command
        api_response = api_instance.client_serversserver_id_command_post(accept, server_id, client_servers_server_id_command_post_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServerApi->client_serversserver_id_command_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **server_id** | **str**|  |
 **client_servers_server_id_command_post_request** | [**ClientServersServerIdCommandPostRequest**](ClientServersServerIdCommandPostRequest.md)|  |

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

# **client_serversserver_id_get**
> bool, date, datetime, dict, float, int, list, str, none_type client_serversserver_id_get(accept, content_type, server_id)

[ / ] Server details

Retrieves information about the specified server  ## Include parameters | Parameter | Description                               | |-----------|-------------------------------------------| | egg       | Information about the egg the server uses | | subusers  | List of subusers on the server            |  <!-- RESPONSE 200 --> {   \"object\": \"server\",   \"attributes\": {     \"server_owner\": true,     \"identifier\": \"{server_id}\",     \"uuid\": \"{server_id}-259b-452e-8b4e-cecc464142ca\",     \"name\": \"Wuhu Island\",     \"node\": \"Test\",     \"sftp_details\": {       \"ip\": \"pterodactyl.file.properties\",       \"port\": 2022     },     \"description\": \"Matt from Wii Sports\",     \"limits\": {       \"memory\": 512,       \"swap\": 0,       \"disk\": 200,       \"io\": 500,       \"cpu\": 0     },     \"feature_limits\": {       \"databases\": 5,       \"allocations\": 5,       \"backups\": 2     },     \"is_suspended\": false,     \"is_installing\": false,     \"relationships\": {       \"allocations\": {         \"object\": \"list\",         \"data\": [           {             \"object\": \"allocation\",             \"attributes\": {               \"id\": 1,               \"ip\": \"45.86.168.218\",               \"ip_alias\": null,               \"port\": 25565,               \"notes\": null,               \"is_default\": true             }           },           {             \"object\": \"allocation\",             \"attributes\": {               \"id\": 2,               \"ip\": \"45.86.168.218\",               \"ip_alias\": null,               \"port\": 25566,               \"notes\": \"Votifier\",               \"is_default\": false             }           }         ]       }     }   },   \"meta\": {     \"is_server_owner\": true,     \"user_permissions\": [       \"*\",       \"admin.websocket.errors\",       \"admin.websocket.install\"     ]   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import server_api
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
    api_instance = server_api.ServerApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 
    server_id = "server_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ / ] Server details
        api_response = api_instance.client_serversserver_id_get(accept, content_type, server_id)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServerApi->client_serversserver_id_get: %s\n" % e)
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

# **client_serversserver_id_power_post**
> bool, date, datetime, dict, float, int, list, str, none_type client_serversserver_id_power_post(accept, server_id, client_servers_server_id_power_post_request)

[ /power ] Change power state

Sends a power signal to the server  ## Fields | Name   | Required? | Type   | Description          | Rules | |--------|-----------|--------|----------------------|-------| | signal | required  | string | Power signal to send |       |  ## Signals | Signal  | Description                      | |---------|----------------------------------| | start   | Starts the server                | | stop    | Gracefully stops the server      | | restart | Stops then starts the server     | | kill    | Instantly end the server process |   <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import server_api
from pterodactyl_client.model.client_servers_server_id_power_post_request import ClientServersServerIdPowerPostRequest
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
    api_instance = server_api.ServerApi(api_client)
    accept = "application/json" # str | 
    server_id = "server_id_example" # str | 
    client_servers_server_id_power_post_request = ClientServersServerIdPowerPostRequest(None) # ClientServersServerIdPowerPostRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ /power ] Change power state
        api_response = api_instance.client_serversserver_id_power_post(accept, server_id, client_servers_server_id_power_post_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServerApi->client_serversserver_id_power_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **server_id** | **str**|  |
 **client_servers_server_id_power_post_request** | [**ClientServersServerIdPowerPostRequest**](ClientServersServerIdPowerPostRequest.md)|  |

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

# **client_serversserver_id_resources_get**
> bool, date, datetime, dict, float, int, list, str, none_type client_serversserver_id_resources_get(accept, content_type, server_id)

[ /resources ] Resource usage

Retrieves resource utilization of the specified server  <!-- RESPONSE 200 --> {   \"object\": \"stats\",   \"attributes\": {     \"current_state\": \"starting\",     \"is_suspended\": false,     \"resources\": {       \"memory_bytes\": 588701696,       \"cpu_absolute\": 0,       \"disk_bytes\": 130156361,       \"network_rx_bytes\": 694220,       \"network_tx_bytes\": 337090     }   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import server_api
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
    api_instance = server_api.ServerApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 
    server_id = "server_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /resources ] Resource usage
        api_response = api_instance.client_serversserver_id_resources_get(accept, content_type, server_id)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServerApi->client_serversserver_id_resources_get: %s\n" % e)
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

# **client_serversserver_id_websocket_get**
> bool, date, datetime, dict, float, int, list, str, none_type client_serversserver_id_websocket_get(accept, content_type, server_id)

[ /websocket ] Console details

Generates credentials to establish a websocket  <!-- RESPONSE 200 --> {   \"data\": {     \"token\": \"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImp0aSI6Ij...\",     \"socket\": \"wss://pterodactyl.file.properties:8080/api/servers/{server_id}-259b-452e-8b4e-cecc464142ca/ws\"   } } <!-- ENDRESPONSE -->  ## How to connect 1. Connect to the websocket address (in this example \"wss://pterodactyl.file.properties:8080/api/servers/{server_id}-259b-452e-8b4e-cecc464142ca/ws\") 2. Send the token to the websocket like this: `{\"event\":\"auth\",\"args\":[\"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImp0aSI6Ij...\"]}`  * Tokens last about 10-15 minutes, and the websocket will notify you once you need to send a new token with `{\"event\":\"token expiring\"}` and `{\"event\":\"token expired\"}`  ## Things you can send * `{\"event\":\"auth\",\"args\":[\"<token>\"]}` # Authenticate with websocket * `{\"event\":\"send stats\",\"args\":[null]}` # Request stats * `{\"event\":\"send logs\",\"args\":[null]}` # Request logs * `{\"event\":\"set state\",\"args\":[\"<power-action>\"]}` # Send power action * `{\"event\":\"send command\",\"args\":[\"<command>\"]}` # Send command  ## Things you'll receive * `{\"event\":\"auth success\"}` # Upon successful websocket authentication * `{\"event\":\"status\",\"args\":[\"offline\"]}` # Status updates of the server * `{\"event\":\"console output\",\"args\":[\"[14:07:12] [Query Listener #1/INFO]: Query running on 0.0.0.0:25565\"]}` # Logs from server * `{\"event\":\"stats\",\"args\":[\"{\\\"memory_bytes\\\":526626816,\\\"memory_limit_bytes\\\":588800000,\\\"cpu_absolute\\\":588.815,\\\"network\\\":{\\\"rx_bytes\\\":1126,\\\"tx_bytes\\\":1126},\\\"state\\\":\\\"stopping\\\",\\\"disk_bytes\\\":128118626}\"]}` # Stats from server * `{\"event\":\"token expiring\"}` # Token is expiring soon so request a new one and send it to the websocket * `{\"event\":\"token expired\"}` # Token has expired

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import server_api
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
    api_instance = server_api.ServerApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 
    server_id = "server_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /websocket ] Console details
        api_response = api_instance.client_serversserver_id_websocket_get(accept, content_type, server_id)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServerApi->client_serversserver_id_websocket_get: %s\n" % e)
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

