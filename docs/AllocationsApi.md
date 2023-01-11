# pterodactyl_client.AllocationsApi

All URIs are relative to *https://example.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**application_nodesnode_id_allocations_get**](AllocationsApi.md#application_nodesnode_id_allocations_get) | **GET** /application/nodes/{node_id}/allocations | [ / ] List allocations
[**application_nodesnode_id_allocations_post**](AllocationsApi.md#application_nodesnode_id_allocations_post) | **POST** /application/nodes/{node_id}/allocations | [ / ] Create allocations
[**application_nodesnode_id_allocationsallocation_id_delete**](AllocationsApi.md#application_nodesnode_id_allocationsallocation_id_delete) | **DELETE** /application/nodes/{node_id}/allocations/{allocation_id} | [ /{allocation} ] Delete allocation


# **application_nodesnode_id_allocations_get**
> bool, date, datetime, dict, float, int, list, str, none_type application_nodesnode_id_allocations_get(accept, content_type, node_id)

[ / ] List allocations

Lists allocations added to the node  ## Available include parameters | Parameter | Description                                            | |-----------|--------------------------------------------------------| | node      | Information about the node the allocation belongs to   | | server    | Information about the server the allocation belongs to |  <!-- RESPONSE 200 --> {   \"object\": \"list\",   \"data\": [     {       \"object\": \"allocation\",       \"attributes\": {         \"id\": 1,         \"ip\": \"45.86.168.218\",         \"alias\": null,         \"port\": 25565,         \"notes\": null,         \"assigned\": true       }     },     {       \"object\": \"allocation\",       \"attributes\": {         \"id\": 2,         \"ip\": \"45.86.168.218\",         \"alias\": null,         \"port\": 25566,         \"notes\": \"Votifier\",         \"assigned\": true       }     },     {       \"object\": \"allocation\",       \"attributes\": {         \"id\": 3,         \"ip\": \"45.86.168.218\",         \"alias\": null,         \"port\": 25567,         \"notes\": null,         \"assigned\": false       }     },     {       \"object\": \"allocation\",       \"attributes\": {         \"id\": 4,         \"ip\": \"45.86.168.218\",         \"alias\": null,         \"port\": 25568,         \"notes\": null,         \"assigned\": false       }     },     {       \"object\": \"allocation\",       \"attributes\": {         \"id\": 5,         \"ip\": \"45.86.168.218\",         \"alias\": null,         \"port\": 25569,         \"notes\": null,         \"assigned\": false       }     },     {       \"object\": \"allocation\",       \"attributes\": {         \"id\": 6,         \"ip\": \"45.86.168.218\",         \"alias\": null,         \"port\": 25570,         \"notes\": null,         \"assigned\": false       }     },     {       \"object\": \"allocation\",       \"attributes\": {         \"id\": 8,         \"ip\": \"10.0.0.1\",         \"alias\": null,         \"port\": 25565,         \"notes\": null,         \"assigned\": false       }     },     {       \"object\": \"allocation\",       \"attributes\": {         \"id\": 9,         \"ip\": \"45.86.168.218\",         \"alias\": null,         \"port\": 25571,         \"notes\": null,         \"assigned\": false       }     },     {       \"object\": \"allocation\",       \"attributes\": {         \"id\": 10,         \"ip\": \"45.86.168.218\",         \"alias\": null,         \"port\": 25572,         \"notes\": null,         \"assigned\": false       }     },     {       \"object\": \"allocation\",       \"attributes\": {         \"id\": 11,         \"ip\": \"45.86.168.218\",         \"alias\": null,         \"port\": 25573,         \"notes\": null,         \"assigned\": false       }     },     {       \"object\": \"allocation\",       \"attributes\": {         \"id\": 12,         \"ip\": \"45.86.168.218\",         \"alias\": null,         \"port\": 25574,         \"notes\": null,         \"assigned\": false       }     },     {       \"object\": \"allocation\",       \"attributes\": {         \"id\": 13,         \"ip\": \"45.86.168.218\",         \"alias\": null,         \"port\": 25575,         \"notes\": null,         \"assigned\": false       }     },     {       \"object\": \"allocation\",       \"attributes\": {         \"id\": 14,         \"ip\": \"45.86.168.218\",         \"alias\": null,         \"port\": 25576,         \"notes\": null,         \"assigned\": false       }     },     {       \"object\": \"allocation\",       \"attributes\": {         \"id\": 15,         \"ip\": \"45.86.168.218\",         \"alias\": null,         \"port\": 25577,         \"notes\": null,         \"assigned\": false       }     },     {       \"object\": \"allocation\",       \"attributes\": {         \"id\": 16,         \"ip\": \"45.86.168.218\",         \"alias\": null,         \"port\": 25578,         \"notes\": null,         \"assigned\": false       }     },     {       \"object\": \"allocation\",       \"attributes\": {         \"id\": 17,         \"ip\": \"45.86.168.218\",         \"alias\": null,         \"port\": 25579,         \"notes\": null,         \"assigned\": false       }     },     {       \"object\": \"allocation\",       \"attributes\": {         \"id\": 18,         \"ip\": \"45.86.168.218\",         \"alias\": null,         \"port\": 25580,         \"notes\": null,         \"assigned\": false       }     }   ],   \"meta\": {     \"pagination\": {       \"total\": 17,       \"count\": 17,       \"per_page\": 50,       \"current_page\": 1,       \"total_pages\": 1,       \"links\": {}     }   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import allocations_api
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
    api_instance = allocations_api.AllocationsApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 
    node_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # [ / ] List allocations
        api_response = api_instance.application_nodesnode_id_allocations_get(accept, content_type, node_id)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling AllocationsApi->application_nodesnode_id_allocations_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **content_type** | **str**|  |
 **node_id** | **int**|  |

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

# **application_nodesnode_id_allocations_post**
> bool, date, datetime, dict, float, int, list, str, none_type application_nodesnode_id_allocations_post(accept, node_id, application_nodes_node_id_allocations_post_request)

[ / ] Create allocations

Adds an allocation to the node  ## Fields | Name  | Required? | Type   | Description                        | Rules | |-------|-----------|--------|------------------------------------|-------| | ip    | required  | string | IP address for the allocations     |       | | ports | required  | object | Object containing the ports to add |       |  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import allocations_api
from pterodactyl_client.model.application_nodes_node_id_allocations_post_request import ApplicationNodesNodeIdAllocationsPostRequest
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
    api_instance = allocations_api.AllocationsApi(api_client)
    accept = "application/json" # str | 
    node_id = 1 # int | 
    application_nodes_node_id_allocations_post_request = ApplicationNodesNodeIdAllocationsPostRequest(None) # ApplicationNodesNodeIdAllocationsPostRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ / ] Create allocations
        api_response = api_instance.application_nodesnode_id_allocations_post(accept, node_id, application_nodes_node_id_allocations_post_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling AllocationsApi->application_nodesnode_id_allocations_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **node_id** | **int**|  |
 **application_nodes_node_id_allocations_post_request** | [**ApplicationNodesNodeIdAllocationsPostRequest**](ApplicationNodesNodeIdAllocationsPostRequest.md)|  |

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

# **application_nodesnode_id_allocationsallocation_id_delete**
> bool, date, datetime, dict, float, int, list, str, none_type application_nodesnode_id_allocationsallocation_id_delete(accept, content_type, node_id, allocation_id)

[ /{allocation} ] Delete allocation

Deletes the specified allocation  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import allocations_api
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
    api_instance = allocations_api.AllocationsApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 
    node_id = 1 # int | 
    allocation_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{allocation} ] Delete allocation
        api_response = api_instance.application_nodesnode_id_allocationsallocation_id_delete(accept, content_type, node_id, allocation_id)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling AllocationsApi->application_nodesnode_id_allocationsallocation_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **content_type** | **str**|  |
 **node_id** | **int**|  |
 **allocation_id** | **int**|  |

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

