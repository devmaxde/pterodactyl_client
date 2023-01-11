# pterodactyl_client.NetworkApi

All URIs are relative to *https://example.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**client_serversserver_id_network_allocations_get**](NetworkApi.md#client_serversserver_id_network_allocations_get) | **GET** /client/servers/{server_id}/network/allocations | [ /allocations ] List allocations
[**client_serversserver_id_network_allocations_post**](NetworkApi.md#client_serversserver_id_network_allocations_post) | **POST** /client/servers/{server_id}/network/allocations | [ /allocations ] Assign allocation
[**client_serversserver_id_network_allocationsallocation_id_delete**](NetworkApi.md#client_serversserver_id_network_allocationsallocation_id_delete) | **DELETE** /client/servers/{server_id}/network/allocations/{allocation_id} | [ /allocations/{allocation} ] Unassign allocation
[**client_serversserver_id_network_allocationsallocation_id_post**](NetworkApi.md#client_serversserver_id_network_allocationsallocation_id_post) | **POST** /client/servers/{server_id}/network/allocations/{allocation_id} | [ /allocations/{allocation} ] Set allocation note
[**client_serversserver_id_network_allocationsallocation_id_primary_post**](NetworkApi.md#client_serversserver_id_network_allocationsallocation_id_primary_post) | **POST** /client/servers/{server_id}/network/allocations/{allocation_id}/primary | [ /allocations/{allocation}/primary ] Set primary allocation


# **client_serversserver_id_network_allocations_get**
> bool, date, datetime, dict, float, int, list, str, none_type client_serversserver_id_network_allocations_get(accept, content_type, server_id)

[ /allocations ] List allocations

Retrieves the network information for the specified server  <!-- RESPONSE 200 --> {   \"object\": \"list\",   \"data\": [     {       \"object\": \"allocation\",       \"attributes\": {         \"id\": 1,         \"ip\": \"45.86.168.218\",         \"ip_alias\": null,         \"port\": 25565,         \"notes\": null,         \"is_default\": true       }     },     {       \"object\": \"allocation\",       \"attributes\": {         \"id\": 2,         \"ip\": \"45.86.168.218\",         \"ip_alias\": null,         \"port\": 25566,         \"notes\": \"Votifier\",         \"is_default\": false       }     }   ] } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import network_api
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
    api_instance = network_api.NetworkApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 
    server_id = "server_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /allocations ] List allocations
        api_response = api_instance.client_serversserver_id_network_allocations_get(accept, content_type, server_id)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling NetworkApi->client_serversserver_id_network_allocations_get: %s\n" % e)
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

# **client_serversserver_id_network_allocations_post**
> bool, date, datetime, dict, float, int, list, str, none_type client_serversserver_id_network_allocations_post(accept, content_type, server_id)

[ /allocations ] Assign allocation

Automatically assigns a new allocation if auto-assign is enabled on the instance  <!-- RESPONSE 200 --> {   \"object\": \"allocation\",   \"attributes\": {     \"id\": 6,     \"ip\": \"45.86.168.218\",     \"ip_alias\": null,     \"port\": 25570,     \"notes\": null,     \"is_default\": false   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import network_api
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
    api_instance = network_api.NetworkApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 
    server_id = "server_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /allocations ] Assign allocation
        api_response = api_instance.client_serversserver_id_network_allocations_post(accept, content_type, server_id)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling NetworkApi->client_serversserver_id_network_allocations_post: %s\n" % e)
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

# **client_serversserver_id_network_allocationsallocation_id_delete**
> bool, date, datetime, dict, float, int, list, str, none_type client_serversserver_id_network_allocationsallocation_id_delete(accept, server_id, allocation_id)

[ /allocations/{allocation} ] Unassign allocation

Deletes the specified non-primary allocation  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->  <!-- RESPONSE 400 --> {   \"errors\": [     {       \"code\": \"DisplayException\",       \"status\": \"400\",       \"detail\": \"Cannot delete the primary allocation for a server.\"     }   ] } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import network_api
from pterodactyl_client.model.int import Int
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
    api_instance = network_api.NetworkApi(api_client)
    accept = "application/json" # str | 
    server_id = "server_id_example" # str | 
    allocation_id =  # Int | 

    # example passing only required values which don't have defaults set
    try:
        # [ /allocations/{allocation} ] Unassign allocation
        api_response = api_instance.client_serversserver_id_network_allocationsallocation_id_delete(accept, server_id, allocation_id)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling NetworkApi->client_serversserver_id_network_allocationsallocation_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **server_id** | **str**|  |
 **allocation_id** | **Int**|  |
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

# **client_serversserver_id_network_allocationsallocation_id_post**
> bool, date, datetime, dict, float, int, list, str, none_type client_serversserver_id_network_allocationsallocation_id_post(accept, server_id, allocation_id, client_servers_server_id_network_allocations_allocation_id_post_request)

[ /allocations/{allocation} ] Set allocation note

Sets a note for the allocation  # Fields | Name  | Required? | Type   | Description         | Rules | |-------|-----------|--------|---------------------|-------| | notes | required  | string | Note for allocation |       |  <!-- RESPONSE 200 --> {   \"object\": \"allocation\",   \"attributes\": {     \"id\": 2,     \"ip\": \"45.86.168.218\",     \"ip_alias\": null,     \"port\": 25566,     \"notes\": \"Votifier\",     \"is_default\": false   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import network_api
from pterodactyl_client.model.client_servers_server_id_network_allocations_allocation_id_post_request import ClientServersServerIdNetworkAllocationsAllocationIdPostRequest
from pterodactyl_client.model.int import Int
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
    api_instance = network_api.NetworkApi(api_client)
    accept = "application/json" # str | 
    server_id = "server_id_example" # str | 
    allocation_id =  # Int | 
    client_servers_server_id_network_allocations_allocation_id_post_request = ClientServersServerIdNetworkAllocationsAllocationIdPostRequest(None) # ClientServersServerIdNetworkAllocationsAllocationIdPostRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ /allocations/{allocation} ] Set allocation note
        api_response = api_instance.client_serversserver_id_network_allocationsallocation_id_post(accept, server_id, allocation_id, client_servers_server_id_network_allocations_allocation_id_post_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling NetworkApi->client_serversserver_id_network_allocationsallocation_id_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **server_id** | **str**|  |
 **allocation_id** | **Int**|  |
 **client_servers_server_id_network_allocations_allocation_id_post_request** | [**ClientServersServerIdNetworkAllocationsAllocationIdPostRequest**](ClientServersServerIdNetworkAllocationsAllocationIdPostRequest.md)|  |

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

# **client_serversserver_id_network_allocationsallocation_id_primary_post**
> bool, date, datetime, dict, float, int, list, str, none_type client_serversserver_id_network_allocationsallocation_id_primary_post(accept, server_id, allocation_id)

[ /allocations/{allocation}/primary ] Set primary allocation

Sets the primary allocation  <!-- RESPONSE 200 --> {   \"object\": \"allocation\",   \"attributes\": {     \"id\": 2,     \"ip\": \"45.86.168.218\",     \"ip_alias\": null,     \"port\": 25566,     \"notes\": \"Votifier\",     \"is_default\": true   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import network_api
from pterodactyl_client.model.int import Int
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
    api_instance = network_api.NetworkApi(api_client)
    accept = "application/json" # str | 
    server_id = "server_id_example" # str | 
    allocation_id =  # Int | 

    # example passing only required values which don't have defaults set
    try:
        # [ /allocations/{allocation}/primary ] Set primary allocation
        api_response = api_instance.client_serversserver_id_network_allocationsallocation_id_primary_post(accept, server_id, allocation_id)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling NetworkApi->client_serversserver_id_network_allocationsallocation_id_primary_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **server_id** | **str**|  |
 **allocation_id** | **Int**|  |
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

