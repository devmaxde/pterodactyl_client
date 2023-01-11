# pterodactyl_client.AccountApi

All URIs are relative to *https://example.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_api_keysapi_key_id_delete**](AccountApi.md#account_api_keysapi_key_id_delete) | **DELETE** /account/api-keys/{api_key_id} | [ /api-keys/{identifier} ] Delete API key


# **account_api_keysapi_key_id_delete**
> bool, date, datetime, dict, float, int, list, str, none_type account_api_keysapi_key_id_delete(accept, content_type, api_key_id)

[ /api-keys/{identifier} ] Delete API key

Deletes the specified API key  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->  <!-- RESPONSE 404 --> // Non existing API key {   \"errors\": [     {       \"code\": \"NotFoundHttpException\",       \"status\": \"404\",       \"detail\": \"An error was encountered while processing this request.\"     }   ] } <!-- ENDRESPONSE --> 

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import account_api
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
    api_instance = account_api.AccountApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 
    api_key_id = "api_key_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /api-keys/{identifier} ] Delete API key
        api_response = api_instance.account_api_keysapi_key_id_delete(accept, content_type, api_key_id)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling AccountApi->account_api_keysapi_key_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **content_type** | **str**|  |
 **api_key_id** | **str**|  |

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

