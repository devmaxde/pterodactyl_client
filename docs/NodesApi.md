# pterodactyl_client.NodesApi

All URIs are relative to *https://example.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**application_nodesnode_id_configuration_get**](NodesApi.md#application_nodesnode_id_configuration_get) | **GET** /application/nodes/{node_id}/configuration | [ /{node}/configuration ] Node configuration
[**application_nodesnode_id_delete**](NodesApi.md#application_nodesnode_id_delete) | **DELETE** /application/nodes/{node_id} | [ /{node} ] Delete node
[**application_nodesnode_id_get**](NodesApi.md#application_nodesnode_id_get) | **GET** /application/nodes/{node_id} | [ /{node} ] Node details
[**application_nodesnode_id_patch**](NodesApi.md#application_nodesnode_id_patch) | **PATCH** /application/nodes/{node_id} | [ /{node} ] Update node


# **application_nodesnode_id_configuration_get**
> bool, date, datetime, dict, float, int, list, str, none_type application_nodesnode_id_configuration_get(accept, content_type, node_id)

[ /{node}/configuration ] Node configuration

Displays the Wings configuration   <!-- RESPONSE 200 --> {   \"debug\": false,   \"uuid\": \"1046d1d1-b8ef-4771-82b1-2b5946d33397\",   \"token_id\": \"iAcosCn1KCAgVjVO\",   \"token\": \"FanPzLCptUxkGow3vi7Z\",   \"api\": {     \"host\": \"0.0.0.0\",     \"port\": 8080,     \"ssl\": {       \"enabled\": true,       \"cert\": \"/etc/letsencrypt/live/pterodactyl.file.properties/fullchain.pem\",       \"key\": \"/etc/letsencrypt/live/pterodactyl.file.properties/privkey.pem\"     },     \"upload_limit\": 100   },   \"system\": {     \"data\": \"/srv/daemon-data\",     \"sftp\": {       \"bind_port\": 2022     }   },   \"remote\": \"https://pterodactyl.file.properties\" } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import nodes_api
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
    api_instance = nodes_api.NodesApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 
    node_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{node}/configuration ] Node configuration
        api_response = api_instance.application_nodesnode_id_configuration_get(accept, content_type, node_id)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling NodesApi->application_nodesnode_id_configuration_get: %s\n" % e)
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

# **application_nodesnode_id_delete**
> bool, date, datetime, dict, float, int, list, str, none_type application_nodesnode_id_delete(accept, content_type, node_id)

[ /{node} ] Delete node

Deletes the specified node  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import nodes_api
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
    api_instance = nodes_api.NodesApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 
    node_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{node} ] Delete node
        api_response = api_instance.application_nodesnode_id_delete(accept, content_type, node_id)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling NodesApi->application_nodesnode_id_delete: %s\n" % e)
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

# **application_nodesnode_id_get**
> bool, date, datetime, dict, float, int, list, str, none_type application_nodesnode_id_get(accept, content_type, node_id)

[ /{node} ] Node details

Retrieves the specified node  ## Available include parameters | Parameter   | Description                                            | |-------------|--------------------------------------------------------| | allocations | List of allocations added to the node                  | | location    | Information about the location the node is assigned to | | servers     | List of servers on the node                            |  <!-- RESPONSE 200 --> {   \"object\": \"node\",   \"attributes\": {     \"id\": 1,     \"uuid\": \"1046d1d1-b8ef-4771-82b1-2b5946d33397\",     \"public\": true,     \"name\": \"Test\",     \"description\": \"Test\",     \"location_id\": 1,     \"fqdn\": \"pterodactyl.file.properties\",     \"scheme\": \"https\",     \"behind_proxy\": false,     \"maintenance_mode\": false,     \"memory\": 2048,     \"memory_overallocate\": 0,     \"disk\": 5000,     \"disk_overallocate\": 0,     \"upload_size\": 100,     \"daemon_listen\": 8080,     \"daemon_sftp\": 2022,     \"daemon_base\": \"/srv/daemon-data\",     \"created_at\": \"2019-12-22T04:44:51+00:00\",     \"updated_at\": \"2019-12-22T04:44:51+00:00\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import nodes_api
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
    api_instance = nodes_api.NodesApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 
    node_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{node} ] Node details
        api_response = api_instance.application_nodesnode_id_get(accept, content_type, node_id)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling NodesApi->application_nodesnode_id_get: %s\n" % e)
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

# **application_nodesnode_id_patch**
> bool, date, datetime, dict, float, int, list, str, none_type application_nodesnode_id_patch(accept, node_id, application_nodes_node_id_patch_request)

[ /{node} ] Update node

Updates the node details  <!-- RESPONSE 200 --> {   \"object\": \"node\",   \"attributes\": {     \"id\": 1,     \"uuid\": \"1046d1d1-b8ef-4771-82b1-2b5946d33397\",     \"public\": true,     \"name\": \"Test Renamed\",     \"description\": \"Test\",     \"location_id\": 1,     \"fqdn\": \"pterodactyl.file.properties\",     \"scheme\": \"https\",     \"behind_proxy\": false,     \"maintenance_mode\": false,     \"memory\": 2048,     \"memory_overallocate\": 0,     \"disk\": 5000,     \"disk_overallocate\": 0,     \"upload_size\": 100,     \"daemon_listen\": 8080,     \"daemon_sftp\": 2022,     \"daemon_base\": \"/var/lib/pterodactyl/volumes\",     \"created_at\": \"2019-12-22T04:44:51+00:00\",     \"updated_at\": \"2020-10-29T01:20:23+00:00\",     \"mounts\": [],     \"allocated_resources\": {       \"memory\": 640,       \"disk\": 700     }   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import nodes_api
from pterodactyl_client.model.application_nodes_node_id_patch_request import ApplicationNodesNodeIdPatchRequest
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
    api_instance = nodes_api.NodesApi(api_client)
    accept = "application/json" # str | 
    node_id = 1 # int | 
    application_nodes_node_id_patch_request = ApplicationNodesNodeIdPatchRequest(None) # ApplicationNodesNodeIdPatchRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{node} ] Update node
        api_response = api_instance.application_nodesnode_id_patch(accept, node_id, application_nodes_node_id_patch_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling NodesApi->application_nodesnode_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **node_id** | **int**|  |
 **application_nodes_node_id_patch_request** | [**ApplicationNodesNodeIdPatchRequest**](ApplicationNodesNodeIdPatchRequest.md)|  |

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

