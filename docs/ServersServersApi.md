# pterodactyl_client.ServersServersApi

All URIs are relative to *https://example.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**__createserver**](ServersServersApi.md#__createserver) | **POST** /application/servers | [ / ] Create server
[**__external_external_id_serverdetails**](ServersServersApi.md#__external_external_id_serverdetails) | **GET** /application/servers/external/RemoteId1 | [ /external/{external_id} ] Server details
[**__listservers**](ServersServersApi.md#__listservers) | **GET** /application/servers | [ / ] List servers
[**__server_build_updatebuild**](ServersServersApi.md#__server_build_updatebuild) | **PATCH** /application/servers/5/build | [ /{server}/build ] Update build
[**__server_deleteserver**](ServersServersApi.md#__server_deleteserver) | **DELETE** /application/servers/1 | [ /{server} ] Delete server
[**__server_details_updatedetails**](ServersServersApi.md#__server_details_updatedetails) | **PATCH** /application/servers/5/details | [ /{server}/details ] Update details
[**__server_force_forcedeleteserver**](ServersServersApi.md#__server_force_forcedeleteserver) | **DELETE** /application/servers/1/force | [ /{server}/{force?} ] Force delete server
[**__server_reinstall_reinstallserver**](ServersServersApi.md#__server_reinstall_reinstallserver) | **POST** /application/servers/5/reinstall | [ /{server}/reinstall ] Reinstall server
[**__server_serverdetails**](ServersServersApi.md#__server_serverdetails) | **GET** /application/servers/5 | [ /{server} ] Server details
[**__server_startup_updatestartup**](ServersServersApi.md#__server_startup_updatestartup) | **PATCH** /application/servers/5/startup | [ /{server}/startup ] Update startup
[**__server_suspend_suspendserver**](ServersServersApi.md#__server_suspend_suspendserver) | **POST** /application/servers/5/suspend | [ /{server}/suspend ] Suspend server
[**__server_unsuspend_unsuspendserver**](ServersServersApi.md#__server_unsuspend_unsuspendserver) | **POST** /application/servers/5/unsuspend | [ /{server}/unsuspend ] Unsuspend server


# **__createserver**
> bool, date, datetime, dict, float, int, list, str, none_type __createserver(accept, createserver_request)

[ / ] Create server

Creates a new server  <!-- RESPONSE 201 --> {   \"object\": \"server\",   \"attributes\": {     \"id\": 7,     \"external_id\": null,     \"uuid\": \"d557c19c-8b21-4456-a9e5-181beda429f4\",     \"identifier\": \"d557c19c\",     \"name\": \"Building\",     \"description\": \"\",     \"suspended\": false,     \"limits\": {       \"memory\": 128,       \"swap\": 0,       \"disk\": 512,       \"io\": 500,       \"cpu\": 100,       \"threads\": null     },     \"feature_limits\": {       \"databases\": 5,       \"allocations\": 0,       \"backups\": 1     },     \"user\": 1,     \"node\": 1,     \"allocation\": 17,     \"nest\": 1,     \"egg\": 1,     \"container\": {       \"startup_command\": \"java -Xms128M -Xmx128M -jar server.jar\",       \"image\": \"quay.io/pterodactyl/core:java\",       \"installed\": false,       \"environment\": {         \"BUNGEE_VERSION\": \"latest\",         \"SERVER_JARFILE\": \"server.jar\",         \"STARTUP\": \"java -Xms128M -Xmx128M -jar server.jar\",         \"P_SERVER_LOCATION\": \"GB\",         \"P_SERVER_UUID\": \"d557c19c-8b21-4456-a9e5-181beda429f4\",         \"P_SERVER_ALLOCATION_LIMIT\": 0       }     },     \"updated_at\": \"2020-10-29T01:38:59+00:00\",     \"created_at\": \"2020-10-29T01:38:59+00:00\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_servers_api
from pterodactyl_client.model.createserver_request import CreateserverRequest
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
    api_instance = servers_servers_api.ServersServersApi(api_client)
    accept = "application/json" # str | 
    createserver_request = CreateserverRequest(None) # CreateserverRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ / ] Create server
        api_response = api_instance.__createserver(accept, createserver_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersServersApi->__createserver: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **createserver_request** | [**CreateserverRequest**](CreateserverRequest.md)|  |

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

# **__external_external_id_serverdetails**
> bool, date, datetime, dict, float, int, list, str, none_type __external_external_id_serverdetails(accept, content_type)

[ /external/{external_id} ] Server details

Retrieves a server by its external ID  ## Available include parameters | Parameter   | Description                                | |-------------|--------------------------------------------| | allocations | List of allocations assigned to the server | | user        | Information about the server owner         | | subusers    | List of users added to the server          | | pack        | Information about the server pack          | | nest        | Information about the server's egg nest    | | egg         | Information about the server's egg         | | variables   | List of server variables                   | | location    | Information about server's node location   | | node        | Information about the server's node        | | databases   | List of databases on the server            |  <!-- RESPONSE --> {   \"object\": \"server\",   \"attributes\": {     \"id\": 5,     \"external_id\": \"RemoteId1\",     \"uuid\": \"1a7ce997-259b-452e-8b4e-cecc464142ca\",     \"identifier\": \"1a7ce997\",     \"name\": \"Gaming\",     \"description\": \"Matt from Wii Sports\",     \"suspended\": false,     \"limits\": {       \"memory\": 512,       \"swap\": 0,       \"disk\": 200,       \"io\": 500,       \"cpu\": 0,       \"threads\": null     },     \"feature_limits\": {       \"databases\": 5,       \"allocations\": 5,       \"backups\": 2     },     \"user\": 1,     \"node\": 1,     \"allocation\": 1,     \"nest\": 1,     \"egg\": 5,     \"pack\": null,     \"container\": {       \"startup_command\": \"java -Xms128M -Xmx{{SERVER_MEMORY}}M -jar {{SERVER_JARFILE}}\",       \"image\": \"quay.io/pterodactyl/core:java\",       \"installed\": true,       \"environment\": {         \"SERVER_JARFILE\": \"server.jar\",         \"VANILLA_VERSION\": \"latest\",         \"STARTUP\": \"java -Xms128M -Xmx{{SERVER_MEMORY}}M -jar {{SERVER_JARFILE}}\",         \"P_SERVER_LOCATION\": \"GB\",         \"P_SERVER_UUID\": \"1a7ce997-259b-452e-8b4e-cecc464142ca\",         \"P_SERVER_ALLOCATION_LIMIT\": 5       }     },     \"updated_at\": \"2020-07-19T15:22:39+00:00\",     \"created_at\": \"2019-12-23T06:46:27+00:00\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_servers_api
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
    api_instance = servers_servers_api.ServersServersApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /external/{external_id} ] Server details
        api_response = api_instance.__external_external_id_serverdetails(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersServersApi->__external_external_id_serverdetails: %s\n" % e)
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

# **__listservers**
> bool, date, datetime, dict, float, int, list, str, none_type __listservers(accept, content_type)

[ / ] List servers

Retrieves all servers  <!-- RESPONSE 200 --> {   \"object\": \"list\",   \"data\": [     {       \"object\": \"server\",       \"attributes\": {         \"id\": 5,         \"external_id\": \"RemoteId1\",         \"uuid\": \"1a7ce997-259b-452e-8b4e-cecc464142ca\",         \"identifier\": \"1a7ce997\",         \"name\": \"Wuhu Island\",         \"description\": \"Matt from Wii Sports\",         \"suspended\": false,         \"limits\": {           \"memory\": 512,           \"swap\": 0,           \"disk\": 200,           \"io\": 500,           \"cpu\": 0,           \"threads\": null         },         \"feature_limits\": {           \"databases\": 5,           \"allocations\": 5,           \"backups\": 2         },         \"user\": 1,         \"node\": 1,         \"allocation\": 1,         \"nest\": 1,         \"egg\": 5,         \"pack\": null,         \"container\": {           \"startup_command\": \"java -Xms128M -Xmx{{SERVER_MEMORY}}M -jar {{SERVER_JARFILE}}\",           \"image\": \"quay.io/pterodactyl/core:java\",           \"installed\": true,           \"environment\": {             \"SERVER_JARFILE\": \"server.jar\",             \"VANILLA_VERSION\": \"latest\",             \"STARTUP\": \"java -Xms128M -Xmx{{SERVER_MEMORY}}M -jar {{SERVER_JARFILE}}\",             \"P_SERVER_LOCATION\": \"Test\",             \"P_SERVER_UUID\": \"1a7ce997-259b-452e-8b4e-cecc464142ca\"           }         },         \"updated_at\": \"2020-06-13T04:20:53+00:00\",         \"created_at\": \"2019-12-23T06:46:27+00:00\",         \"relationships\": {           \"databases\": {             \"object\": \"list\",             \"data\": [               {                 \"object\": \"databases\",                 \"attributes\": {                   \"id\": 1,                   \"server\": 5,                   \"host\": 4,                   \"database\": \"s5_perms\",                   \"username\": \"u5_QsIAp1jhvS\",                   \"remote\": \"%\",                   \"max_connections\": 0,                   \"created_at\": \"2020-06-12T23:00:13+01:00\",                   \"updated_at\": \"2020-06-12T23:00:13+01:00\"                 }               },               {                 \"object\": \"databases\",                 \"attributes\": {                   \"id\": 2,                   \"server\": 5,                   \"host\": 4,                   \"database\": \"s5_coreprotect\",                   \"username\": \"u5_2jtJx1nO1d\",                   \"remote\": \"%\",                   \"max_connections\": 0,                   \"created_at\": \"2020-06-12T23:00:20+01:00\",                   \"updated_at\": \"2020-06-12T23:00:20+01:00\"                 }               }             ]           }         }       }     }   ],   \"meta\": {     \"pagination\": {       \"total\": 1,       \"count\": 1,       \"per_page\": 50,       \"current_page\": 1,       \"total_pages\": 1,       \"links\": {}     }   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_servers_api
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
    api_instance = servers_servers_api.ServersServersApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ / ] List servers
        api_response = api_instance.__listservers(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersServersApi->__listservers: %s\n" % e)
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

# **__server_build_updatebuild**
> bool, date, datetime, dict, float, int, list, str, none_type __server_build_updatebuild(accept, server_build_updatebuild_request)

[ /{server}/build ] Update build

Updates the server build information  ## Fields | Name                       | Required?        | Type   | Description                                                                                                                                                                                                                                         | Rules | |----------------------------|------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------| | allocation                 | required         | number | ID of primary allocation                                                                                                                                                                                                                            |       | | memory                     | required_without | number | The maximum amount of memory allowed for this container. Setting this to 0 will allow unlimited memory in a container.                                                                                                                              |       | | swap                       | required_without | number | Setting this to 0 will disable swap space on this server. Setting to -1 will allow unlimited swap.                                                                                                                                                  |       | | io                         | required_without | number | IO performance of this server relative to other running containers                                                                                                                                                                                  |       | | cpu                        | required_without | number | Each physical core on the system is considered to be 100%. Setting this value to 0 will allow a server to use CPU time without restrictions.                                                                                                        |       | | disk                       | required_without | number | This server will not be allowed to boot if it is using more than this amount of space. If a server goes over this limit while running it will be safely stopped and locked until enough space is available. Set to 0 to allow unlimited disk usage. |       | | threads                    |                  | number | Enter the specific CPU cores that this process can run on, or leave blank to allow all cores. This can be a single number, or a comma seperated list. Example: 0, 0-1,3, or 0,1,3,4.                                                                |       | | feature_limits             | required         | object |                                                                                                                                                                                                                                                     |       | | feature_limits.databases   | present          | number | The total number of databases a user is allowed to create for this server.                                                                                                                                                                          |       | | feature_limits.backups     | present          | number | The total number of allocations a user is allowed to create for this server.                                                                                                                                                                        |       | | feature_limits.allocations |                  | number | The total number of allocations a user is allowed to create for this server.                                                                                                                                                                        |       |  <!-- RESPONSE --> {   \"object\": \"server\",   \"attributes\": {     \"id\": 5,     \"external_id\": \"RemoteID1\",     \"uuid\": \"1a7ce997-259b-452e-8b4e-cecc464142ca\",     \"identifier\": \"1a7ce997\",     \"name\": \"Gaming\",     \"description\": \"Matt from Wii Sports\",     \"suspended\": false,     \"limits\": {       \"memory\": 512,       \"swap\": 0,       \"disk\": 200,       \"io\": 500,       \"cpu\": 0,       \"threads\": null     },     \"feature_limits\": {       \"databases\": 5,       \"allocations\": 5,       \"backups\": 2     },     \"user\": 1,     \"node\": 1,     \"allocation\": 1,     \"nest\": 1,     \"egg\": 5,     \"container\": {       \"startup_command\": \"java -Xms128M -Xmx2014M -jar server.jar\",       \"image\": \"quay.io/pterodactyl/core:java\",       \"installed\": true,       \"environment\": {         \"SERVER_JARFILE\": \"server.jar\",         \"VANILLA_VERSION\": \"latest\",         \"STARTUP\": \"java -Xms128M -Xmx2048M -jar server.jar\",         \"P_SERVER_LOCATION\": \"GB\",         \"P_SERVER_UUID\": \"1a7ce997-259b-452e-8b4e-cecc464142ca\",         \"P_SERVER_ALLOCATION_LIMIT\": 5       }     },     \"updated_at\": \"2020-11-04T21:11:26+00:00\",     \"created_at\": \"2019-12-23T06:46:27+00:00\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_servers_api
from pterodactyl_client.model.server_build_updatebuild_request import ServerBuildUpdatebuildRequest
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
    api_instance = servers_servers_api.ServersServersApi(api_client)
    accept = "application/json" # str | 
    server_build_updatebuild_request = ServerBuildUpdatebuildRequest(None) # ServerBuildUpdatebuildRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{server}/build ] Update build
        api_response = api_instance.__server_build_updatebuild(accept, server_build_updatebuild_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersServersApi->__server_build_updatebuild: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **server_build_updatebuild_request** | [**ServerBuildUpdatebuildRequest**](ServerBuildUpdatebuildRequest.md)|  |

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

# **__server_deleteserver**
> bool, date, datetime, dict, float, int, list, str, none_type __server_deleteserver(accept, content_type)

[ /{server} ] Delete server

Deletes the specified server  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_servers_api
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
    api_instance = servers_servers_api.ServersServersApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{server} ] Delete server
        api_response = api_instance.__server_deleteserver(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersServersApi->__server_deleteserver: %s\n" % e)
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

# **__server_details_updatedetails**
> bool, date, datetime, dict, float, int, list, str, none_type __server_details_updatedetails(accept, server_details_updatedetails_request)

[ /{server}/details ] Update details

Updates the server details  ## Fields | Name        | Required? | Type        | Description                                | Rules | |-------------|-----------|-------------|--------------------------------------------|-------| | name        | required  | string | Name for the server                        |       | | user        | required  | number      | ID of the user which the server belongs to |       | | external_id |           | string      | External ID of the server                  |       | | description |           | string | Description of the server                  |       |  <!-- RESPONSE --> {   \"object\": \"server\",   \"attributes\": {     \"id\": 5,     \"external_id\": \"RemoteID1\",     \"uuid\": \"1a7ce997-259b-452e-8b4e-cecc464142ca\",     \"identifier\": \"1a7ce997\",     \"name\": \"Gaming\",     \"description\": \"Matt from Wii Sports\",     \"suspended\": false,     \"limits\": {       \"memory\": 512,       \"swap\": 0,       \"disk\": 200,       \"io\": 500,       \"cpu\": 0,       \"threads\": null     },     \"feature_limits\": {       \"databases\": 5,       \"allocations\": 5,       \"backups\": 2     },     \"user\": 1,     \"node\": 1,     \"allocation\": 1,     \"nest\": 1,     \"egg\": 5,     \"container\": {       \"startup_command\": \"java -Xms128M -Xmx2014M -jar server.jar\",       \"image\": \"quay.io/pterodactyl/core:java\",       \"installed\": true,       \"environment\": {         \"SERVER_JARFILE\": \"server.jar\",         \"VANILLA_VERSION\": \"latest\",         \"STARTUP\": \"java -Xms128M -Xmx2048M -jar server.jar\",         \"P_SERVER_LOCATION\": \"GB\",         \"P_SERVER_UUID\": \"1a7ce997-259b-452e-8b4e-cecc464142ca\",         \"P_SERVER_ALLOCATION_LIMIT\": 5       }     },     \"updated_at\": \"2020-11-04T21:11:26+00:00\",     \"created_at\": \"2019-12-23T06:46:27+00:00\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_servers_api
from pterodactyl_client.model.server_details_updatedetails_request import ServerDetailsUpdatedetailsRequest
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
    api_instance = servers_servers_api.ServersServersApi(api_client)
    accept = "application/json" # str | 
    server_details_updatedetails_request = ServerDetailsUpdatedetailsRequest(None) # ServerDetailsUpdatedetailsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{server}/details ] Update details
        api_response = api_instance.__server_details_updatedetails(accept, server_details_updatedetails_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersServersApi->__server_details_updatedetails: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **server_details_updatedetails_request** | [**ServerDetailsUpdatedetailsRequest**](ServerDetailsUpdatedetailsRequest.md)|  |

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

# **__server_force_forcedeleteserver**
> bool, date, datetime, dict, float, int, list, str, none_type __server_force_forcedeleteserver(accept, content_type)

[ /{server}/{force?} ] Force delete server

Forcefully deletes the specified server  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_servers_api
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
    api_instance = servers_servers_api.ServersServersApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{server}/{force?} ] Force delete server
        api_response = api_instance.__server_force_forcedeleteserver(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersServersApi->__server_force_forcedeleteserver: %s\n" % e)
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

# **__server_reinstall_reinstallserver**
> bool, date, datetime, dict, float, int, list, str, none_type __server_reinstall_reinstallserver(accept, content_type)

[ /{server}/reinstall ] Reinstall server

Reinstalls the specified server  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_servers_api
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
    api_instance = servers_servers_api.ServersServersApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{server}/reinstall ] Reinstall server
        api_response = api_instance.__server_reinstall_reinstallserver(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersServersApi->__server_reinstall_reinstallserver: %s\n" % e)
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

# **__server_serverdetails**
> bool, date, datetime, dict, float, int, list, str, none_type __server_serverdetails(accept, content_type)

[ /{server} ] Server details

Retrieves the specified server  ## Available include parameters | Parameter   | Description                                | |-------------|--------------------------------------------| | allocations | List of allocations assigned to the server | | user        | Information about the server owner         | | subusers    | List of users added to the server          | | pack        | Information about the server pack          | | nest        | Information about the server's egg nest    | | egg         | Information about the server's egg         | | variables   | List of server variables                   | | location    | Information about server's node location   | | node        | Information about the server's node        | | databases   | List of databases on the server            |  <!-- RESPONSE 200 --> {   \"object\": \"server\",   \"attributes\": {     \"id\": 5,     \"external_id\": \"RemoteId1\",     \"uuid\": \"1a7ce997-259b-452e-8b4e-cecc464142ca\",     \"identifier\": \"1a7ce997\",     \"name\": \"Gaming\",     \"description\": \"Matt from Wii Sports\",     \"suspended\": false,     \"limits\": {       \"memory\": 512,       \"swap\": 0,       \"disk\": 200,       \"io\": 500,       \"cpu\": 0,       \"threads\": null     },     \"feature_limits\": {       \"databases\": 5,       \"allocations\": 5,       \"backups\": 2     },     \"user\": 1,     \"node\": 1,     \"allocation\": 1,     \"nest\": 1,     \"egg\": 5,     \"pack\": null,     \"container\": {       \"startup_command\": \"java -Xms128M -Xmx{{SERVER_MEMORY}}M -jar {{SERVER_JARFILE}}\",       \"image\": \"quay.io/pterodactyl/core:java\",       \"installed\": true,       \"environment\": {         \"SERVER_JARFILE\": \"server.jar\",         \"VANILLA_VERSION\": \"latest\",         \"STARTUP\": \"java -Xms128M -Xmx{{SERVER_MEMORY}}M -jar {{SERVER_JARFILE}}\",         \"P_SERVER_LOCATION\": \"GB\",         \"P_SERVER_UUID\": \"1a7ce997-259b-452e-8b4e-cecc464142ca\",         \"P_SERVER_ALLOCATION_LIMIT\": 5       }     },     \"updated_at\": \"2020-07-19T15:22:39+00:00\",     \"created_at\": \"2019-12-23T06:46:27+00:00\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_servers_api
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
    api_instance = servers_servers_api.ServersServersApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{server} ] Server details
        api_response = api_instance.__server_serverdetails(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersServersApi->__server_serverdetails: %s\n" % e)
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

# **__server_startup_updatestartup**
> bool, date, datetime, dict, float, int, list, str, none_type __server_startup_updatestartup(accept, server_startup_updatestartup_request)

[ /{server}/startup ] Update startup

Updates the server startup information  ## Fields | Name         | Required? | Type     | Description                                                                                                                                       | Rules | |--------------|-----------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------|-------| | startup      | required  | string   | Edit your server's startup command here. |       | | environment  | present   | object   | Environment variables that the egg requires/supports                                                                                              |       | | egg          | required  | string   | ID of the egg to use                                                                                                                              |       | | image        | required  | required | The Docker image to use for this server                                                                                                           |       | | skip_scripts | present   | required | If enabled, if the Egg has an install script, it will NOT be ran during install.                                                                  |       |  <!-- RESPONSE --> {   \"object\": \"server\",   \"attributes\": {     \"id\": 5,     \"external_id\": \"RemoteID1\",     \"uuid\": \"1a7ce997-259b-452e-8b4e-cecc464142ca\",     \"identifier\": \"1a7ce997\",     \"name\": \"Gaming\",     \"description\": \"Matt from Wii Sports\",     \"suspended\": false,     \"limits\": {       \"memory\": 512,       \"swap\": 0,       \"disk\": 200,       \"io\": 500,       \"cpu\": 0,       \"threads\": null     },     \"feature_limits\": {       \"databases\": 5,       \"allocations\": 5,       \"backups\": 2     },     \"user\": 1,     \"node\": 1,     \"allocation\": 1,     \"nest\": 1,     \"egg\": 5,     \"container\": {       \"startup_command\": \"java -Xms128M -Xmx2014M -jar server.jar\",       \"image\": \"quay.io/pterodactyl/core:java\",       \"installed\": true,       \"environment\": {         \"SERVER_JARFILE\": \"server.jar\",         \"VANILLA_VERSION\": \"latest\",         \"STARTUP\": \"java -Xms128M -Xmx2048M -jar server.jar\",         \"P_SERVER_LOCATION\": \"GB\",         \"P_SERVER_UUID\": \"1a7ce997-259b-452e-8b4e-cecc464142ca\",         \"P_SERVER_ALLOCATION_LIMIT\": 5       }     },     \"updated_at\": \"2020-11-04T21:11:26+00:00\",     \"created_at\": \"2019-12-23T06:46:27+00:00\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_servers_api
from pterodactyl_client.model.server_startup_updatestartup_request import ServerStartupUpdatestartupRequest
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
    api_instance = servers_servers_api.ServersServersApi(api_client)
    accept = "application/json" # str | 
    server_startup_updatestartup_request = ServerStartupUpdatestartupRequest(None) # ServerStartupUpdatestartupRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{server}/startup ] Update startup
        api_response = api_instance.__server_startup_updatestartup(accept, server_startup_updatestartup_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersServersApi->__server_startup_updatestartup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **server_startup_updatestartup_request** | [**ServerStartupUpdatestartupRequest**](ServerStartupUpdatestartupRequest.md)|  |

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

# **__server_suspend_suspendserver**
> bool, date, datetime, dict, float, int, list, str, none_type __server_suspend_suspendserver(accept, content_type)

[ /{server}/suspend ] Suspend server

Suspends the specified server  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_servers_api
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
    api_instance = servers_servers_api.ServersServersApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{server}/suspend ] Suspend server
        api_response = api_instance.__server_suspend_suspendserver(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersServersApi->__server_suspend_suspendserver: %s\n" % e)
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

# **__server_unsuspend_unsuspendserver**
> bool, date, datetime, dict, float, int, list, str, none_type __server_unsuspend_unsuspendserver(accept, content_type)

[ /{server}/unsuspend ] Unsuspend server

Unuspends the specified   <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import servers_servers_api
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
    api_instance = servers_servers_api.ServersServersApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{server}/unsuspend ] Unsuspend server
        api_response = api_instance.__server_unsuspend_unsuspendserver(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ServersServersApi->__server_unsuspend_unsuspendserver: %s\n" % e)
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

