# pterodactyl_client.AccountApi

All URIs are relative to *http://example.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_client_account_api_keys_get**](AccountApi.md#api_client_account_api_keys_get) | **GET** /api/client/account/api-keys | 
[**api_client_account_api_keys_key_id_delete**](AccountApi.md#api_client_account_api_keys_key_id_delete) | **DELETE** /api/client/account/api-keys/{key_id} | 
[**api_client_account_api_keys_post**](AccountApi.md#api_client_account_api_keys_post) | **POST** /api/client/account/api-keys | 
[**api_client_account_email_put**](AccountApi.md#api_client_account_email_put) | **PUT** /api/client/account/email | 
[**api_client_account_get**](AccountApi.md#api_client_account_get) | **GET** /api/client/account | 
[**api_client_account_password_put**](AccountApi.md#api_client_account_password_put) | **PUT** /api/client/account/password | 
[**api_client_account_two_factor_delete**](AccountApi.md#api_client_account_two_factor_delete) | **DELETE** /api/client/account/two-factor | 
[**api_client_account_two_factor_get**](AccountApi.md#api_client_account_two_factor_get) | **GET** /api/client/account/two-factor | 
[**api_client_account_two_factor_post**](AccountApi.md#api_client_account_two_factor_post) | **POST** /api/client/account/two-factor | 


# **api_client_account_api_keys_get**
> api_client_account_api_keys_get()



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import account_api
from pprint import pprint
# Defining the host is optional and defaults to http://example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pterodactyl_client.Configuration(
    host = "http://example.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with pterodactyl_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = account_api.AccountApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.api_client_account_api_keys_get()
    except pterodactyl_client.ApiException as e:
        print("Exception when calling AccountApi->api_client_account_api_keys_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_client_account_api_keys_key_id_delete**
> api_client_account_api_keys_key_id_delete(key_id)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import account_api
from pprint import pprint
# Defining the host is optional and defaults to http://example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pterodactyl_client.Configuration(
    host = "http://example.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with pterodactyl_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = account_api.AccountApi(api_client)
    key_id = "key_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_account_api_keys_key_id_delete(key_id)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling AccountApi->api_client_account_api_keys_key_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_client_account_api_keys_post**
> api_client_account_api_keys_post(api_client_account_api_keys_get_request)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import account_api
from pterodactyl_client.model.api_client_account_api_keys_get_request import ApiClientAccountApiKeysGetRequest
from pprint import pprint
# Defining the host is optional and defaults to http://example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pterodactyl_client.Configuration(
    host = "http://example.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with pterodactyl_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = account_api.AccountApi(api_client)
    api_client_account_api_keys_get_request = ApiClientAccountApiKeysGetRequest(
        description="description_example",
        allowed_ips=[
            "allowed_ips_example",
        ],
    ) # ApiClientAccountApiKeysGetRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_account_api_keys_post(api_client_account_api_keys_get_request)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling AccountApi->api_client_account_api_keys_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_client_account_api_keys_get_request** | [**ApiClientAccountApiKeysGetRequest**](ApiClientAccountApiKeysGetRequest.md)|  |

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_client_account_email_put**
> api_client_account_email_put(api_client_account_email_put_request)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import account_api
from pterodactyl_client.model.api_client_account_email_put_request import ApiClientAccountEmailPutRequest
from pprint import pprint
# Defining the host is optional and defaults to http://example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pterodactyl_client.Configuration(
    host = "http://example.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with pterodactyl_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = account_api.AccountApi(api_client)
    api_client_account_email_put_request = ApiClientAccountEmailPutRequest(
        email="email_example",
        password="password_example",
    ) # ApiClientAccountEmailPutRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_account_email_put(api_client_account_email_put_request)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling AccountApi->api_client_account_email_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_client_account_email_put_request** | [**ApiClientAccountEmailPutRequest**](ApiClientAccountEmailPutRequest.md)|  |

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_client_account_get**
> api_client_account_get()



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import account_api
from pprint import pprint
# Defining the host is optional and defaults to http://example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pterodactyl_client.Configuration(
    host = "http://example.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with pterodactyl_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = account_api.AccountApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.api_client_account_get()
    except pterodactyl_client.ApiException as e:
        print("Exception when calling AccountApi->api_client_account_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_client_account_password_put**
> api_client_account_password_put(api_client_account_password_put_request)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import account_api
from pterodactyl_client.model.api_client_account_password_put_request import ApiClientAccountPasswordPutRequest
from pprint import pprint
# Defining the host is optional and defaults to http://example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pterodactyl_client.Configuration(
    host = "http://example.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with pterodactyl_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = account_api.AccountApi(api_client)
    api_client_account_password_put_request = ApiClientAccountPasswordPutRequest(
        current_password="current_password_example",
        password="password_example",
        password_confirmation="password_confirmation_example",
    ) # ApiClientAccountPasswordPutRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_account_password_put(api_client_account_password_put_request)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling AccountApi->api_client_account_password_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_client_account_password_put_request** | [**ApiClientAccountPasswordPutRequest**](ApiClientAccountPasswordPutRequest.md)|  |

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_client_account_two_factor_delete**
> api_client_account_two_factor_delete(api_client_account_two_factor_delete_request1)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import account_api
from pterodactyl_client.model.api_client_account_two_factor_delete_request1 import ApiClientAccountTwoFactorDeleteRequest1
from pprint import pprint
# Defining the host is optional and defaults to http://example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pterodactyl_client.Configuration(
    host = "http://example.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with pterodactyl_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = account_api.AccountApi(api_client)
    api_client_account_two_factor_delete_request1 = ApiClientAccountTwoFactorDeleteRequest1(
        password="password_example",
    ) # ApiClientAccountTwoFactorDeleteRequest1 | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_account_two_factor_delete(api_client_account_two_factor_delete_request1)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling AccountApi->api_client_account_two_factor_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_client_account_two_factor_delete_request1** | [**ApiClientAccountTwoFactorDeleteRequest1**](ApiClientAccountTwoFactorDeleteRequest1.md)|  |

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_client_account_two_factor_get**
> api_client_account_two_factor_get()



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import account_api
from pprint import pprint
# Defining the host is optional and defaults to http://example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pterodactyl_client.Configuration(
    host = "http://example.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with pterodactyl_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = account_api.AccountApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.api_client_account_two_factor_get()
    except pterodactyl_client.ApiException as e:
        print("Exception when calling AccountApi->api_client_account_two_factor_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_client_account_two_factor_post**
> api_client_account_two_factor_post(api_client_account_two_factor_delete_request)



### Example

* Api Key Authentication (JWT):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import account_api
from pterodactyl_client.model.api_client_account_two_factor_delete_request import ApiClientAccountTwoFactorDeleteRequest
from pprint import pprint
# Defining the host is optional and defaults to http://example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pterodactyl_client.Configuration(
    host = "http://example.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: JWT
configuration.api_key['JWT'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['JWT'] = 'Bearer'

# Enter a context with an instance of the API client
with pterodactyl_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = account_api.AccountApi(api_client)
    api_client_account_two_factor_delete_request = ApiClientAccountTwoFactorDeleteRequest(
        code="code_example",
    ) # ApiClientAccountTwoFactorDeleteRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_client_account_two_factor_post(api_client_account_two_factor_delete_request)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling AccountApi->api_client_account_two_factor_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_client_account_two_factor_delete_request** | [**ApiClientAccountTwoFactorDeleteRequest**](ApiClientAccountTwoFactorDeleteRequest.md)|  |

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

