# pterodactyl_client.SchedulesSchedulesApi

All URIs are relative to *https://example.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**__createschedule**](SchedulesSchedulesApi.md#__createschedule) | **POST** /client/servers/1a7ce997/schedules | [ / ] Create schedule
[**__listschedules**](SchedulesSchedulesApi.md#__listschedules) | **GET** /client/servers/1a7ce997/schedules | [ / ] List schedules
[**__schedule_deleteschedule**](SchedulesSchedulesApi.md#__schedule_deleteschedule) | **DELETE** /client/servers/1a7ce997/schedules/2 | [ /{schedule} ] Delete schedule
[**__schedule_scheduledetails**](SchedulesSchedulesApi.md#__schedule_scheduledetails) | **GET** /client/servers/1a7ce997/schedules/1 | [ /{schedule} ] Schedule details
[**__schedule_tasks_createtask**](SchedulesSchedulesApi.md#__schedule_tasks_createtask) | **POST** /client/servers/1a7ce997/schedules/7/tasks | [ /{schedule}/tasks ] Create task
[**__schedule_tasks_task_deletetask**](SchedulesSchedulesApi.md#__schedule_tasks_task_deletetask) | **DELETE** /client/servers/1a7ce997/schedules/2/tasks/3 | [ /{schedule}/tasks/{task} ] Delete  task
[**__schedule_tasks_task_updatetask**](SchedulesSchedulesApi.md#__schedule_tasks_task_updatetask) | **POST** /client/servers/1a7ce997/schedules/7/tasks/6 | [ /{schedule}/tasks/{task} ] Update task
[**__schedule_updateschedule**](SchedulesSchedulesApi.md#__schedule_updateschedule) | **POST** /client/servers/1a7ce997/schedules/2 | [ /{schedule} ] Update schedule


# **__createschedule**
> bool, date, datetime, dict, float, int, list, str, none_type __createschedule(accept, createschedule_request)

[ / ] Create schedule

Creates a new schedule  ## Fields | Name         | Required? | Type    | Description                              | Rules | |--------------|-----------|---------|------------------------------------------|-------| | name         | required  | string  | Friendly name for the schedule           | min:1 | | is_active    | optional  | boolean | Specifies whether the schedule is active |       | | minute       | required  | string  | Cron minute syntax                       |       | | hour         | required  | string  | Cron hour syntax                         |       | | day\\_of\\_week  | required  | string  | Cron day-of-month syntax                 |       | | day\\_of\\_month | required  | string  | Cron day-of-month syntax                 |       |  <!-- RESPONSE 200 --> {   \"object\": \"server_schedule\",   \"attributes\": {     \"id\": 4,     \"name\": \"Minute Hello\",     \"cron\": {       \"day_of_week\": \"*\",       \"day_of_month\": \"*\",       \"hour\": \"*\",       \"minute\": \"*\"     },     \"is_active\": true,     \"is_processing\": false,     \"last_run_at\": null,     \"next_run_at\": \"2020-06-13T15:17:00+01:00\",     \"created_at\": \"2020-06-13T15:16:45+01:00\",     \"updated_at\": \"2020-06-13T15:16:45+01:00\",     \"relationships\": {       \"tasks\": {         \"object\": \"list\",         \"data\": []       }     }   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import schedules_schedules_api
from pterodactyl_client.model.createschedule_request import CreatescheduleRequest
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
    api_instance = schedules_schedules_api.SchedulesSchedulesApi(api_client)
    accept = "application/json" # str | 
    createschedule_request = CreatescheduleRequest(None) # CreatescheduleRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ / ] Create schedule
        api_response = api_instance.__createschedule(accept, createschedule_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling SchedulesSchedulesApi->__createschedule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **createschedule_request** | [**CreatescheduleRequest**](CreatescheduleRequest.md)|  |

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

# **__listschedules**
> bool, date, datetime, dict, float, int, list, str, none_type __listschedules(accept, content_type)

[ / ] List schedules

Lists all schedules added to the server  <!-- RESPONSE 200 --> {   \"object\": \"list\",   \"data\": [     {       \"object\": \"server_schedule\",       \"attributes\": {         \"id\": 1,         \"name\": \"Daily Reboot\",         \"cron\": {           \"day_of_week\": \"*\",           \"day_of_month\": \"*\",           \"hour\": \"0\",           \"minute\": \"0\"         },         \"is_active\": true,         \"is_processing\": false,         \"last_run_at\": null,         \"next_run_at\": \"2020-06-13T00:00:00+01:00\",         \"created_at\": \"2020-06-12T23:50:14+01:00\",         \"updated_at\": \"2020-06-12T23:53:07+01:00\",         \"relationships\": {           \"tasks\": {             \"object\": \"list\",             \"data\": [               {                 \"object\": \"schedule_task\",                 \"attributes\": {                   \"id\": 1,                   \"sequence_id\": 1,                   \"action\": \"command\",                   \"payload\": \"say Rebooting...\",                   \"time_offset\": 0,                   \"is_queued\": false,                   \"created_at\": \"2020-06-12T23:50:46+01:00\",                   \"updated_at\": \"2020-06-12T23:52:54+01:00\"                 }               },               {                 \"object\": \"schedule_task\",                 \"attributes\": {                   \"id\": 2,                   \"sequence_id\": 2,                   \"action\": \"power\",                   \"payload\": \"restart\",                   \"time_offset\": 5,                   \"is_queued\": false,                   \"created_at\": \"2020-06-12T23:53:07+01:00\",                   \"updated_at\": \"2020-06-12T23:53:07+01:00\"                 }               }             ]           }         }       }     }   ] } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import schedules_schedules_api
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
    api_instance = schedules_schedules_api.SchedulesSchedulesApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ / ] List schedules
        api_response = api_instance.__listschedules(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling SchedulesSchedulesApi->__listschedules: %s\n" % e)
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

# **__schedule_deleteschedule**
> bool, date, datetime, dict, float, int, list, str, none_type __schedule_deleteschedule(accept, content_type)

[ /{schedule} ] Delete schedule

Deletes the specified schedule  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import schedules_schedules_api
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
    api_instance = schedules_schedules_api.SchedulesSchedulesApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{schedule} ] Delete schedule
        api_response = api_instance.__schedule_deleteschedule(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling SchedulesSchedulesApi->__schedule_deleteschedule: %s\n" % e)
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

# **__schedule_scheduledetails**
> bool, date, datetime, dict, float, int, list, str, none_type __schedule_scheduledetails(accept, content_type)

[ /{schedule} ] Schedule details

Retrieves specific schedule  <!-- RESPONSE 200 --> {   \"object\": \"server_schedule\",   \"attributes\": {     \"id\": 1,     \"name\": \"Daily Reboot\",     \"cron\": {       \"day_of_week\": \"*\",       \"day_of_month\": \"*\",       \"hour\": \"0\",       \"minute\": \"0\"     },     \"is_active\": true,     \"is_processing\": false,     \"last_run_at\": null,     \"next_run_at\": \"2020-06-13T00:00:00+01:00\",     \"created_at\": \"2020-06-12T23:50:14+01:00\",     \"updated_at\": \"2020-06-12T23:53:07+01:00\",     \"relationships\": {       \"tasks\": {         \"object\": \"list\",         \"data\": [           {             \"object\": \"schedule_task\",             \"attributes\": {               \"id\": 1,               \"sequence_id\": 1,               \"action\": \"command\",               \"payload\": \"say Rebooting...\",               \"time_offset\": 0,               \"is_queued\": false,               \"created_at\": \"2020-06-12T23:50:46+01:00\",               \"updated_at\": \"2020-06-12T23:52:54+01:00\"             }           },           {             \"object\": \"schedule_task\",             \"attributes\": {               \"id\": 2,               \"sequence_id\": 2,               \"action\": \"power\",               \"payload\": \"restart\",               \"time_offset\": 5,               \"is_queued\": false,               \"created_at\": \"2020-06-12T23:53:07+01:00\",               \"updated_at\": \"2020-06-12T23:53:07+01:00\"             }           }         ]       }     }   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import schedules_schedules_api
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
    api_instance = schedules_schedules_api.SchedulesSchedulesApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{schedule} ] Schedule details
        api_response = api_instance.__schedule_scheduledetails(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling SchedulesSchedulesApi->__schedule_scheduledetails: %s\n" % e)
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

# **__schedule_tasks_createtask**
> bool, date, datetime, dict, float, int, list, str, none_type __schedule_tasks_createtask(accept, schedule_tasks_createtask_request)

[ /{schedule}/tasks ] Create task

Creates a new task on the specified schedule  ## Fields | Name        | Required? | Type   | Description           | Rules | |-------------|-----------|--------|-----------------------|-------| | action      | required  | string | Type of action to use |       | | payload     | required  | string | Payload to send       |       | | time_offset | required  | string | Offset in seconds     |       |  # Actions | Action  | Description                                           | |---------|-------------------------------------------------------| | command | Sends power action                                    | | power   | Changes power signal - Check power route for payloads | | backup  | Creates a backup                                      |  <!-- RESPONSE 200 --> {   \"object\": \"schedule_task\",   \"attributes\": {     \"id\": 6,     \"sequence_id\": 1,     \"action\": \"command\",     \"payload\": \"say Hello World\",     \"time_offset\": 0,     \"is_queued\": false,     \"created_at\": \"2020-10-29T01:09:03+00:00\",     \"updated_at\": \"2020-10-29T01:09:03+00:00\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import schedules_schedules_api
from pterodactyl_client.model.schedule_tasks_createtask_request import ScheduleTasksCreatetaskRequest
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
    api_instance = schedules_schedules_api.SchedulesSchedulesApi(api_client)
    accept = "application/json" # str | 
    schedule_tasks_createtask_request = ScheduleTasksCreatetaskRequest(None) # ScheduleTasksCreatetaskRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{schedule}/tasks ] Create task
        api_response = api_instance.__schedule_tasks_createtask(accept, schedule_tasks_createtask_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling SchedulesSchedulesApi->__schedule_tasks_createtask: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **schedule_tasks_createtask_request** | [**ScheduleTasksCreatetaskRequest**](ScheduleTasksCreatetaskRequest.md)|  |

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

# **__schedule_tasks_task_deletetask**
> bool, date, datetime, dict, float, int, list, str, none_type __schedule_tasks_task_deletetask(accept, content_type)

[ /{schedule}/tasks/{task} ] Delete  task

Deletes the specified task  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import schedules_schedules_api
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
    api_instance = schedules_schedules_api.SchedulesSchedulesApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{schedule}/tasks/{task} ] Delete  task
        api_response = api_instance.__schedule_tasks_task_deletetask(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling SchedulesSchedulesApi->__schedule_tasks_task_deletetask: %s\n" % e)
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

# **__schedule_tasks_task_updatetask**
> bool, date, datetime, dict, float, int, list, str, none_type __schedule_tasks_task_updatetask(accept, schedule_tasks_task_updatetask_request)

[ /{schedule}/tasks/{task} ] Update task

Updates the specified task  ## Fields | Name        | Required? | Type   | Description           | Rules | |-------------|-----------|--------|-----------------------|-------| | action      | required  | string | Type of action to use |       | | payload     | required  | string | Payload to send       |       | | time_offset | required  | string | Offset in seconds     |       |  # Actions | Action  | Description                                           | |---------|-------------------------------------------------------| | command | Sends power action                                    | | power   | Changes power signal - Check power route for payloads | | backup  | Creates a backup                                      |  <!-- RESPONSE 200 --> {   \"object\": \"schedule_task\",   \"attributes\": {     \"id\": 6,     \"sequence_id\": 1,     \"action\": \"command\",     \"payload\": \"say Updated Statement!?\",     \"time_offset\": 0,     \"is_queued\": false,     \"created_at\": \"2020-10-29T01:09:03+00:00\",     \"updated_at\": \"2020-10-29T01:10:30+00:00\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import schedules_schedules_api
from pterodactyl_client.model.schedule_tasks_task_updatetask_request import ScheduleTasksTaskUpdatetaskRequest
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
    api_instance = schedules_schedules_api.SchedulesSchedulesApi(api_client)
    accept = "application/json" # str | 
    schedule_tasks_task_updatetask_request = ScheduleTasksTaskUpdatetaskRequest(None) # ScheduleTasksTaskUpdatetaskRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{schedule}/tasks/{task} ] Update task
        api_response = api_instance.__schedule_tasks_task_updatetask(accept, schedule_tasks_task_updatetask_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling SchedulesSchedulesApi->__schedule_tasks_task_updatetask: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **schedule_tasks_task_updatetask_request** | [**ScheduleTasksTaskUpdatetaskRequest**](ScheduleTasksTaskUpdatetaskRequest.md)|  |

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

# **__schedule_updateschedule**
> bool, date, datetime, dict, float, int, list, str, none_type __schedule_updateschedule(accept, schedule_updateschedule_request)

[ /{schedule} ] Update schedule

Updates the specified schedule  ## Fields | Name         | Required? | Type    | Description                              | Rules | |--------------|-----------|---------|------------------------------------------|-------| | name         | required  | string  | Friendly name for the schedule           | min:1 | | is_active    | optional  | boolean | Specifies whether the schedule is active |       | | minute       | required  | string  | Cron minute syntax                       |       | | hour         | required  | string  | Cron hour syntax                         |       | | day_of_week  | required  | string  | Cron day-of-month syntax                 |       | | day_of_month | required  | string  | Cron day-of-month syntax                 |       |  <!-- RESPONSE 200 --> {   \"object\": \"server_schedule\",   \"attributes\": {     \"id\": 2,     \"name\": \"Hourly Hello\",     \"cron\": {       \"day_of_week\": \"*\",       \"day_of_month\": \"*\",       \"hour\": \"*\",       \"minute\": \"0\"     },     \"is_active\": false,     \"is_processing\": false,     \"last_run_at\": null,     \"next_run_at\": \"2020-06-13T16:00:00+01:00\",     \"created_at\": \"2020-06-13T15:05:25+01:00\",     \"updated_at\": \"2020-06-13T15:14:07+01:00\",     \"relationships\": {       \"tasks\": {         \"object\": \"list\",         \"data\": []       }     }   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import schedules_schedules_api
from pterodactyl_client.model.schedule_updateschedule_request import ScheduleUpdatescheduleRequest
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
    api_instance = schedules_schedules_api.SchedulesSchedulesApi(api_client)
    accept = "application/json" # str | 
    schedule_updateschedule_request = ScheduleUpdatescheduleRequest(None) # ScheduleUpdatescheduleRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{schedule} ] Update schedule
        api_response = api_instance.__schedule_updateschedule(accept, schedule_updateschedule_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling SchedulesSchedulesApi->__schedule_updateschedule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **schedule_updateschedule_request** | [**ScheduleUpdatescheduleRequest**](ScheduleUpdatescheduleRequest.md)|  |

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

