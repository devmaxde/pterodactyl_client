# pterodactyl_client.NodeAllocationsAllocationsApi

All URIs are relative to *https://example.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**__allocation_deleteallocation**](NodeAllocationsAllocationsApi.md#__allocation_deleteallocation) | **DELETE** /application/nodes/1/allocations/18 | [ /{allocation} ] Delete allocation
[**__createallocations**](NodeAllocationsAllocationsApi.md#__createallocations) | **POST** /application/nodes/1/allocations | [ / ] Create allocations
[**__listallocations**](NodeAllocationsAllocationsApi.md#__listallocations) | **GET** /application/nodes/1/allocations | [ / ] List allocations


# **__allocation_deleteallocation**
> bool, date, datetime, dict, float, int, list, str, none_type __allocation_deleteallocation(accept, content_type)

[ /{allocation} ] Delete allocation

Deletes the specified allocation  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import node_allocations_allocations_api
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
    api_instance = node_allocations_allocations_api.NodeAllocationsAllocationsApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{allocation} ] Delete allocation
        api_response = api_instance.__allocation_deleteallocation(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling NodeAllocationsAllocationsApi->__allocation_deleteallocation: %s\n" % e)
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

# **__createallocations**
> bool, date, datetime, dict, float, int, list, str, none_type __createallocations(accept, createallocations_request)

[ / ] Create allocations

Adds an allocation to the node  ## Fields | Name  | Required? | Type   | Description                        | Rules | |-------|-----------|--------|------------------------------------|-------| | ip    | required  | string | IP address for the allocations     |       | | ports | required  | object | Object containing the ports to add |       |  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import node_allocations_allocations_api
from pterodactyl_client.model.createallocations_request import CreateallocationsRequest
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
    api_instance = node_allocations_allocations_api.NodeAllocationsAllocationsApi(api_client)
    accept = "application/json" # str | 
    createallocations_request = CreateallocationsRequest(None) # CreateallocationsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ / ] Create allocations
        api_response = api_instance.__createallocations(accept, createallocations_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling NodeAllocationsAllocationsApi->__createallocations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **createallocations_request** | [**CreateallocationsRequest**](CreateallocationsRequest.md)|  |

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

# **__listallocations**
> bool, date, datetime, dict, float, int, list, str, none_type __listallocations(accept, content_type)

[ / ] List allocations

Lists allocations added to the node  ## Available include parameters | Parameter | Description                                            | |-----------|--------------------------------------------------------| | node      | Information about the node the allocation belongs to   | | server    | Information about the server the allocation belongs to |  <!-- RESPONSE 200 --> {   \"object\": \"list\",   \"data\": [     {       \"object\": \"allocation\",       \"attributes\": {         \"id\": 1,         \"ip\": \"45.86.168.218\",         \"alias\": null,         \"port\": 25565,         \"notes\": null,         \"assigned\": true       }     },     {       \"object\": \"allocation\",       \"attributes\": {         \"id\": 2,         \"ip\": \"45.86.168.218\",         \"alias\": null,         \"port\": 25566,         \"notes\": \"Votifier\",         \"assigned\": true       }     },     {       \"object\": \"allocation\",       \"attributes\": {         \"id\": 3,         \"ip\": \"45.86.168.218\",         \"alias\": null,         \"port\": 25567,         \"notes\": null,         \"assigned\": false       }     },     {       \"object\": \"allocation\",       \"attributes\": {         \"id\": 4,         \"ip\": \"45.86.168.218\",         \"alias\": null,         \"port\": 25568,         \"notes\": null,         \"assigned\": false       }     },     {       \"object\": \"allocation\",       \"attributes\": {         \"id\": 5,         \"ip\": \"45.86.168.218\",         \"alias\": null,         \"port\": 25569,         \"notes\": null,         \"assigned\": false       }     },     {       \"object\": \"allocation\",       \"attributes\": {         \"id\": 6,         \"ip\": \"45.86.168.218\",         \"alias\": null,         \"port\": 25570,         \"notes\": null,         \"assigned\": false       }     },     {       \"object\": \"allocation\",       \"attributes\": {         \"id\": 8,         \"ip\": \"10.0.0.1\",         \"alias\": null,         \"port\": 25565,         \"notes\": null,         \"assigned\": false       }     },     {       \"object\": \"allocation\",       \"attributes\": {         \"id\": 9,         \"ip\": \"45.86.168.218\",         \"alias\": null,         \"port\": 25571,         \"notes\": null,         \"assigned\": false       }     },     {       \"object\": \"allocation\",       \"attributes\": {         \"id\": 10,         \"ip\": \"45.86.168.218\",         \"alias\": null,         \"port\": 25572,         \"notes\": null,         \"assigned\": false       }     },     {       \"object\": \"allocation\",       \"attributes\": {         \"id\": 11,         \"ip\": \"45.86.168.218\",         \"alias\": null,         \"port\": 25573,         \"notes\": null,         \"assigned\": false       }     },     {       \"object\": \"allocation\",       \"attributes\": {         \"id\": 12,         \"ip\": \"45.86.168.218\",         \"alias\": null,         \"port\": 25574,         \"notes\": null,         \"assigned\": false       }     },     {       \"object\": \"allocation\",       \"attributes\": {         \"id\": 13,         \"ip\": \"45.86.168.218\",         \"alias\": null,         \"port\": 25575,         \"notes\": null,         \"assigned\": false       }     },     {       \"object\": \"allocation\",       \"attributes\": {         \"id\": 14,         \"ip\": \"45.86.168.218\",         \"alias\": null,         \"port\": 25576,         \"notes\": null,         \"assigned\": false       }     },     {       \"object\": \"allocation\",       \"attributes\": {         \"id\": 15,         \"ip\": \"45.86.168.218\",         \"alias\": null,         \"port\": 25577,         \"notes\": null,         \"assigned\": false       }     },     {       \"object\": \"allocation\",       \"attributes\": {         \"id\": 16,         \"ip\": \"45.86.168.218\",         \"alias\": null,         \"port\": 25578,         \"notes\": null,         \"assigned\": false       }     },     {       \"object\": \"allocation\",       \"attributes\": {         \"id\": 17,         \"ip\": \"45.86.168.218\",         \"alias\": null,         \"port\": 25579,         \"notes\": null,         \"assigned\": false       }     },     {       \"object\": \"allocation\",       \"attributes\": {         \"id\": 18,         \"ip\": \"45.86.168.218\",         \"alias\": null,         \"port\": 25580,         \"notes\": null,         \"assigned\": false       }     }   ],   \"meta\": {     \"pagination\": {       \"total\": 17,       \"count\": 17,       \"per_page\": 50,       \"current_page\": 1,       \"total_pages\": 1,       \"links\": {}     }   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import node_allocations_allocations_api
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
    api_instance = node_allocations_allocations_api.NodeAllocationsAllocationsApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ / ] List allocations
        api_response = api_instance.__listallocations(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling NodeAllocationsAllocationsApi->__listallocations: %s\n" % e)
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

