# pterodactyl_client.StartupStartupApi

All URIs are relative to *https://example.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**__list_variables**](StartupStartupApi.md#__list_variables) | **GET** /client/servers/1a7ce997/startup | [ / ] List Variables
[**__variable_update_variable**](StartupStartupApi.md#__variable_update_variable) | **PUT** /client/servers/1a7ce997/startup/variable | [ /variable ] Update Variable


# **__list_variables**
> bool, date, datetime, dict, float, int, list, str, none_type __list_variables(accept)

[ / ] List Variables

Lists all variables on the server  <!-- RESPONSE 200 --> {   \"object\": \"list\",   \"data\": [     {       \"object\": \"egg_variable\",       \"attributes\": {         \"name\": \"Server Jar File\",         \"description\": \"The name of the server jarfile to run the server with.\",         \"env_variable\": \"SERVER_JARFILE\",         \"default_value\": \"server.jar\",         \"server_value\": \"server.jar\",         \"is_editable\": true,         \"rules\": \"required|regex:/^([\\\\w\\\\d._-]+)(\\\\.jar)$/\"       }     },     {       \"object\": \"egg_variable\",       \"attributes\": {         \"name\": \"Server Version\",         \"description\": \"The version of Minecraft Vanilla to install. Use \\\"latest\\\" to install the latest version.\",         \"env_variable\": \"VANILLA_VERSION\",         \"default_value\": \"latest\",         \"server_value\": \"latest\",         \"is_editable\": true,         \"rules\": \"required|string|between:3,15\"       }     }   ],   \"meta\": {     \"startup_command\": \"java -Xms128M -Xmx512M -jar server.jar\",     \"raw_startup_command\": \"java -Xms128M -Xmx\\{\\{ SERVER_MEMORY }}M -jar {\\{ SERVER_JARFILE }}\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import startup_startup_api
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
    api_instance = startup_startup_api.StartupStartupApi(api_client)
    accept = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ / ] List Variables
        api_response = api_instance.__list_variables(accept)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling StartupStartupApi->__list_variables: %s\n" % e)
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

# **__variable_update_variable**
> bool, date, datetime, dict, float, int, list, str, none_type __variable_update_variable(accept, variable_update_variable_request)

[ /variable ] Update Variable

Updates the specified variable  <!-- RESPONSE 200 --> {   \"object\": \"egg_variable\",   \"attributes\": {     \"name\": \"Server Jar File\",     \"description\": \"The name of the server jarfile to run the server with.\",     \"env_variable\": \"SERVER_JARFILE\",     \"default_value\": \"server.jar\",     \"server_value\": \"server.jar\",     \"is_editable\": true,     \"rules\": \"required|regex:/^([\\\\w\\\\d._-]+)(\\\\.jar)$/\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import startup_startup_api
from pterodactyl_client.model.variable_update_variable_request import VariableUpdateVariableRequest
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
    api_instance = startup_startup_api.StartupStartupApi(api_client)
    accept = "application/json" # str | 
    variable_update_variable_request = VariableUpdateVariableRequest(None) # VariableUpdateVariableRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ /variable ] Update Variable
        api_response = api_instance.__variable_update_variable(accept, variable_update_variable_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling StartupStartupApi->__variable_update_variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **variable_update_variable_request** | [**VariableUpdateVariableRequest**](VariableUpdateVariableRequest.md)|  |

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

