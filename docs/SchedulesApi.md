# pterodactyl_client.SchedulesApi

All URIs are relative to *https://example.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**client_serversserver_id_schedules_get**](SchedulesApi.md#client_serversserver_id_schedules_get) | **GET** /client/servers/{server_id}/schedules | [ / ] List schedules
[**client_serversserver_id_schedules_post**](SchedulesApi.md#client_serversserver_id_schedules_post) | **POST** /client/servers/{server_id}/schedules | [ / ] Create schedule
[**client_serversserver_id_schedulesschedule_id_delete**](SchedulesApi.md#client_serversserver_id_schedulesschedule_id_delete) | **DELETE** /client/servers/{server_id}/schedules/{schedule_id} | [ /{schedule} ] Delete schedule
[**client_serversserver_id_schedulesschedule_id_get**](SchedulesApi.md#client_serversserver_id_schedulesschedule_id_get) | **GET** /client/servers/{server_id}/schedules/{schedule_id} | [ /{schedule} ] Schedule details
[**client_serversserver_id_schedulesschedule_id_post**](SchedulesApi.md#client_serversserver_id_schedulesschedule_id_post) | **POST** /client/servers/{server_id}/schedules/{schedule_id} | [ /{schedule} ] Update schedule
[**client_serversserver_id_schedulesschedule_id_tasks_post**](SchedulesApi.md#client_serversserver_id_schedulesschedule_id_tasks_post) | **POST** /client/servers/{server_id}/schedules/{schedule_id}/tasks | [ /{schedule}/tasks ] Create task
[**client_serversserver_id_schedulesschedule_id_taskstask_id_delete**](SchedulesApi.md#client_serversserver_id_schedulesschedule_id_taskstask_id_delete) | **DELETE** /client/servers/{server_id}/schedules/{schedule_id}/tasks/{task_id} | [ /{schedule}/tasks/{task} ] Delete  task
[**client_serversserver_id_schedulesschedule_id_taskstask_id_post**](SchedulesApi.md#client_serversserver_id_schedulesschedule_id_taskstask_id_post) | **POST** /client/servers/{server_id}/schedules/{schedule_id}/tasks/{task_id} | [ /{schedule}/tasks/{task} ] Update task


# **client_serversserver_id_schedules_get**
> bool, date, datetime, dict, float, int, list, str, none_type client_serversserver_id_schedules_get(accept, content_type, server_id)

[ / ] List schedules

Lists all schedules added to the server  <!-- RESPONSE 200 --> {   \"object\": \"list\",   \"data\": [     {       \"object\": \"server_schedule\",       \"attributes\": {         \"id\": 1,         \"name\": \"Daily Reboot\",         \"cron\": {           \"day_of_week\": \"*\",           \"day_of_month\": \"*\",           \"hour\": \"0\",           \"minute\": \"0\"         },         \"is_active\": true,         \"is_processing\": false,         \"last_run_at\": null,         \"next_run_at\": \"2020-06-13T00:00:00+01:00\",         \"created_at\": \"2020-06-12T23:50:14+01:00\",         \"updated_at\": \"2020-06-12T23:53:07+01:00\",         \"relationships\": {           \"tasks\": {             \"object\": \"list\",             \"data\": [               {                 \"object\": \"schedule_task\",                 \"attributes\": {                   \"id\": 1,                   \"sequence_id\": 1,                   \"action\": \"command\",                   \"payload\": \"say Rebooting...\",                   \"time_offset\": 0,                   \"is_queued\": false,                   \"created_at\": \"2020-06-12T23:50:46+01:00\",                   \"updated_at\": \"2020-06-12T23:52:54+01:00\"                 }               },               {                 \"object\": \"schedule_task\",                 \"attributes\": {                   \"id\": 2,                   \"sequence_id\": 2,                   \"action\": \"power\",                   \"payload\": \"restart\",                   \"time_offset\": 5,                   \"is_queued\": false,                   \"created_at\": \"2020-06-12T23:53:07+01:00\",                   \"updated_at\": \"2020-06-12T23:53:07+01:00\"                 }               }             ]           }         }       }     }   ] } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import schedules_api
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
    api_instance = schedules_api.SchedulesApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 
    server_id = "server_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ / ] List schedules
        api_response = api_instance.client_serversserver_id_schedules_get(accept, content_type, server_id)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling SchedulesApi->client_serversserver_id_schedules_get: %s\n" % e)
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

# **client_serversserver_id_schedules_post**
> bool, date, datetime, dict, float, int, list, str, none_type client_serversserver_id_schedules_post(accept, server_id, client_servers_server_id_schedules_post_request)

[ / ] Create schedule

Creates a new schedule  ## Fields | Name         | Required? | Type    | Description                              | Rules | |--------------|-----------|---------|------------------------------------------|-------| | name         | required  | string  | Friendly name for the schedule           | min:1 | | is_active    | optional  | boolean | Specifies whether the schedule is active |       | | minute       | required  | string  | Cron minute syntax                       |       | | hour         | required  | string  | Cron hour syntax                         |       | | day\\_of\\_week  | required  | string  | Cron day-of-month syntax                 |       | | day\\_of\\_month | required  | string  | Cron day-of-month syntax                 |       |  <!-- RESPONSE 200 --> {   \"object\": \"server_schedule\",   \"attributes\": {     \"id\": 4,     \"name\": \"Minute Hello\",     \"cron\": {       \"day_of_week\": \"*\",       \"day_of_month\": \"*\",       \"hour\": \"*\",       \"minute\": \"*\"     },     \"is_active\": true,     \"is_processing\": false,     \"last_run_at\": null,     \"next_run_at\": \"2020-06-13T15:17:00+01:00\",     \"created_at\": \"2020-06-13T15:16:45+01:00\",     \"updated_at\": \"2020-06-13T15:16:45+01:00\",     \"relationships\": {       \"tasks\": {         \"object\": \"list\",         \"data\": []       }     }   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import schedules_api
from pterodactyl_client.model.client_servers_server_id_schedules_post_request import ClientServersServerIdSchedulesPostRequest
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
    api_instance = schedules_api.SchedulesApi(api_client)
    accept = "application/json" # str | 
    server_id = "server_id_example" # str | 
    client_servers_server_id_schedules_post_request = ClientServersServerIdSchedulesPostRequest(None) # ClientServersServerIdSchedulesPostRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ / ] Create schedule
        api_response = api_instance.client_serversserver_id_schedules_post(accept, server_id, client_servers_server_id_schedules_post_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling SchedulesApi->client_serversserver_id_schedules_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **server_id** | **str**|  |
 **client_servers_server_id_schedules_post_request** | [**ClientServersServerIdSchedulesPostRequest**](ClientServersServerIdSchedulesPostRequest.md)|  |

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

# **client_serversserver_id_schedulesschedule_id_delete**
> bool, date, datetime, dict, float, int, list, str, none_type client_serversserver_id_schedulesschedule_id_delete(accept, content_type, server_id, schedule_id)

[ /{schedule} ] Delete schedule

Deletes the specified schedule  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import schedules_api
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
    api_instance = schedules_api.SchedulesApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 
    server_id = "server_id_example" # str | 
    schedule_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{schedule} ] Delete schedule
        api_response = api_instance.client_serversserver_id_schedulesschedule_id_delete(accept, content_type, server_id, schedule_id)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling SchedulesApi->client_serversserver_id_schedulesschedule_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **content_type** | **str**|  |
 **server_id** | **str**|  |
 **schedule_id** | **int**|  |

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

# **client_serversserver_id_schedulesschedule_id_get**
> bool, date, datetime, dict, float, int, list, str, none_type client_serversserver_id_schedulesschedule_id_get(accept, content_type, server_id, schedule_id)

[ /{schedule} ] Schedule details

Retrieves specific schedule  <!-- RESPONSE 200 --> {   \"object\": \"server_schedule\",   \"attributes\": {     \"id\": 1,     \"name\": \"Daily Reboot\",     \"cron\": {       \"day_of_week\": \"*\",       \"day_of_month\": \"*\",       \"hour\": \"0\",       \"minute\": \"0\"     },     \"is_active\": true,     \"is_processing\": false,     \"last_run_at\": null,     \"next_run_at\": \"2020-06-13T00:00:00+01:00\",     \"created_at\": \"2020-06-12T23:50:14+01:00\",     \"updated_at\": \"2020-06-12T23:53:07+01:00\",     \"relationships\": {       \"tasks\": {         \"object\": \"list\",         \"data\": [           {             \"object\": \"schedule_task\",             \"attributes\": {               \"id\": 1,               \"sequence_id\": 1,               \"action\": \"command\",               \"payload\": \"say Rebooting...\",               \"time_offset\": 0,               \"is_queued\": false,               \"created_at\": \"2020-06-12T23:50:46+01:00\",               \"updated_at\": \"2020-06-12T23:52:54+01:00\"             }           },           {             \"object\": \"schedule_task\",             \"attributes\": {               \"id\": 2,               \"sequence_id\": 2,               \"action\": \"power\",               \"payload\": \"restart\",               \"time_offset\": 5,               \"is_queued\": false,               \"created_at\": \"2020-06-12T23:53:07+01:00\",               \"updated_at\": \"2020-06-12T23:53:07+01:00\"             }           }         ]       }     }   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import schedules_api
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
    api_instance = schedules_api.SchedulesApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 
    server_id = "server_id_example" # str | 
    schedule_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{schedule} ] Schedule details
        api_response = api_instance.client_serversserver_id_schedulesschedule_id_get(accept, content_type, server_id, schedule_id)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling SchedulesApi->client_serversserver_id_schedulesschedule_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **content_type** | **str**|  |
 **server_id** | **str**|  |
 **schedule_id** | **int**|  |

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

# **client_serversserver_id_schedulesschedule_id_post**
> bool, date, datetime, dict, float, int, list, str, none_type client_serversserver_id_schedulesschedule_id_post(accept, server_id, schedule_id, client_servers_server_id_schedules_schedule_id_post_request)

[ /{schedule} ] Update schedule

Updates the specified schedule  ## Fields | Name         | Required? | Type    | Description                              | Rules | |--------------|-----------|---------|------------------------------------------|-------| | name         | required  | string  | Friendly name for the schedule           | min:1 | | is_active    | optional  | boolean | Specifies whether the schedule is active |       | | minute       | required  | string  | Cron minute syntax                       |       | | hour         | required  | string  | Cron hour syntax                         |       | | day_of_week  | required  | string  | Cron day-of-month syntax                 |       | | day_of_month | required  | string  | Cron day-of-month syntax                 |       |  <!-- RESPONSE 200 --> {   \"object\": \"server_schedule\",   \"attributes\": {     \"id\": 2,     \"name\": \"Hourly Hello\",     \"cron\": {       \"day_of_week\": \"*\",       \"day_of_month\": \"*\",       \"hour\": \"*\",       \"minute\": \"0\"     },     \"is_active\": false,     \"is_processing\": false,     \"last_run_at\": null,     \"next_run_at\": \"2020-06-13T16:00:00+01:00\",     \"created_at\": \"2020-06-13T15:05:25+01:00\",     \"updated_at\": \"2020-06-13T15:14:07+01:00\",     \"relationships\": {       \"tasks\": {         \"object\": \"list\",         \"data\": []       }     }   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import schedules_api
from pterodactyl_client.model.client_servers_server_id_schedules_schedule_id_post_request import ClientServersServerIdSchedulesScheduleIdPostRequest
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
    api_instance = schedules_api.SchedulesApi(api_client)
    accept = "application/json" # str | 
    server_id = "server_id_example" # str | 
    schedule_id = 1 # int | 
    client_servers_server_id_schedules_schedule_id_post_request = ClientServersServerIdSchedulesScheduleIdPostRequest(None) # ClientServersServerIdSchedulesScheduleIdPostRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{schedule} ] Update schedule
        api_response = api_instance.client_serversserver_id_schedulesschedule_id_post(accept, server_id, schedule_id, client_servers_server_id_schedules_schedule_id_post_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling SchedulesApi->client_serversserver_id_schedulesschedule_id_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **server_id** | **str**|  |
 **schedule_id** | **int**|  |
 **client_servers_server_id_schedules_schedule_id_post_request** | [**ClientServersServerIdSchedulesScheduleIdPostRequest**](ClientServersServerIdSchedulesScheduleIdPostRequest.md)|  |

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

# **client_serversserver_id_schedulesschedule_id_tasks_post**
> bool, date, datetime, dict, float, int, list, str, none_type client_serversserver_id_schedulesschedule_id_tasks_post(accept, server_id, schedule_id, client_servers_server_id_schedules_schedule_id_tasks_post_request)

[ /{schedule}/tasks ] Create task

Creates a new task on the specified schedule  ## Fields | Name        | Required? | Type   | Description           | Rules | |-------------|-----------|--------|-----------------------|-------| | action      | required  | string | Type of action to use |       | | payload     | required  | string | Payload to send       |       | | time_offset | required  | string | Offset in seconds     |       |  # Actions | Action  | Description                                           | |---------|-------------------------------------------------------| | command | Sends power action                                    | | power   | Changes power signal - Check power route for payloads | | backup  | Creates a backup                                      |  <!-- RESPONSE 200 --> {   \"object\": \"schedule_task\",   \"attributes\": {     \"id\": 6,     \"sequence_id\": 1,     \"action\": \"command\",     \"payload\": \"say Hello World\",     \"time_offset\": 0,     \"is_queued\": false,     \"created_at\": \"2020-10-29T01:09:03+00:00\",     \"updated_at\": \"2020-10-29T01:09:03+00:00\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import schedules_api
from pterodactyl_client.model.client_servers_server_id_schedules_schedule_id_tasks_post_request import ClientServersServerIdSchedulesScheduleIdTasksPostRequest
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
    api_instance = schedules_api.SchedulesApi(api_client)
    accept = "application/json" # str | 
    server_id = "server_id_example" # str | 
    schedule_id = 1 # int | 
    client_servers_server_id_schedules_schedule_id_tasks_post_request = ClientServersServerIdSchedulesScheduleIdTasksPostRequest(None) # ClientServersServerIdSchedulesScheduleIdTasksPostRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{schedule}/tasks ] Create task
        api_response = api_instance.client_serversserver_id_schedulesschedule_id_tasks_post(accept, server_id, schedule_id, client_servers_server_id_schedules_schedule_id_tasks_post_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling SchedulesApi->client_serversserver_id_schedulesschedule_id_tasks_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **server_id** | **str**|  |
 **schedule_id** | **int**|  |
 **client_servers_server_id_schedules_schedule_id_tasks_post_request** | [**ClientServersServerIdSchedulesScheduleIdTasksPostRequest**](ClientServersServerIdSchedulesScheduleIdTasksPostRequest.md)|  |

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

# **client_serversserver_id_schedulesschedule_id_taskstask_id_delete**
> bool, date, datetime, dict, float, int, list, str, none_type client_serversserver_id_schedulesschedule_id_taskstask_id_delete(accept, content_type, server_id, schedule_id, task_id)

[ /{schedule}/tasks/{task} ] Delete  task

Deletes the specified task  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import schedules_api
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
    api_instance = schedules_api.SchedulesApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 
    server_id = "server_id_example" # str | 
    schedule_id = 1 # int | 
    task_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{schedule}/tasks/{task} ] Delete  task
        api_response = api_instance.client_serversserver_id_schedulesschedule_id_taskstask_id_delete(accept, content_type, server_id, schedule_id, task_id)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling SchedulesApi->client_serversserver_id_schedulesschedule_id_taskstask_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **content_type** | **str**|  |
 **server_id** | **str**|  |
 **schedule_id** | **int**|  |
 **task_id** | **int**|  |

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

# **client_serversserver_id_schedulesschedule_id_taskstask_id_post**
> bool, date, datetime, dict, float, int, list, str, none_type client_serversserver_id_schedulesschedule_id_taskstask_id_post(accept, server_id, schedule_id, task_id, client_servers_server_id_schedules_schedule_id_tasks_task_id_post_request)

[ /{schedule}/tasks/{task} ] Update task

Updates the specified task  ## Fields | Name        | Required? | Type   | Description           | Rules | |-------------|-----------|--------|-----------------------|-------| | action      | required  | string | Type of action to use |       | | payload     | required  | string | Payload to send       |       | | time_offset | required  | string | Offset in seconds     |       |  # Actions | Action  | Description                                           | |---------|-------------------------------------------------------| | command | Sends power action                                    | | power   | Changes power signal - Check power route for payloads | | backup  | Creates a backup                                      |  <!-- RESPONSE 200 --> {   \"object\": \"schedule_task\",   \"attributes\": {     \"id\": 6,     \"sequence_id\": 1,     \"action\": \"command\",     \"payload\": \"say Updated Statement!?\",     \"time_offset\": 0,     \"is_queued\": false,     \"created_at\": \"2020-10-29T01:09:03+00:00\",     \"updated_at\": \"2020-10-29T01:10:30+00:00\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import schedules_api
from pterodactyl_client.model.client_servers_server_id_schedules_schedule_id_tasks_task_id_post_request import ClientServersServerIdSchedulesScheduleIdTasksTaskIdPostRequest
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
    api_instance = schedules_api.SchedulesApi(api_client)
    accept = "application/json" # str | 
    server_id = "server_id_example" # str | 
    schedule_id = 1 # int | 
    task_id = 1 # int | 
    client_servers_server_id_schedules_schedule_id_tasks_task_id_post_request = ClientServersServerIdSchedulesScheduleIdTasksTaskIdPostRequest(None) # ClientServersServerIdSchedulesScheduleIdTasksTaskIdPostRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{schedule}/tasks/{task} ] Update task
        api_response = api_instance.client_serversserver_id_schedulesschedule_id_taskstask_id_post(accept, server_id, schedule_id, task_id, client_servers_server_id_schedules_schedule_id_tasks_task_id_post_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling SchedulesApi->client_serversserver_id_schedulesschedule_id_taskstask_id_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **server_id** | **str**|  |
 **schedule_id** | **int**|  |
 **task_id** | **int**|  |
 **client_servers_server_id_schedules_schedule_id_tasks_task_id_post_request** | [**ClientServersServerIdSchedulesScheduleIdTasksTaskIdPostRequest**](ClientServersServerIdSchedulesScheduleIdTasksTaskIdPostRequest.md)|  |

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

