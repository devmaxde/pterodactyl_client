# pterodactyl_client.ApiClientClientApi

All URIs are relative to *https://example.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**__permissions_showpermissions**](ApiClientClientApi.md#__permissions_showpermissions) | **GET** /client/permissions | [ /permissions ] Show permissions
[**get__listservers**](ApiClientClientApi.md#get__listservers) | **GET** /client | [ / ] List servers


# **__permissions_showpermissions**
> bool, date, datetime, dict, float, int, list, str, none_type __permissions_showpermissions(accept, content_type)

[ /permissions ] Show permissions

Retries all available permissions  This is used for the frontend  <!-- RESPONSE 200 --> {   \"object\": \"system_permissions\",   \"attributes\": {     \"permissions\": {       \"websocket\": {         \"description\": \"Allows the user to connect to the server websocket, giving them access to view console output and realtime server stats.\",         \"keys\": {           \"connect\": \"Allows a user to connect to the websocket instance for a server to stream the console.\"         }       },       \"control\": {         \"description\": \"Permissions that control a user's ability to control the power state of a server, or send commands.\",         \"keys\": {           \"console\": \"Allows a user to send commands to the server instance via the console.\",           \"start\": \"Allows a user to start the server if it is stopped.\",           \"stop\": \"Allows a user to stop a server if it is running.\",           \"restart\": \"Allows a user to perform a server restart. This allows them to start the server if it is offline, but not put the server in a completely stopped state.\"         }       },       \"user\": {         \"description\": \"Permissions that allow a user to manage other subusers on a server. They will never be able to edit their own account, or assign permissions they do not have themselves.\",         \"keys\": {           \"create\": \"Allows a user to create new subusers for the server.\",           \"read\": \"Allows the user to view subusers and their permissions for the server.\",           \"update\": \"Allows a user to modify other subusers.\",           \"delete\": \"Allows a user to delete a subuser from the server.\"         }       },       \"file\": {         \"description\": \"Permissions that control a user's ability to modify the filesystem for this server.\",         \"keys\": {           \"create\": \"Allows a user to create additional files and folders via the Panel or direct upload.\",           \"read\": \"Allows a user to view the contents of a directory and read the contents of a file. Users with this permission can also download files.\",           \"update\": \"Allows a user to update the contents of an existing file or directory.\",           \"delete\": \"Allows a user to delete files or directories.\",           \"archive\": \"Allows a user to archive the contents of a directory as well as decompress existing archives on the system.\",           \"sftp\": \"Allows a user to connect to SFTP and manage server files using the other assigned file permissions.\"         }       },       \"backup\": {         \"description\": \"Permissions that control a user's ability to generate and manage server backups.\",         \"keys\": {           \"create\": \"Allows a user to create new backups for this server.\",           \"read\": \"Allows a user to view all backups that exist for this server.\",           \"update\": \"\",           \"delete\": \"Allows a user to remove backups from the system.\",           \"download\": \"Allows a user to download backups.\"         }       },       \"allocation\": {         \"description\": \"Permissions that control a user's ability to modify the port allocations for this server.\",         \"keys\": {           \"read\": \"Allows a user to view the allocations assigned to this server.\",           \"create\": \"Allows a user to assign additional allocations to the server.\",           \"update\": \"Allows a user to change the primary server allocation and attach notes to each allocation.\",           \"delete\": \"Allows a user to delete an allocation from the server.\"         }       },       \"startup\": {         \"description\": \"Permissions that control a user's ability to view this server's startup parameters.\",         \"keys\": {           \"read\": \"\",           \"update\": \"\"         }       },       \"database\": {         \"description\": \"Permissions that control a user's access to the database management for this server.\",         \"keys\": {           \"create\": \"Allows a user to create a new database for this server.\",           \"read\": \"Allows a user to view the database associated with this server.\",           \"update\": \"Allows a user to rotate the password on a database instance. If the user does not have the view_password permission they will not see the updated password.\",           \"delete\": \"Allows a user to remove a database instance from this server.\",           \"view_password\": \"Allows a user to view the password associated with a database instance for this server.\"         }       },       \"schedule\": {         \"description\": \"Permissions that control a user's access to the schedule management for this server.\",         \"keys\": {           \"create\": \"\",           \"read\": \"\",           \"update\": \"\",           \"delete\": \"\"         }       },       \"settings\": {         \"description\": \"Permissions that control a user's access to the settings for this server.\",         \"keys\": {           \"rename\": \"\",           \"reinstall\": \"\"         }       }     }   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import api_client_client_api
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
    api_instance = api_client_client_api.ApiClientClientApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /permissions ] Show permissions
        api_response = api_instance.__permissions_showpermissions(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ApiClientClientApi->__permissions_showpermissions: %s\n" % e)
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

# **get__listservers**
> bool, date, datetime, dict, float, int, list, str, none_type get__listservers(accept)

[ / ] List servers

Lists all servers  ## Include parameters | Parameter | Description                               | |-----------|-------------------------------------------| | egg       | Information about the egg the server uses | | subusers  | List of subusers on the server            |  <!-- RESPONSE 200 --> {   \"object\": \"list\",   \"data\": [     {       \"object\": \"server\",       \"attributes\": {         \"server_owner\": true,         \"identifier\": \"1a7ce997\",         \"uuid\": \"1a7ce997-259b-452e-8b4e-cecc464142ca\",         \"name\": \"Gaming\",         \"node\": \"Test\",         \"sftp_details\": {           \"ip\": \"pterodactyl.file.properties\",           \"port\": 2022         },         \"description\": \"Matt from Wii Sports\",         \"limits\": {           \"memory\": 512,           \"swap\": 0,           \"disk\": 200,           \"io\": 500,           \"cpu\": 0         },         \"feature_limits\": {           \"databases\": 5,           \"allocations\": 5,           \"backups\": 2         },         \"is_suspended\": false,         \"is_installing\": false,         \"relationships\": {           \"allocations\": {             \"object\": \"list\",             \"data\": [               {                 \"object\": \"allocation\",                 \"attributes\": {                   \"id\": 1,                   \"ip\": \"45.86.168.218\",                   \"ip_alias\": null,                   \"port\": 25565,                   \"notes\": null,                   \"is_default\": true                 }               },               {                 \"object\": \"allocation\",                 \"attributes\": {                   \"id\": 2,                   \"ip\": \"45.86.168.218\",                   \"ip_alias\": null,                   \"port\": 25566,                   \"notes\": \"Votifier\",                   \"is_default\": false                 }               }             ]           }         }       }     }   ],   \"meta\": {     \"pagination\": {       \"total\": 1,       \"count\": 1,       \"per_page\": 50,       \"current_page\": 1,       \"total_pages\": 1,       \"links\": {}     }   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import api_client_client_api
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
    api_instance = api_client_client_api.ApiClientClientApi(api_client)
    accept = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ / ] List servers
        api_response = api_instance.get__listservers(accept)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling ApiClientClientApi->get__listservers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |

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

