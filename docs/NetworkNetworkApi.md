# pterodactyl_client.NetworkNetworkApi

All URIs are relative to *https://example.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**__allocations_allocation_primary_setprimaryallocation**](NetworkNetworkApi.md#__allocations_allocation_primary_setprimaryallocation) | **POST** /client/servers/1a7ce997/network/allocations/1/primary | [ /allocations/{allocation}/primary ] Set primary allocation
[**__allocations_allocation_setallocationnote**](NetworkNetworkApi.md#__allocations_allocation_setallocationnote) | **POST** /client/servers/1a7ce997/network/allocations/2 | [ /allocations/{allocation} ] Set allocation note
[**__allocations_allocation_unassignallocation**](NetworkNetworkApi.md#__allocations_allocation_unassignallocation) | **DELETE** /client/servers/1a7ce997/network/allocations/2 | [ /allocations/{allocation} ] Unassign allocation
[**__allocations_assignallocation**](NetworkNetworkApi.md#__allocations_assignallocation) | **POST** /client/servers/1a7ce997/network/allocations | [ /allocations ] Assign allocation
[**__allocations_listallocations**](NetworkNetworkApi.md#__allocations_listallocations) | **GET** /client/servers/1a7ce997/network/allocations | [ /allocations ] List allocations


# **__allocations_allocation_primary_setprimaryallocation**
> bool, date, datetime, dict, float, int, list, str, none_type __allocations_allocation_primary_setprimaryallocation(accept)

[ /allocations/{allocation}/primary ] Set primary allocation

Sets the primary allocation  <!-- RESPONSE 200 --> {   \"object\": \"allocation\",   \"attributes\": {     \"id\": 2,     \"ip\": \"45.86.168.218\",     \"ip_alias\": null,     \"port\": 25566,     \"notes\": \"Votifier\",     \"is_default\": true   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import network_network_api
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
    api_instance = network_network_api.NetworkNetworkApi(api_client)
    accept = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /allocations/{allocation}/primary ] Set primary allocation
        api_response = api_instance.__allocations_allocation_primary_setprimaryallocation(accept)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling NetworkNetworkApi->__allocations_allocation_primary_setprimaryallocation: %s\n" % e)
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

# **__allocations_allocation_setallocationnote**
> bool, date, datetime, dict, float, int, list, str, none_type __allocations_allocation_setallocationnote(accept, allocations_allocation_setallocationnote_request)

[ /allocations/{allocation} ] Set allocation note

Sets a note for the allocation  # Fields | Name  | Required? | Type   | Description         | Rules | |-------|-----------|--------|---------------------|-------| | notes | required  | string | Note for allocation |       |  <!-- RESPONSE 200 --> {   \"object\": \"allocation\",   \"attributes\": {     \"id\": 2,     \"ip\": \"45.86.168.218\",     \"ip_alias\": null,     \"port\": 25566,     \"notes\": \"Votifier\",     \"is_default\": false   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import network_network_api
from pterodactyl_client.model.allocations_allocation_setallocationnote_request import AllocationsAllocationSetallocationnoteRequest
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
    api_instance = network_network_api.NetworkNetworkApi(api_client)
    accept = "application/json" # str | 
    allocations_allocation_setallocationnote_request = AllocationsAllocationSetallocationnoteRequest(None) # AllocationsAllocationSetallocationnoteRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ /allocations/{allocation} ] Set allocation note
        api_response = api_instance.__allocations_allocation_setallocationnote(accept, allocations_allocation_setallocationnote_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling NetworkNetworkApi->__allocations_allocation_setallocationnote: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **allocations_allocation_setallocationnote_request** | [**AllocationsAllocationSetallocationnoteRequest**](AllocationsAllocationSetallocationnoteRequest.md)|  |

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

# **__allocations_allocation_unassignallocation**
> bool, date, datetime, dict, float, int, list, str, none_type __allocations_allocation_unassignallocation(accept)

[ /allocations/{allocation} ] Unassign allocation

Deletes the specified non-primary allocation  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->  <!-- RESPONSE 400 --> {   \"errors\": [     {       \"code\": \"DisplayException\",       \"status\": \"400\",       \"detail\": \"Cannot delete the primary allocation for a server.\"     }   ] } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import network_network_api
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
    api_instance = network_network_api.NetworkNetworkApi(api_client)
    accept = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /allocations/{allocation} ] Unassign allocation
        api_response = api_instance.__allocations_allocation_unassignallocation(accept)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling NetworkNetworkApi->__allocations_allocation_unassignallocation: %s\n" % e)
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

# **__allocations_assignallocation**
> bool, date, datetime, dict, float, int, list, str, none_type __allocations_assignallocation(accept, content_type)

[ /allocations ] Assign allocation

Automatically assigns a new allocation if auto-assign is enabled on the instance  <!-- RESPONSE 200 --> {   \"object\": \"allocation\",   \"attributes\": {     \"id\": 6,     \"ip\": \"45.86.168.218\",     \"ip_alias\": null,     \"port\": 25570,     \"notes\": null,     \"is_default\": false   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import network_network_api
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
    api_instance = network_network_api.NetworkNetworkApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /allocations ] Assign allocation
        api_response = api_instance.__allocations_assignallocation(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling NetworkNetworkApi->__allocations_assignallocation: %s\n" % e)
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

# **__allocations_listallocations**
> bool, date, datetime, dict, float, int, list, str, none_type __allocations_listallocations(accept, content_type)

[ /allocations ] List allocations

Retrieves the network information for the specified server  <!-- RESPONSE 200 --> {   \"object\": \"list\",   \"data\": [     {       \"object\": \"allocation\",       \"attributes\": {         \"id\": 1,         \"ip\": \"45.86.168.218\",         \"ip_alias\": null,         \"port\": 25565,         \"notes\": null,         \"is_default\": true       }     },     {       \"object\": \"allocation\",       \"attributes\": {         \"id\": 2,         \"ip\": \"45.86.168.218\",         \"ip_alias\": null,         \"port\": 25566,         \"notes\": \"Votifier\",         \"is_default\": false       }     }   ] } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import network_network_api
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
    api_instance = network_network_api.NetworkNetworkApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /allocations ] List allocations
        api_response = api_instance.__allocations_listallocations(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling NetworkNetworkApi->__allocations_listallocations: %s\n" % e)
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

