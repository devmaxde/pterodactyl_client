# pterodactyl_client.NestsNestsApi

All URIs are relative to *https://example.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**__listnests**](NestsNestsApi.md#__listnests) | **GET** /application/nests | [ / ] List nests
[**__nest_nestdetails**](NestsNestsApi.md#__nest_nestdetails) | **GET** /application/nests/1 | [ /{nest} ] Nest details


# **__listnests**
> bool, date, datetime, dict, float, int, list, str, none_type __listnests(accept, content_type)

[ / ] List nests

Retrieves all nests  # Available include parameters | Parameter | Description                     | |-----------|---------------------------------| | eggs      | List of eggs in the location    | | servers   | List of servers in the location |  <!-- RESPONSE 200 --> {   \"object\": \"list\",   \"data\": [     {       \"object\": \"nest\",       \"attributes\": {         \"id\": 1,         \"uuid\": \"58bde975-ec57-4af2-b241-1426ac6d6d59\",         \"author\": \"support@pterodactyl.io\",         \"name\": \"Minecraft\",         \"description\": \"Minecraft - the classic game from Mojang. With support for Vanilla MC, Spigot, and many others!\",         \"created_at\": \"2019-12-22T04:42:51+00:00\",         \"updated_at\": \"2019-12-22T04:42:51+00:00\"       }     },     {       \"object\": \"nest\",       \"attributes\": {         \"id\": 2,         \"uuid\": \"5246d226-e8e8-46f5-b624-e99cf1a68c9a\",         \"author\": \"support@pterodactyl.io\",         \"name\": \"Source Engine\",         \"description\": \"Includes support for most Source Dedicated Server games.\",         \"created_at\": \"2019-12-22T04:42:51+00:00\",         \"updated_at\": \"2019-12-22T04:42:51+00:00\"       }     },     {       \"object\": \"nest\",       \"attributes\": {         \"id\": 3,         \"uuid\": \"0eb05bf7-3a00-4b1d-bef5-a6d8d7375e44\",         \"author\": \"support@pterodactyl.io\",         \"name\": \"Voice Servers\",         \"description\": \"Voice servers such as Mumble and Teamspeak 3.\",         \"created_at\": \"2019-12-22T04:42:51+00:00\",         \"updated_at\": \"2019-12-22T04:42:51+00:00\"       }     },     {       \"object\": \"nest\",       \"attributes\": {         \"id\": 4,         \"uuid\": \"e2a21c82-7175-4db0-9510-8d1ed525b2bf\",         \"author\": \"support@pterodactyl.io\",         \"name\": \"Rust\",         \"description\": \"Rust - A game where you must fight to survive.\",         \"created_at\": \"2019-12-22T04:42:51+00:00\",         \"updated_at\": \"2019-12-22T04:42:51+00:00\"       }     }   ],   \"meta\": {     \"pagination\": {       \"total\": 4,       \"count\": 4,       \"per_page\": 50,       \"current_page\": 1,       \"total_pages\": 1,       \"links\": {}     }   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import nests_nests_api
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
    api_instance = nests_nests_api.NestsNestsApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ / ] List nests
        api_response = api_instance.__listnests(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling NestsNestsApi->__listnests: %s\n" % e)
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

# **__nest_nestdetails**
> bool, date, datetime, dict, float, int, list, str, none_type __nest_nestdetails(accept, content_type)

[ /{nest} ] Nest details

Retrieves the specified nests  # Available include parameters | Parameter | Description                     | |-----------|---------------------------------| | eggs      | List of eggs in the location    | | servers   | List of servers in the location |  <!-- RESPONSE 200 --> {   \"object\": \"nest\",   \"attributes\": {     \"id\": 1,     \"uuid\": \"58bde975-ec57-4af2-b241-1426ac6d6d59\",     \"author\": \"support@pterodactyl.io\",     \"name\": \"Minecraft\",     \"description\": \"Minecraft - the classic game from Mojang. With support for Vanilla MC, Spigot, and many others!\",     \"created_at\": \"2019-12-22T04:42:51+00:00\",     \"updated_at\": \"2019-12-22T04:42:51+00:00\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import nests_nests_api
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
    api_instance = nests_nests_api.NestsNestsApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /{nest} ] Nest details
        api_response = api_instance.__nest_nestdetails(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling NestsNestsApi->__nest_nestdetails: %s\n" % e)
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

