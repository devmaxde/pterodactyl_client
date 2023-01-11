# pterodactyl_client.LocationsLocationsApi

All URIs are relative to *https://example.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**__createlocation**](LocationsLocationsApi.md#__createlocation) | **POST** /application/locations | [ / ] Create location
[**__listlocations**](LocationsLocationsApi.md#__listlocations) | **GET** /application/locations | [ / ] List locations


# **__createlocation**
> bool, date, datetime, dict, float, int, list, str, none_type __createlocation(accept, createlocation_request)

[ / ] Create location

Creates a new location  ## Fields | Name  | Required? | Type   | Description          | Rules | |-------|-----------|--------|----------------------|-------| | short | required  | string | Location identifier  |       | | long  | optional  | string | Location description |       |  <!-- RESPONSE 200 --> {   \"object\": \"location\",   \"attributes\": {     \"id\": 3,     \"short\": \"G\",     \"long\": \"London Datacenter\",     \"updated_at\": \"2020-06-13T20:44:48+00:00\",     \"created_at\": \"2020-06-13T20:44:48+00:00\"   },   \"meta\": {     \"resource\": \"https://pterodactyl.file.properties/api/application/locations/3\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import locations_locations_api
from pterodactyl_client.model.createlocation_request import CreatelocationRequest
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
    api_instance = locations_locations_api.LocationsLocationsApi(api_client)
    accept = "application/json" # str | 
    createlocation_request = CreatelocationRequest(None) # CreatelocationRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ / ] Create location
        api_response = api_instance.__createlocation(accept, createlocation_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling LocationsLocationsApi->__createlocation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **createlocation_request** | [**CreatelocationRequest**](CreatelocationRequest.md)|  |

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

# **__listlocations**
> bool, date, datetime, dict, float, int, list, str, none_type __listlocations(accept, content_type)

[ / ] List locations

Retrieves all locations  # Available include parameters | Parameter | Description                            | |-----------|----------------------------------------| | nodes     | List of nodes assigned to the location | | servers   | List of servers in the location        |  <!-- RESPONSE 200 --> {   \"object\": \"list\",   \"data\": [     {       \"object\": \"location\",       \"attributes\": {         \"id\": 1,         \"short\": \"GB\",         \"long\": \"London Datacenter\",         \"updated_at\": \"2020-06-13T21:16:58+00:00\",         \"created_at\": \"2019-12-22T04:44:18+00:00\"       }     }   ],   \"meta\": {     \"pagination\": {       \"total\": 1,       \"count\": 1,       \"per_page\": 50,       \"current_page\": 1,       \"total_pages\": 1,       \"links\": {}     }   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import locations_locations_api
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
    api_instance = locations_locations_api.LocationsLocationsApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ / ] List locations
        api_response = api_instance.__listlocations(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling LocationsLocationsApi->__listlocations: %s\n" % e)
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

