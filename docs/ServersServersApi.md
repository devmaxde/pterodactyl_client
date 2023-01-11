# pterodactyl_client.ServersServersApi

All URIs are relative to *https://example.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**__createserver**](ServersServersApi.md#__createserver) | **POST** /application/servers | [ / ] Create server
[**__listservers**](ServersServersApi.md#__listservers) | **GET** /application/servers | [ / ] List servers


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

# **__listservers**
> bool, date, datetime, dict, float, int, list, str, none_type __listservers(accept, content_type)

[ / ] List servers

Retrieves all servers  <!-- RESPONSE 200 --> {   \"object\": \"list\",   \"data\": [     {       \"object\": \"server\",       \"attributes\": {         \"id\": 5,         \"external_id\": \"RemoteId1\",         \"uuid\": \"{server_id}-259b-452e-8b4e-cecc464142ca\",         \"identifier\": \"{server_id}\",         \"name\": \"Wuhu Island\",         \"description\": \"Matt from Wii Sports\",         \"suspended\": false,         \"limits\": {           \"memory\": 512,           \"swap\": 0,           \"disk\": 200,           \"io\": 500,           \"cpu\": 0,           \"threads\": null         },         \"feature_limits\": {           \"databases\": 5,           \"allocations\": 5,           \"backups\": 2         },         \"user\": 1,         \"node\": 1,         \"allocation\": 1,         \"nest\": 1,         \"egg\": 5,         \"pack\": null,         \"container\": {           \"startup_command\": \"java -Xms128M -Xmx{{SERVER_MEMORY}}M -jar {{SERVER_JARFILE}}\",           \"image\": \"quay.io/pterodactyl/core:java\",           \"installed\": true,           \"environment\": {             \"SERVER_JARFILE\": \"server.jar\",             \"VANILLA_VERSION\": \"latest\",             \"STARTUP\": \"java -Xms128M -Xmx{{SERVER_MEMORY}}M -jar {{SERVER_JARFILE}}\",             \"P_SERVER_LOCATION\": \"Test\",             \"P_SERVER_UUID\": \"{server_id}-259b-452e-8b4e-cecc464142ca\"           }         },         \"updated_at\": \"2020-06-13T04:20:53+00:00\",         \"created_at\": \"2019-12-23T06:46:27+00:00\",         \"relationships\": {           \"databases\": {             \"object\": \"list\",             \"data\": [               {                 \"object\": \"databases\",                 \"attributes\": {                   \"id\": 1,                   \"server\": 5,                   \"host\": 4,                   \"database\": \"s5_perms\",                   \"username\": \"u5_QsIAp1jhvS\",                   \"remote\": \"%\",                   \"max_connections\": 0,                   \"created_at\": \"2020-06-12T23:00:13+01:00\",                   \"updated_at\": \"2020-06-12T23:00:13+01:00\"                 }               },               {                 \"object\": \"databases\",                 \"attributes\": {                   \"id\": 2,                   \"server\": 5,                   \"host\": 4,                   \"database\": \"s5_coreprotect\",                   \"username\": \"u5_2jtJx1nO1d\",                   \"remote\": \"%\",                   \"max_connections\": 0,                   \"created_at\": \"2020-06-12T23:00:20+01:00\",                   \"updated_at\": \"2020-06-12T23:00:20+01:00\"                 }               }             ]           }         }       }     }   ],   \"meta\": {     \"pagination\": {       \"total\": 1,       \"count\": 1,       \"per_page\": 50,       \"current_page\": 1,       \"total_pages\": 1,       \"links\": {}     }   } } <!-- ENDRESPONSE -->

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

