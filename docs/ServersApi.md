# pterodactyl_client.ServersApi

All URIs are relative to *https://example.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**application_servers_externalserver_id_get**](ServersApi.md#application_servers_externalserver_id_get) | **GET** /application/servers/external/{server_id} | [ /external/{external_id} ] Server details
[**application_servers_get**](ServersApi.md#application_servers_get) | **GET** /application/servers | [ / ] List servers
[**application_servers_post**](ServersApi.md#application_servers_post) | **POST** /application/servers | [ / ] Create server
[**application_serversserver_id_build_patch**](ServersApi.md#application_serversserver_id_build_patch) | **PATCH** /application/servers/{server_id}/build | [ /{server}/build ] Update build
[**application_serversserver_id_delete**](ServersApi.md#application_serversserver_id_delete) | **DELETE** /application/servers/{server_id} | [ /{server} ] Delete server
[**application_serversserver_id_details_patch**](ServersApi.md#application_serversserver_id_details_patch) | **PATCH** /application/servers/{server_id}/details | [ /{server}/details ] Update details
[**application_serversserver_id_force_delete**](ServersApi.md#application_serversserver_id_force_delete) | **DELETE** /application/servers/{server_id}/force | [ /{server}/{force?} ] Force delete server
[**application_serversserver_id_get**](ServersApi.md#application_serversserver_id_get) | **GET** /application/servers/{server_id} | [ /{server} ] Server details
[**application_serversserver_id_reinstall_post**](ServersApi.md#application_serversserver_id_reinstall_post) | **POST** /application/servers/{server_id}/reinstall | [ /{server}/reinstall ] Reinstall server
[**application_serversserver_id_startup_patch**](ServersApi.md#application_serversserver_id_startup_patch) | **PATCH** /application/servers/{server_id}/startup | [ /{server}/startup ] Update startup
[**application_serversserver_id_suspend_post**](ServersApi.md#application_serversserver_id_suspend_post) | **POST** /application/servers/{server_id}/suspend | [ /{server}/suspend ] Suspend server
[**application_serversserver_id_unsuspend_post**](ServersApi.md#application_serversserver_id_unsuspend_post) | **POST** /application/servers/{server_id}/unsuspend | [ /{server}/unsuspend ] Unsuspend server


# **application_servers_externalserver_id_get**
> bool, date, datetime, dict, float, int, list, str, none_type application_servers_externalserver_id_get(accept, content_type, server_id)

[ /external/{external_id} ] Server details

Retrieves a server by its external ID  ## Available include parameters | Parameter   | Description                                | |-------------|--------------------------------------------| | allocations | List of allocations assigned to the server | | user        | Information about the server owner         | | subusers    | List of users added to the server          | | pack        | Information about the server pack          | | nest        | Information about the server's egg nest    | | egg         | Information about the server's egg         | | variables   | List of server variables                   | | location    | Information about server's node location   | | node        | Information about the server's node        | | databases   | List of databases on the server            |  <!-- RESPONSE --> {   \"object\": \"server\",   \"attributes\": {     \"id\": 5,     \"external_id\": \"RemoteId1\",     \"uuid\": \"{server_id}-259b-452e-8b4e-cecc464142ca\",     \"identifier\": \"{server_id}\",     \"name\": \"Gaming\",     \"description\": \"Matt from Wii Sports\",     \"suspended\": false,     \"limits\": {       \"memory\": 512,       \"swap\": 0,       \"disk\": 200,       \"io\": 500,       \"cpu\": 0,       \"threads\": null     },     \"feature_limits\": {       \"databases\": 5,       \"allocations\": 5,       \"backups\": 2     },     \"user\": 1,     \"node\": 1,     \"allocation\": 1,     \"nest\": 1,     \"egg\": 5,     \"pack\": null,     \"container\": {       \"startup_command\": \"java -Xms128M -Xmx{{SERVER_MEMORY}}M -jar {{SERVER_JARFILE}}\",       \"image\": \"quay.io/pterodactyl/core:java\",       \"installed\": true,       \"environment\": {         \"SERVER_JARFILE\": \"server.jar\",         \"VANILLA_VERSION\": \"latest\",         \"STARTUP\": \"java -Xms128M -Xmx{{SERVER_MEMORY}}M -jar {{SERVER_JARFILE}}\",         \"P_SERVER_LOCATION\": \"GB\",         \"P_SERVER_UUID\": \"{server_id}-259b-452e-8b4e-cecc464142ca\",         \"P_SERVER_ALLOCATION_LIMIT\": 5       }     },     \"updated_at\": \"2020-07-19T15:22:39+00:00\",     \"created_at\": \"2019-12-23T06:46:27+00:00\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 
    server_id = "server_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /external/{external_id} ] Server details
        api_response = api_instance.application_servers_externalserver_id_get(accept, content_type, server_id)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->application_servers_externalserver_id_get: %s\n" % e)
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

# **application_servers_get**
> bool, date, datetime, dict, float, int, list, str, none_type application_servers_get(accept, content_type)

[ / ] List servers

Retrieves all servers  <!-- RESPONSE 200 --> {   \"object\": \"list\",   \"data\": [     {       \"object\": \"server\",       \"attributes\": {         \"id\": 5,         \"external_id\": \"RemoteId1\",         \"uuid\": \"{server_id}-259b-452e-8b4e-cecc464142ca\",         \"identifier\": \"{server_id}\",         \"name\": \"Wuhu Island\",         \"description\": \"Matt from Wii Sports\",         \"suspended\": false,         \"limits\": {           \"memory\": 512,           \"swap\": 0,           \"disk\": 200,           \"io\": 500,           \"cpu\": 0,           \"threads\": null         },         \"feature_limits\": {           \"databases\": 5,           \"allocations\": 5,           \"backups\": 2         },         \"user\": 1,         \"node\": 1,         \"allocation\": 1,         \"nest\": 1,         \"egg\": 5,         \"pack\": null,         \"container\": {           \"startup_command\": \"java -Xms128M -Xmx{{SERVER_MEMORY}}M -jar {{SERVER_JARFILE}}\",           \"image\": \"quay.io/pterodactyl/core:java\",           \"installed\": true,           \"environment\": {             \"SERVER_JARFILE\": \"server.jar\",             \"VANILLA_VERSION\": \"latest\",             \"STARTUP\": \"java -Xms128M -Xmx{{SERVER_MEMORY}}M -jar {{SERVER_JARFILE}}\",             \"P_SERVER_LOCATION\": \"Test\",             \"P_SERVER_UUID\": \"{server_id}-259b-452e-8b4e-cecc464142ca\"           }         },         \"updated_at\": \"2020-06-13T04:20:53+00:00\",         \"created_at\": \"2019-12-23T06:46:27+00:00\",         \"relationships\": {           \"databases\": {             \"object\": \"list\",             \"data\": [               {                 \"object\": \"databases\",                 \"attributes\": {                   \"id\": 1,                   \"server\": 5,                   \"host\": 4,                   \"database\": \"s5_perms\",                   \"username\": \"u5_QsIAp1jhvS\",                   \"remote\": \"%\",                   \"max_connections\": 0,                   \"created_at\": \"2020-06-12T23:00:13+01:00\",                   \"updated_at\": \"2020-06-12T23:00:13+01:00\"                 }               },               {                 \"object\": \"databases\",                 \"attributes\": {                   \"id\": 2,                   \"server\": 5,                   \"host\": 4,                   \"database\": \"s5_coreprotect\",                   \"username\": \"u5_2jtJx1nO1d\",                   \"remote\": \"%\",                   \"max_connections\": 0,                   \"created_at\": \"2020-06-12T23:00:20+01:00\",                   \"updated_at\": \"2020-06-12T23:00:20+01:00\"                 }               }             ]           }         }       }     }   ],   \"meta\": {     \"pagination\": {       \"total\": 1,       \"count\": 1,       \"per_page\": 50,       \"current_page\": 1,       \"total_pages\": 1,       \"links\": {}     }   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ / ] List servers
        api_response = api_instance.application_servers_get(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->application_servers_get: %s\n" % e)
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

# **application_servers_post**
> bool, date, datetime, dict, float, int, list, str, none_type application_servers_post(accept, application_servers_post_request)

[ / ] Create server

Creates a new server  <!-- RESPONSE 201 --> {   \"object\": \"server\",   \"attributes\": {     \"id\": 7,     \"external_id\": null,     \"uuid\": \"d557c19c-8b21-4456-a9e5-181beda429f4\",     \"identifier\": \"d557c19c\",     \"name\": \"Building\",     \"description\": \"\",     \"suspended\": false,     \"limits\": {       \"memory\": 128,       \"swap\": 0,       \"disk\": 512,       \"io\": 500,       \"cpu\": 100,       \"threads\": null     },     \"feature_limits\": {       \"databases\": 5,       \"allocations\": 0,       \"backups\": 1     },     \"user\": 1,     \"node\": 1,     \"allocation\": 17,     \"nest\": 1,     \"egg\": 1,     \"container\": {       \"startup_command\": \"java -Xms128M -Xmx128M -jar server.jar\",       \"image\": \"quay.io/pterodactyl/core:java\",       \"installed\": false,       \"environment\": {         \"BUNGEE_VERSION\": \"latest\",         \"SERVER_JARFILE\": \"server.jar\",         \"STARTUP\": \"java -Xms128M -Xmx128M -jar server.jar\",         \"P_SERVER_LOCATION\": \"GB\",         \"P_SERVER_UUID\": \"d557c19c-8b21-4456-a9e5-181beda429f4\",         \"P_SERVER_ALLOCATION_LIMIT\": 0       }     },     \"updated_at\": \"2020-10-29T01:38:59+00:00\",     \"created_at\": \"2020-10-29T01:38:59+00:00\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
from pterodactyl_client.model.application_servers_post_request import ApplicationServersPostRequest
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
    api_instance = servers_api.ServersApi(api_client)
    accept = "application/json" # str | 
    application_servers_post_request = ApplicationServersPostRequest(None) # ApplicationServersPostRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ / ] Create server
        api_response = api_instance.application_servers_post(accept, application_servers_post_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->application_servers_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **application_servers_post_request** | [**ApplicationServersPostRequest**](ApplicationServersPostRequest.md)|  |

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

# **application_serversserver_id_build_patch**
> bool, date, datetime, dict, float, int, list, str, none_type application_serversserver_id_build_patch(accept, server_id, application_servers_server_id_build_patch_request)

[ /{server}/build ] Update build

Updates the server build information  ## Fields | Name                       | Required?        | Type   | Description                                                                                                                                                                                                                                         | Rules | |----------------------------|------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------| | allocation                 | required         | number | ID of primary allocation                                                                                                                                                                                                                            |       | | memory                     | required_without | number | The maximum amount of memory allowed for this container. Setting this to 0 will allow unlimited memory in a container.                                                                                                                              |       | | swap                       | required_without | number | Setting this to 0 will disable swap space on this server. Setting to -1 will allow unlimited swap.                                                                                                                                                  |       | | io                         | required_without | number | IO performance of this server relative to other running containers                                                                                                                                                                                  |       | | cpu                        | required_without | number | Each physical core on the system is considered to be 100%. Setting this value to 0 will allow a server to use CPU time without restrictions.                                                                                                        |       | | disk                       | required_without | number | This server will not be allowed to boot if it is using more than this amount of space. If a server goes over this limit while running it will be safely stopped and locked until enough space is available. Set to 0 to allow unlimited disk usage. |       | | threads                    |                  | number | Enter the specific CPU cores that this process can run on, or leave blank to allow all cores. This can be a single number, or a comma seperated list. Example: 0, 0-1,3, or 0,1,3,4.                                                                |       | | feature_limits             | required         | object |                                                                                                                                                                                                                                                     |       | | feature_limits.databases   | present          | number | The total number of databases a user is allowed to create for this server.                                                                                                                                                                          |       | | feature_limits.backups     | present          | number | The total number of allocations a user is allowed to create for this server.                                                                                                                                                                        |       | | feature_limits.allocations |                  | number | The total number of allocations a user is allowed to create for this server.                                                                                                                                                                        |       |  <!-- RESPONSE --> {   \"object\": \"server\",   \"attributes\": {     \"id\": 5,     \"external_id\": \"RemoteID1\",     \"uuid\": \"{server_id}-259b-452e-8b4e-cecc464142ca\",     \"identifier\": \"{server_id}\",     \"name\": \"Gaming\",     \"description\": \"Matt from Wii Sports\",     \"suspended\": false,     \"limits\": {       \"memory\": 512,       \"swap\": 0,       \"disk\": 200,       \"io\": 500,       \"cpu\": 0,       \"threads\": null     },     \"feature_limits\": {       \"databases\": 5,       \"allocations\": 5,       \"backups\": 2     },     \"user\": 1,     \"node\": 1,     \"allocation\": 1,     \"nest\": 1,     \"egg\": 5,     \"container\": {       \"startup_command\": \"java -Xms128M -Xmx2014M -jar server.jar\",       \"image\": \"quay.io/pterodactyl/core:java\",       \"installed\": true,       \"environment\": {         \"SERVER_JARFILE\": \"server.jar\",         \"VANILLA_VERSION\": \"latest\",         \"STARTUP\": \"java -Xms128M -Xmx2048M -jar server.jar\",         \"P_SERVER_LOCATION\": \"GB\",         \"P_SERVER_UUID\": \"{server_id}-259b-452e-8b4e-cecc464142ca\",         \"P_SERVER_ALLOCATION_LIMIT\": 5       }     },     \"updated_at\": \"2020-11-04T21:11:26+00:00\",     \"created_at\": \"2019-12-23T06:46:27+00:00\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
from pterodactyl_client.model.application_servers_server_id_build_patch_request import ApplicationServersServerIdBuildPatchRequest
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
    api_instance = servers_api.ServersApi(api_client)
    accept = "application/json" # str | 
    server_id = "server_id_example" # str | 
    application_servers_server_id_build_patch_request = ApplicationServersServerIdBuildPatchRequest(None) # ApplicationServersServerIdBuildPatchRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{server}/build ] Update build
        api_response = api_instance.application_serversserver_id_build_patch(accept, server_id, application_servers_server_id_build_patch_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->application_serversserver_id_build_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **server_id** | **str**|  |
 **application_servers_server_id_build_patch_request** | [**ApplicationServersServerIdBuildPatchRequest**](ApplicationServersServerIdBuildPatchRequest.md)|  |

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

# **application_serversserver_id_delete**
> bool, date, datetime, dict, float, int, list, str, none_type application_serversserver_id_delete(accept, content_type, server_id)

[ /{server} ] Delete server

Deletes the specified server  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 
    server_id = "server_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{server} ] Delete server
        api_response = api_instance.application_serversserver_id_delete(accept, content_type, server_id)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->application_serversserver_id_delete: %s\n" % e)
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

# **application_serversserver_id_details_patch**
> bool, date, datetime, dict, float, int, list, str, none_type application_serversserver_id_details_patch(accept, server_id, application_servers_server_id_details_patch_request)

[ /{server}/details ] Update details

Updates the server details  ## Fields | Name        | Required? | Type        | Description                                | Rules | |-------------|-----------|-------------|--------------------------------------------|-------| | name        | required  | string | Name for the server                        |       | | user        | required  | number      | ID of the user which the server belongs to |       | | external_id |           | string      | External ID of the server                  |       | | description |           | string | Description of the server                  |       |  <!-- RESPONSE --> {   \"object\": \"server\",   \"attributes\": {     \"id\": 5,     \"external_id\": \"RemoteID1\",     \"uuid\": \"{server_id}-259b-452e-8b4e-cecc464142ca\",     \"identifier\": \"{server_id}\",     \"name\": \"Gaming\",     \"description\": \"Matt from Wii Sports\",     \"suspended\": false,     \"limits\": {       \"memory\": 512,       \"swap\": 0,       \"disk\": 200,       \"io\": 500,       \"cpu\": 0,       \"threads\": null     },     \"feature_limits\": {       \"databases\": 5,       \"allocations\": 5,       \"backups\": 2     },     \"user\": 1,     \"node\": 1,     \"allocation\": 1,     \"nest\": 1,     \"egg\": 5,     \"container\": {       \"startup_command\": \"java -Xms128M -Xmx2014M -jar server.jar\",       \"image\": \"quay.io/pterodactyl/core:java\",       \"installed\": true,       \"environment\": {         \"SERVER_JARFILE\": \"server.jar\",         \"VANILLA_VERSION\": \"latest\",         \"STARTUP\": \"java -Xms128M -Xmx2048M -jar server.jar\",         \"P_SERVER_LOCATION\": \"GB\",         \"P_SERVER_UUID\": \"{server_id}-259b-452e-8b4e-cecc464142ca\",         \"P_SERVER_ALLOCATION_LIMIT\": 5       }     },     \"updated_at\": \"2020-11-04T21:11:26+00:00\",     \"created_at\": \"2019-12-23T06:46:27+00:00\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
from pterodactyl_client.model.application_servers_server_id_details_patch_request import ApplicationServersServerIdDetailsPatchRequest
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
    api_instance = servers_api.ServersApi(api_client)
    accept = "application/json" # str | 
    server_id = "server_id_example" # str | 
    application_servers_server_id_details_patch_request = ApplicationServersServerIdDetailsPatchRequest(None) # ApplicationServersServerIdDetailsPatchRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{server}/details ] Update details
        api_response = api_instance.application_serversserver_id_details_patch(accept, server_id, application_servers_server_id_details_patch_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->application_serversserver_id_details_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **server_id** | **str**|  |
 **application_servers_server_id_details_patch_request** | [**ApplicationServersServerIdDetailsPatchRequest**](ApplicationServersServerIdDetailsPatchRequest.md)|  |

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

# **application_serversserver_id_force_delete**
> bool, date, datetime, dict, float, int, list, str, none_type application_serversserver_id_force_delete(accept, content_type, server_id)

[ /{server}/{force?} ] Force delete server

Forcefully deletes the specified server  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 
    server_id = "server_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{server}/{force?} ] Force delete server
        api_response = api_instance.application_serversserver_id_force_delete(accept, content_type, server_id)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->application_serversserver_id_force_delete: %s\n" % e)
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

# **application_serversserver_id_get**
> bool, date, datetime, dict, float, int, list, str, none_type application_serversserver_id_get(accept, content_type, server_id)

[ /{server} ] Server details

Retrieves the specified server  ## Available include parameters | Parameter   | Description                                | |-------------|--------------------------------------------| | allocations | List of allocations assigned to the server | | user        | Information about the server owner         | | subusers    | List of users added to the server          | | pack        | Information about the server pack          | | nest        | Information about the server's egg nest    | | egg         | Information about the server's egg         | | variables   | List of server variables                   | | location    | Information about server's node location   | | node        | Information about the server's node        | | databases   | List of databases on the server            |  <!-- RESPONSE 200 --> {   \"object\": \"server\",   \"attributes\": {     \"id\": 5,     \"external_id\": \"RemoteId1\",     \"uuid\": \"{server_id}-259b-452e-8b4e-cecc464142ca\",     \"identifier\": \"{server_id}\",     \"name\": \"Gaming\",     \"description\": \"Matt from Wii Sports\",     \"suspended\": false,     \"limits\": {       \"memory\": 512,       \"swap\": 0,       \"disk\": 200,       \"io\": 500,       \"cpu\": 0,       \"threads\": null     },     \"feature_limits\": {       \"databases\": 5,       \"allocations\": 5,       \"backups\": 2     },     \"user\": 1,     \"node\": 1,     \"allocation\": 1,     \"nest\": 1,     \"egg\": 5,     \"pack\": null,     \"container\": {       \"startup_command\": \"java -Xms128M -Xmx{{SERVER_MEMORY}}M -jar {{SERVER_JARFILE}}\",       \"image\": \"quay.io/pterodactyl/core:java\",       \"installed\": true,       \"environment\": {         \"SERVER_JARFILE\": \"server.jar\",         \"VANILLA_VERSION\": \"latest\",         \"STARTUP\": \"java -Xms128M -Xmx{{SERVER_MEMORY}}M -jar {{SERVER_JARFILE}}\",         \"P_SERVER_LOCATION\": \"GB\",         \"P_SERVER_UUID\": \"{server_id}-259b-452e-8b4e-cecc464142ca\",         \"P_SERVER_ALLOCATION_LIMIT\": 5       }     },     \"updated_at\": \"2020-07-19T15:22:39+00:00\",     \"created_at\": \"2019-12-23T06:46:27+00:00\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 
    server_id = "server_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{server} ] Server details
        api_response = api_instance.application_serversserver_id_get(accept, content_type, server_id)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->application_serversserver_id_get: %s\n" % e)
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

# **application_serversserver_id_reinstall_post**
> bool, date, datetime, dict, float, int, list, str, none_type application_serversserver_id_reinstall_post(accept, content_type, server_id)

[ /{server}/reinstall ] Reinstall server

Reinstalls the specified server  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 
    server_id = "server_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{server}/reinstall ] Reinstall server
        api_response = api_instance.application_serversserver_id_reinstall_post(accept, content_type, server_id)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->application_serversserver_id_reinstall_post: %s\n" % e)
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

# **application_serversserver_id_startup_patch**
> bool, date, datetime, dict, float, int, list, str, none_type application_serversserver_id_startup_patch(accept, server_id, application_servers_server_id_startup_patch_request)

[ /{server}/startup ] Update startup

Updates the server startup information  ## Fields | Name         | Required? | Type     | Description                                                                                                                                       | Rules | |--------------|-----------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------|-------| | startup      | required  | string   | Edit your server's startup command here. |       | | environment  | present   | object   | Environment variables that the egg requires/supports                                                                                              |       | | egg          | required  | string   | ID of the egg to use                                                                                                                              |       | | image        | required  | required | The Docker image to use for this server                                                                                                           |       | | skip_scripts | present   | required | If enabled, if the Egg has an install script, it will NOT be ran during install.                                                                  |       |  <!-- RESPONSE --> {   \"object\": \"server\",   \"attributes\": {     \"id\": 5,     \"external_id\": \"RemoteID1\",     \"uuid\": \"{server_id}-259b-452e-8b4e-cecc464142ca\",     \"identifier\": \"{server_id}\",     \"name\": \"Gaming\",     \"description\": \"Matt from Wii Sports\",     \"suspended\": false,     \"limits\": {       \"memory\": 512,       \"swap\": 0,       \"disk\": 200,       \"io\": 500,       \"cpu\": 0,       \"threads\": null     },     \"feature_limits\": {       \"databases\": 5,       \"allocations\": 5,       \"backups\": 2     },     \"user\": 1,     \"node\": 1,     \"allocation\": 1,     \"nest\": 1,     \"egg\": 5,     \"container\": {       \"startup_command\": \"java -Xms128M -Xmx2014M -jar server.jar\",       \"image\": \"quay.io/pterodactyl/core:java\",       \"installed\": true,       \"environment\": {         \"SERVER_JARFILE\": \"server.jar\",         \"VANILLA_VERSION\": \"latest\",         \"STARTUP\": \"java -Xms128M -Xmx2048M -jar server.jar\",         \"P_SERVER_LOCATION\": \"GB\",         \"P_SERVER_UUID\": \"{server_id}-259b-452e-8b4e-cecc464142ca\",         \"P_SERVER_ALLOCATION_LIMIT\": 5       }     },     \"updated_at\": \"2020-11-04T21:11:26+00:00\",     \"created_at\": \"2019-12-23T06:46:27+00:00\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
from pterodactyl_client.model.application_servers_server_id_startup_patch_request import ApplicationServersServerIdStartupPatchRequest
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
    api_instance = servers_api.ServersApi(api_client)
    accept = "application/json" # str | 
    server_id = "server_id_example" # str | 
    application_servers_server_id_startup_patch_request = ApplicationServersServerIdStartupPatchRequest(None) # ApplicationServersServerIdStartupPatchRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{server}/startup ] Update startup
        api_response = api_instance.application_serversserver_id_startup_patch(accept, server_id, application_servers_server_id_startup_patch_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->application_serversserver_id_startup_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **server_id** | **str**|  |
 **application_servers_server_id_startup_patch_request** | [**ApplicationServersServerIdStartupPatchRequest**](ApplicationServersServerIdStartupPatchRequest.md)|  |

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

# **application_serversserver_id_suspend_post**
> bool, date, datetime, dict, float, int, list, str, none_type application_serversserver_id_suspend_post(accept, content_type, server_id)

[ /{server}/suspend ] Suspend server

Suspends the specified server  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 
    server_id = "server_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{server}/suspend ] Suspend server
        api_response = api_instance.application_serversserver_id_suspend_post(accept, content_type, server_id)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->application_serversserver_id_suspend_post: %s\n" % e)
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

# **application_serversserver_id_unsuspend_post**
> bool, date, datetime, dict, float, int, list, str, none_type application_serversserver_id_unsuspend_post(accept, content_type, server_id)

[ /{server}/unsuspend ] Unsuspend server

Unuspends the specified   <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_api
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
    api_instance = servers_api.ServersApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 
    server_id = "server_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{server}/unsuspend ] Unsuspend server
        api_response = api_instance.application_serversserver_id_unsuspend_post(accept, content_type, server_id)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersApi->application_serversserver_id_unsuspend_post: %s\n" % e)
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

