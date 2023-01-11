# pterodactyl_client.AccountApi

All URIs are relative to *https://example.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_api_keys_get**](AccountApi.md#account_api_keys_get) | **GET** /account/api-keys | [ /api-keys ] List API keys
[**account_api_keys_post**](AccountApi.md#account_api_keys_post) | **POST** /account/api-keys | [ /api-keys ] Create API key
[**account_api_keysapi_key_id_delete**](AccountApi.md#account_api_keysapi_key_id_delete) | **DELETE** /account/api-keys/{api_key_id} | [ /api-keys/{identifier} ] Delete API key
[**account_email_put**](AccountApi.md#account_email_put) | **PUT** /account/email | [ /email ] Update email
[**account_get**](AccountApi.md#account_get) | **GET** /account | [ / ] Account details
[**account_password_put**](AccountApi.md#account_password_put) | **PUT** /account/password | [ /password ] Update password
[**account_two_factor_delete**](AccountApi.md#account_two_factor_delete) | **DELETE** /account/two-factor | [ /two-factor ] Disable 2FA
[**account_two_factor_get**](AccountApi.md#account_two_factor_get) | **GET** /account/two-factor | [ /two-factor ] 2FA details
[**account_two_factor_post**](AccountApi.md#account_two_factor_post) | **POST** /account/two-factor | [ /two-factor ] Enable 2FA


# **account_api_keys_get**
> bool, date, datetime, dict, float, int, list, str, none_type account_api_keys_get(accept, content_type)

[ /api-keys ] List API keys

Retries a list of API keys  <!-- RESPONSE 200 --> {   \"object\": \"list\",   \"data\": [     {       \"object\": \"api_key\",       \"attributes\": {         \"identifier\": \"wwQ5DJ6X1XaFznQS\",         \"description\": \"API Docs\",         \"allowed_ips\": [],         \"last_used_at\": \"2020-06-03T15:04:47+01:00\",         \"created_at\": \"2020-05-18T00:12:43+01:00\"       }     }   ] } <!-- ENDRESPONSE -->

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

    # example passing only required values which don't have defaults set
    try:
        # [ /api-keys ] List API keys
        api_response = api_instance.account_api_keys_get(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling AccountApi->account_api_keys_get: %s\n" % e)
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

# **account_api_keys_post**
> bool, date, datetime, dict, float, int, list, str, none_type account_api_keys_post(accept, account_api_keys_post_request)

[ /api-keys ] Create API key

Generates a new API key  ## Fields | Name        | Required? | Type   | Description          | Rules | |-------------|-----------|--------|----------------------|-------| | description | required  | string | Note for the API key |       | | allowed_ips |           | object | List of allowed IPs  |       |  <!-- RESPONSE 201 --> {   \"object\": \"api_key\",   \"attributes\": {     \"identifier\": \"yjAZbHMyKrv9YRZ0\",     \"description\": \"Restricted IPs\",     \"allowed_ips\": [       \"127.0.0.1\",       \"192.168.0.1\"     ],     \"last_used_at\": null,     \"created_at\": \"2020-08-17T04:44:42+01:00\"   },   \"meta\": {     \"secret_token\": \"wiHiMbmgjLOkA2fPzRD6KdMe7Q9Cqaka\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import account_api
from pterodactyl_client.model.account_api_keys_post_request import AccountApiKeysPostRequest
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
    account_api_keys_post_request = AccountApiKeysPostRequest(None) # AccountApiKeysPostRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ /api-keys ] Create API key
        api_response = api_instance.account_api_keys_post(accept, account_api_keys_post_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling AccountApi->account_api_keys_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **account_api_keys_post_request** | [**AccountApiKeysPostRequest**](AccountApiKeysPostRequest.md)|  |

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

# **account_email_put**
> bool, date, datetime, dict, float, int, list, str, none_type account_email_put(accept, account_email_put_request)

[ /email ] Update email

Updates the email address of the account  ## Fields | Name     | Required? | Type   | Description       | Rules | |----------|-----------|--------|-------------------|-------| | email    | required  | string | New email         |       | | password | required  | string | Existing password |       |  <!-- RESPONSE 201 --> // Successful <!-- ENDRESPONSE -->  <!-- RESPONSE 400 --> // Invalid email format {   \"errors\": [     {       \"code\": \"email\",       \"detail\": \"The email must be a valid email address.\",       \"source\": {         \"field\": \"email\"       }     }   ] } <!-- ENDRESPONSE -->  <!-- RESPONSE 400 --> // Invalid password {   \"errors\": [     {       \"code\": \"InvalidPasswordProvidedException\",       \"status\": \"400\",       \"detail\": \"The password provided was invalid for this account.\"     }   ] } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import account_api
from pterodactyl_client.model.account_email_put_request import AccountEmailPutRequest
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
    account_email_put_request = AccountEmailPutRequest(None) # AccountEmailPutRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ /email ] Update email
        api_response = api_instance.account_email_put(accept, account_email_put_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling AccountApi->account_email_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **account_email_put_request** | [**AccountEmailPutRequest**](AccountEmailPutRequest.md)|  |

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

# **account_get**
> bool, date, datetime, dict, float, int, list, str, none_type account_get(accept, content_type)

[ / ] Account details

Retrieves information about the account  <!-- RESPONSE 200 --> {   \"object\": \"user\",   \"attributes\": {     \"id\": 1,     \"admin\": true,     \"username\": \"admin\",     \"email\": \"example@example.com\",     \"first_name\": \"Admin\",     \"last_name\": \"User\",     \"language\": \"en\"   } } <!-- ENDRESPONSE -->

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

    # example passing only required values which don't have defaults set
    try:
        # [ / ] Account details
        api_response = api_instance.account_get(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling AccountApi->account_get: %s\n" % e)
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

# **account_password_put**
> bool, date, datetime, dict, float, int, list, str, none_type account_password_put(accept, account_password_put_request)

[ /password ] Update password

Updates the password of the account  ## Fields | Name                  | Required? | Type   | Description          | Rules | |-----------------------|-----------|--------|----------------------|-------| | current_password      | required  | string | Existing password    |       | | password              | required  | string | New password         |       | | password_confirmation | required  | string | Confirm new password |       |  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import account_api
from pterodactyl_client.model.account_password_put_request import AccountPasswordPutRequest
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
    account_password_put_request = AccountPasswordPutRequest(None) # AccountPasswordPutRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ /password ] Update password
        api_response = api_instance.account_password_put(accept, account_password_put_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling AccountApi->account_password_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **account_password_put_request** | [**AccountPasswordPutRequest**](AccountPasswordPutRequest.md)|  |

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

# **account_two_factor_delete**
> bool, date, datetime, dict, float, int, list, str, none_type account_two_factor_delete(accept)

[ /two-factor ] Disable 2FA

Disables TOTP 2FA on the account  ## Fields | Name     | Required? | Type   | Description       | Rules | |----------|-----------|--------|-------------------|-------| | password | required  | string | Existing password |       |  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->  <!-- RESPONSE 400 --> // Incorrect password {   \"errors\": [     {       \"code\": \"BadRequestHttpException\",       \"status\": \"400\",       \"detail\": \"An error was encountered while processing this request.\"     }   ] } <!-- ENDRESPONSE -->

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

    # example passing only required values which don't have defaults set
    try:
        # [ /two-factor ] Disable 2FA
        api_response = api_instance.account_two_factor_delete(accept)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling AccountApi->account_two_factor_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **content_type** | **str**|  | defaults to "application/json"

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

# **account_two_factor_get**
> bool, date, datetime, dict, float, int, list, str, none_type account_two_factor_get(accept, content_type)

[ /two-factor ] 2FA details

Generates a TOTP QR code image to allow the setup of 2FA  <!-- RESPONSE 200 --> {   \"data\": {     \"image_url_data\": \"otpauth://totp/Pterodactyl:example%40example.com?secret=LGYOWJEGVRPPGPWATP5ZHOYC7DHAYQ6S&issuer=Pterodactyl\"   } } <!-- ENDRESPONSE -->

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

    # example passing only required values which don't have defaults set
    try:
        # [ /two-factor ] 2FA details
        api_response = api_instance.account_two_factor_get(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling AccountApi->account_two_factor_get: %s\n" % e)
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

# **account_two_factor_post**
> bool, date, datetime, dict, float, int, list, str, none_type account_two_factor_post(accept, account_two_factor_post_request)

[ /two-factor ] Enable 2FA

Enables TOTP 2FA using the QR code generated by the GET request  Uses code generated from `GET /account/two-factor`  ## Fields | Name    | Required? | Type   | Description       | Rules | |---------|-----------|--------|-------------------|-------| | code    | required  | string | TOTP Code         |       |  <!-- RESPONSE 200 --> {   \"object\": \"recovery_tokens\",   \"attributes\": {     \"tokens\": [       \"MpBjHH8O08\",       \"D9H0hktN6L\",       \"ho8KiUpeV8\",       \"06vZEfrYPf\",       \"nFRySZ2ryh\",       \"7K1cTrhGoV\",       \"n6xpwwlJfv\",       \"hAmyCsZxYO\",       \"5FiMKFyNpH\",       \"IViSFoRFvW\"     ]   } } <!-- ENDRESPONSE -->  <!-- RESPONSE 400 --> {   \"errors\": [     {       \"code\": \"TwoFactorAuthenticationTokenInvalid\",       \"status\": \"400\",       \"detail\": \"The token provided is not valid.\"     }   ] } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import account_api
from pterodactyl_client.model.account_two_factor_post_request import AccountTwoFactorPostRequest
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
    account_two_factor_post_request = AccountTwoFactorPostRequest(None) # AccountTwoFactorPostRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ /two-factor ] Enable 2FA
        api_response = api_instance.account_two_factor_post(accept, account_two_factor_post_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling AccountApi->account_two_factor_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **account_two_factor_post_request** | [**AccountTwoFactorPostRequest**](AccountTwoFactorPostRequest.md)|  |

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

