# pterodactyl_client.NodesNodesApi

All URIs are relative to *https://example.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**__createnode**](NodesNodesApi.md#__createnode) | **POST** /application/nodes | [ / ] Create node
[**__listnodes**](NodesNodesApi.md#__listnodes) | **GET** /application/nodes | [ / ] List nodes
[**__node_configuration_nodeconfiguration**](NodesNodesApi.md#__node_configuration_nodeconfiguration) | **GET** /application/nodes/1/configuration | [ /{node}/configuration ] Node configuration
[**__node_deletenode**](NodesNodesApi.md#__node_deletenode) | **DELETE** /application/nodes/1 | [ /{node} ] Delete node
[**__node_nodedetails**](NodesNodesApi.md#__node_nodedetails) | **GET** /application/nodes/1 | [ /{node} ] Node details
[**__node_updatenode**](NodesNodesApi.md#__node_updatenode) | **PATCH** /application/nodes/1 | [ /{node} ] Update node


# **__createnode**
> bool, date, datetime, dict, float, int, list, str, none_type __createnode(accept, createnode_request)

[ / ] Create node

Creates a new node  <!-- RESPONSE 201 --> {   \"object\": \"node\",   \"attributes\": {     \"id\": 4,     \"uuid\": \"4158cfe9-2aa8-4812-bf6e-d88beeb08e98\",     \"public\": true,     \"name\": \"New Node\",     \"description\": null,     \"location_id\": 1,     \"fqdn\": \"node2.example.com\",     \"scheme\": \"https\",     \"behind_proxy\": false,     \"maintenance_mode\": false,     \"memory\": 10240,     \"memory_overallocate\": 0,     \"disk\": 50000,     \"disk_overallocate\": 0,     \"upload_size\": 100,     \"daemon_listen\": 8080,     \"daemon_sftp\": 2022,     \"daemon_base\": \"/var/lib/pterodactyl/volumes\",     \"created_at\": \"2020-10-29T01:17:38+00:00\",     \"updated_at\": \"2020-10-29T01:17:38+00:00\",     \"allocated_resources\": {       \"memory\": 0,       \"disk\": 0     }   },   \"meta\": {     \"resource\": \"https://pterodactyl.file.properties/api/application/nodes/4\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import nodes_nodes_api
from pterodactyl_client.model.createnode_request import CreatenodeRequest
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
    api_instance = nodes_nodes_api.NodesNodesApi(api_client)
    accept = "application/json" # str | 
    createnode_request = CreatenodeRequest(None) # CreatenodeRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ / ] Create node
        api_response = api_instance.__createnode(accept, createnode_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling NodesNodesApi->__createnode: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **createnode_request** | [**CreatenodeRequest**](CreatenodeRequest.md)|  |

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

# **__listnodes**
> bool, date, datetime, dict, float, int, list, str, none_type __listnodes(accept, content_type)

[ / ] List nodes

Retrieves a list of nodes  ## Available include parameters | Parameter   | Description                                            | |-------------|--------------------------------------------------------| | allocations | List of allocations added to the node                  | | location    | Information about the location the node is assigned to | | servers     | List of servers on the node                            |  <!-- RESPONSE 200 --> {   \"object\": \"list\",   \"data\": [     {       \"object\": \"node\",       \"attributes\": {         \"id\": 1,         \"uuid\": \"1046d1d1-b8ef-4771-82b1-2b5946d33397\",         \"public\": true,         \"name\": \"Test\",         \"description\": \"Test\",         \"location_id\": 1,         \"fqdn\": \"pterodactyl.file.properties\",         \"scheme\": \"https\",         \"behind_proxy\": false,         \"maintenance_mode\": false,         \"memory\": 2048,         \"memory_overallocate\": 0,         \"disk\": 5000,         \"disk_overallocate\": 0,         \"upload_size\": 100,         \"daemon_listen\": 8080,         \"daemon_sftp\": 2022,         \"daemon_base\": \"/srv/daemon-data\",         \"created_at\": \"2019-12-22T04:44:51+00:00\",         \"updated_at\": \"2019-12-22T04:44:51+00:00\"       }     },     {       \"object\": \"node\",       \"attributes\": {         \"id\": 3,         \"uuid\": \"71b15cf6-909a-4b60-aa04-abb4c8f98f61\",         \"public\": true,         \"name\": \"2\",         \"description\": \"e\",         \"location_id\": 1,         \"fqdn\": \"pterodactyl.file.properties\",         \"scheme\": \"https\",         \"behind_proxy\": false,         \"maintenance_mode\": false,         \"memory\": 100,         \"memory_overallocate\": 0,         \"disk\": 100,         \"disk_overallocate\": 0,         \"upload_size\": 100,         \"daemon_listen\": 8080,         \"daemon_sftp\": 2022,         \"daemon_base\": \"/var/lib/pterodactyl/volumes\",         \"created_at\": \"2020-06-23T04:50:37+00:00\",         \"updated_at\": \"2020-06-23T04:50:37+00:00\"       }     }   ],   \"meta\": {     \"pagination\": {       \"total\": 2,       \"count\": 2,       \"per_page\": 50,       \"current_page\": 1,       \"total_pages\": 1,       \"links\": {}     }   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import nodes_nodes_api
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
    api_instance = nodes_nodes_api.NodesNodesApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ / ] List nodes
        api_response = api_instance.__listnodes(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling NodesNodesApi->__listnodes: %s\n" % e)
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

# **__node_configuration_nodeconfiguration**
> bool, date, datetime, dict, float, int, list, str, none_type __node_configuration_nodeconfiguration(accept, content_type)

[ /{node}/configuration ] Node configuration

Displays the Wings configuration   <!-- RESPONSE 200 --> {   \"debug\": false,   \"uuid\": \"1046d1d1-b8ef-4771-82b1-2b5946d33397\",   \"token_id\": \"iAcosCn1KCAgVjVO\",   \"token\": \"FanPzLCptUxkGow3vi7Z\",   \"api\": {     \"host\": \"0.0.0.0\",     \"port\": 8080,     \"ssl\": {       \"enabled\": true,       \"cert\": \"/etc/letsencrypt/live/pterodactyl.file.properties/fullchain.pem\",       \"key\": \"/etc/letsencrypt/live/pterodactyl.file.properties/privkey.pem\"     },     \"upload_limit\": 100   },   \"system\": {     \"data\": \"/srv/daemon-data\",     \"sftp\": {       \"bind_port\": 2022     }   },   \"remote\": \"https://pterodactyl.file.properties\" } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import nodes_nodes_api
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
    api_instance = nodes_nodes_api.NodesNodesApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{node}/configuration ] Node configuration
        api_response = api_instance.__node_configuration_nodeconfiguration(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling NodesNodesApi->__node_configuration_nodeconfiguration: %s\n" % e)
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

# **__node_deletenode**
> bool, date, datetime, dict, float, int, list, str, none_type __node_deletenode(accept, content_type)

[ /{node} ] Delete node

Deletes the specified node  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import nodes_nodes_api
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
    api_instance = nodes_nodes_api.NodesNodesApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{node} ] Delete node
        api_response = api_instance.__node_deletenode(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling NodesNodesApi->__node_deletenode: %s\n" % e)
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

# **__node_nodedetails**
> bool, date, datetime, dict, float, int, list, str, none_type __node_nodedetails(accept, content_type)

[ /{node} ] Node details

Retrieves the specified node  ## Available include parameters | Parameter   | Description                                            | |-------------|--------------------------------------------------------| | allocations | List of allocations added to the node                  | | location    | Information about the location the node is assigned to | | servers     | List of servers on the node                            |  <!-- RESPONSE 200 --> {   \"object\": \"node\",   \"attributes\": {     \"id\": 1,     \"uuid\": \"1046d1d1-b8ef-4771-82b1-2b5946d33397\",     \"public\": true,     \"name\": \"Test\",     \"description\": \"Test\",     \"location_id\": 1,     \"fqdn\": \"pterodactyl.file.properties\",     \"scheme\": \"https\",     \"behind_proxy\": false,     \"maintenance_mode\": false,     \"memory\": 2048,     \"memory_overallocate\": 0,     \"disk\": 5000,     \"disk_overallocate\": 0,     \"upload_size\": 100,     \"daemon_listen\": 8080,     \"daemon_sftp\": 2022,     \"daemon_base\": \"/srv/daemon-data\",     \"created_at\": \"2019-12-22T04:44:51+00:00\",     \"updated_at\": \"2019-12-22T04:44:51+00:00\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import nodes_nodes_api
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
    api_instance = nodes_nodes_api.NodesNodesApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{node} ] Node details
        api_response = api_instance.__node_nodedetails(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling NodesNodesApi->__node_nodedetails: %s\n" % e)
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

# **__node_updatenode**
> bool, date, datetime, dict, float, int, list, str, none_type __node_updatenode(accept, node_updatenode_request)

[ /{node} ] Update node

Updates the node details  <!-- RESPONSE 200 --> {   \"object\": \"node\",   \"attributes\": {     \"id\": 1,     \"uuid\": \"1046d1d1-b8ef-4771-82b1-2b5946d33397\",     \"public\": true,     \"name\": \"Test Renamed\",     \"description\": \"Test\",     \"location_id\": 1,     \"fqdn\": \"pterodactyl.file.properties\",     \"scheme\": \"https\",     \"behind_proxy\": false,     \"maintenance_mode\": false,     \"memory\": 2048,     \"memory_overallocate\": 0,     \"disk\": 5000,     \"disk_overallocate\": 0,     \"upload_size\": 100,     \"daemon_listen\": 8080,     \"daemon_sftp\": 2022,     \"daemon_base\": \"/var/lib/pterodactyl/volumes\",     \"created_at\": \"2019-12-22T04:44:51+00:00\",     \"updated_at\": \"2020-10-29T01:20:23+00:00\",     \"mounts\": [],     \"allocated_resources\": {       \"memory\": 640,       \"disk\": 700     }   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import nodes_nodes_api
from pterodactyl_client.model.node_updatenode_request import NodeUpdatenodeRequest
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
    api_instance = nodes_nodes_api.NodesNodesApi(api_client)
    accept = "application/json" # str | 
    node_updatenode_request = NodeUpdatenodeRequest(None) # NodeUpdatenodeRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{node} ] Update node
        api_response = api_instance.__node_updatenode(accept, node_updatenode_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling NodesNodesApi->__node_updatenode: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **node_updatenode_request** | [**NodeUpdatenodeRequest**](NodeUpdatenodeRequest.md)|  |

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

