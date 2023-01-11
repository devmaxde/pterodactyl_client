# pterodactyl_client.LocationsApi

All URIs are relative to *https://example.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**application_locations_get**](LocationsApi.md#application_locations_get) | **GET** /application/locations | [ / ] List locations
[**application_locations_post**](LocationsApi.md#application_locations_post) | **POST** /application/locations | [ / ] Create location
[**application_locationslocation_id_delete**](LocationsApi.md#application_locationslocation_id_delete) | **DELETE** /application/locations/{location_id} | [ /{location} ] Delete location
[**application_locationslocation_id_get**](LocationsApi.md#application_locationslocation_id_get) | **GET** /application/locations/{location_id} | [ /{location} ] Location details
[**application_locationslocation_id_patch**](LocationsApi.md#application_locationslocation_id_patch) | **PATCH** /application/locations/{location_id} | [ / ] Update location


# **application_locations_get**
> bool, date, datetime, dict, float, int, list, str, none_type application_locations_get(accept, content_type)

[ / ] List locations

Retrieves all locations  # Available include parameters | Parameter | Description                            | |-----------|----------------------------------------| | nodes     | List of nodes assigned to the location | | servers   | List of servers in the location        |  <!-- RESPONSE 200 --> {   \"object\": \"list\",   \"data\": [     {       \"object\": \"location\",       \"attributes\": {         \"id\": 1,         \"short\": \"GB\",         \"long\": \"London Datacenter\",         \"updated_at\": \"2020-06-13T21:16:58+00:00\",         \"created_at\": \"2019-12-22T04:44:18+00:00\"       }     }   ],   \"meta\": {     \"pagination\": {       \"total\": 1,       \"count\": 1,       \"per_page\": 50,       \"current_page\": 1,       \"total_pages\": 1,       \"links\": {}     }   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import locations_api
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
    api_instance = locations_api.LocationsApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ / ] List locations
        api_response = api_instance.application_locations_get(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling LocationsApi->application_locations_get: %s\n" % e)
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

# **application_locations_post**
> bool, date, datetime, dict, float, int, list, str, none_type application_locations_post(accept, application_locations_post_request)

[ / ] Create location

Creates a new location  ## Fields | Name  | Required? | Type   | Description          | Rules | |-------|-----------|--------|----------------------|-------| | short | required  | string | Location identifier  |       | | long  | optional  | string | Location description |       |  <!-- RESPONSE 200 --> {   \"object\": \"location\",   \"attributes\": {     \"id\": 3,     \"short\": \"G\",     \"long\": \"London Datacenter\",     \"updated_at\": \"2020-06-13T20:44:48+00:00\",     \"created_at\": \"2020-06-13T20:44:48+00:00\"   },   \"meta\": {     \"resource\": \"https://pterodactyl.file.properties/api/application/locations/3\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import locations_api
from pterodactyl_client.model.application_locations_post_request import ApplicationLocationsPostRequest
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
    api_instance = locations_api.LocationsApi(api_client)
    accept = "application/json" # str | 
    application_locations_post_request = ApplicationLocationsPostRequest(None) # ApplicationLocationsPostRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ / ] Create location
        api_response = api_instance.application_locations_post(accept, application_locations_post_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling LocationsApi->application_locations_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **application_locations_post_request** | [**ApplicationLocationsPostRequest**](ApplicationLocationsPostRequest.md)|  |

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

# **application_locationslocation_id_delete**
> bool, date, datetime, dict, float, int, list, str, none_type application_locationslocation_id_delete(accept, content_type, location_id)

[ /{location} ] Delete location

Deletes the specified location  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import locations_api
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
    api_instance = locations_api.LocationsApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 
    location_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{location} ] Delete location
        api_response = api_instance.application_locationslocation_id_delete(accept, content_type, location_id)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling LocationsApi->application_locationslocation_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **content_type** | **str**|  |
 **location_id** | **int**|  |

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

# **application_locationslocation_id_get**
> bool, date, datetime, dict, float, int, list, str, none_type application_locationslocation_id_get(accept, content_type, location_id)

[ /{location} ] Location details

Retrieves the specified location  # Available include parameters | Parameter | Description                            | |-----------|----------------------------------------| | nodes     | List of nodes assigned to the location | | servers   | List of servers in the location        |  <!-- RESPONSE 200 --> {   \"object\": \"location\",   \"attributes\": {     \"id\": 1,     \"short\": \"Test\",     \"long\": \"Test\",     \"updated_at\": \"2019-12-22T04:44:18+00:00\",     \"created_at\": \"2019-12-22T04:44:18+00:00\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import locations_api
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
    api_instance = locations_api.LocationsApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 
    location_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{location} ] Location details
        api_response = api_instance.application_locationslocation_id_get(accept, content_type, location_id)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling LocationsApi->application_locationslocation_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **content_type** | **str**|  |
 **location_id** | **int**|  |

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

# **application_locationslocation_id_patch**
> bool, date, datetime, dict, float, int, list, str, none_type application_locationslocation_id_patch(accept, location_id, application_locations_location_id_patch_request)

[ / ] Update location

Updates the specified location  <!-- RESPONSE 200 --> {   \"object\": \"location\",   \"attributes\": {     \"id\": 1,     \"short\": \"GB\",     \"long\": \"London Datacenter\",     \"updated_at\": \"2020-06-13T21:16:58+00:00\",     \"created_at\": \"2019-12-22T04:44:18+00:00\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import locations_api
from pterodactyl_client.model.application_locations_location_id_patch_request import ApplicationLocationsLocationIdPatchRequest
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
    api_instance = locations_api.LocationsApi(api_client)
    accept = "application/json" # str | 
    location_id = 1 # int | 
    application_locations_location_id_patch_request = ApplicationLocationsLocationIdPatchRequest(None) # ApplicationLocationsLocationIdPatchRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ / ] Update location
        api_response = api_instance.application_locationslocation_id_patch(accept, location_id, application_locations_location_id_patch_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling LocationsApi->application_locationslocation_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **location_id** | **int**|  |
 **application_locations_location_id_patch_request** | [**ApplicationLocationsLocationIdPatchRequest**](ApplicationLocationsLocationIdPatchRequest.md)|  |

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

