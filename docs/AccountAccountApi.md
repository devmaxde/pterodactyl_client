# pterodactyl_client.AccountAccountApi

All URIs are relative to *https://example.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**__accountdetails**](AccountAccountApi.md#__accountdetails) | **GET** /account | [ / ] Account details
[**__api_keys_create_ap_ikey**](AccountAccountApi.md#__api_keys_create_ap_ikey) | **POST** /account/api-keys | [ /api-keys ] Create API key
[**__api_keys_list_ap_ikeys**](AccountAccountApi.md#__api_keys_list_ap_ikeys) | **GET** /account/api-keys | [ /api-keys ] List API keys
[**__email_updateemail**](AccountAccountApi.md#__email_updateemail) | **PUT** /account/email | [ /email ] Update email
[**__password_updatepassword**](AccountAccountApi.md#__password_updatepassword) | **PUT** /account/password | [ /password ] Update password
[**__two_factor2_f_adetails**](AccountAccountApi.md#__two_factor2_f_adetails) | **GET** /account/two-factor | [ /two-factor ] 2FA details
[**__two_factor_disable2_fa**](AccountAccountApi.md#__two_factor_disable2_fa) | **DELETE** /account/two-factor | [ /two-factor ] Disable 2FA
[**__two_factor_enable2_fa**](AccountAccountApi.md#__two_factor_enable2_fa) | **POST** /account/two-factor | [ /two-factor ] Enable 2FA


# **__accountdetails**
> bool, date, datetime, dict, float, int, list, str, none_type __accountdetails(accept, content_type)

[ / ] Account details

Retrieves information about the account  <!-- RESPONSE 200 --> {   \"object\": \"user\",   \"attributes\": {     \"id\": 1,     \"admin\": true,     \"username\": \"admin\",     \"email\": \"example@example.com\",     \"first_name\": \"Admin\",     \"last_name\": \"User\",     \"language\": \"en\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import account_account_api
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
    api_instance = account_account_api.AccountAccountApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ / ] Account details
        api_response = api_instance.__accountdetails(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling AccountAccountApi->__accountdetails: %s\n" % e)
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

# **__api_keys_create_ap_ikey**
> bool, date, datetime, dict, float, int, list, str, none_type __api_keys_create_ap_ikey(accept, api_keys_create_ap_ikey_request)

[ /api-keys ] Create API key

Generates a new API key  ## Fields | Name        | Required? | Type   | Description          | Rules | |-------------|-----------|--------|----------------------|-------| | description | required  | string | Note for the API key |       | | allowed_ips |           | object | List of allowed IPs  |       |  <!-- RESPONSE 201 --> {   \"object\": \"api_key\",   \"attributes\": {     \"identifier\": \"yjAZbHMyKrv9YRZ0\",     \"description\": \"Restricted IPs\",     \"allowed_ips\": [       \"127.0.0.1\",       \"192.168.0.1\"     ],     \"last_used_at\": null,     \"created_at\": \"2020-08-17T04:44:42+01:00\"   },   \"meta\": {     \"secret_token\": \"wiHiMbmgjLOkA2fPzRD6KdMe7Q9Cqaka\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import account_account_api
from pterodactyl_client.model.api_keys_create_ap_ikey_request import ApiKeysCreateAPIkeyRequest
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
    api_instance = account_account_api.AccountAccountApi(api_client)
    accept = "application/json" # str | 
    api_keys_create_ap_ikey_request = ApiKeysCreateAPIkeyRequest(None) # ApiKeysCreateAPIkeyRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ /api-keys ] Create API key
        api_response = api_instance.__api_keys_create_ap_ikey(accept, api_keys_create_ap_ikey_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling AccountAccountApi->__api_keys_create_ap_ikey: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **api_keys_create_ap_ikey_request** | [**ApiKeysCreateAPIkeyRequest**](ApiKeysCreateAPIkeyRequest.md)|  |

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

# **__api_keys_list_ap_ikeys**
> bool, date, datetime, dict, float, int, list, str, none_type __api_keys_list_ap_ikeys(accept, content_type)

[ /api-keys ] List API keys

Retries a list of API keys  <!-- RESPONSE 200 --> {   \"object\": \"list\",   \"data\": [     {       \"object\": \"api_key\",       \"attributes\": {         \"identifier\": \"wwQ5DJ6X1XaFznQS\",         \"description\": \"API Docs\",         \"allowed_ips\": [],         \"last_used_at\": \"2020-06-03T15:04:47+01:00\",         \"created_at\": \"2020-05-18T00:12:43+01:00\"       }     }   ] } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import account_account_api
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
    api_instance = account_account_api.AccountAccountApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /api-keys ] List API keys
        api_response = api_instance.__api_keys_list_ap_ikeys(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling AccountAccountApi->__api_keys_list_ap_ikeys: %s\n" % e)
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

# **__email_updateemail**
> bool, date, datetime, dict, float, int, list, str, none_type __email_updateemail(accept, email_updateemail_request)

[ /email ] Update email

Updates the email address of the account  ## Fields | Name     | Required? | Type   | Description       | Rules | |----------|-----------|--------|-------------------|-------| | email    | required  | string | New email         |       | | password | required  | string | Existing password |       |  <!-- RESPONSE 201 --> // Successful <!-- ENDRESPONSE -->  <!-- RESPONSE 400 --> // Invalid email format {   \"errors\": [     {       \"code\": \"email\",       \"detail\": \"The email must be a valid email address.\",       \"source\": {         \"field\": \"email\"       }     }   ] } <!-- ENDRESPONSE -->  <!-- RESPONSE 400 --> // Invalid password {   \"errors\": [     {       \"code\": \"InvalidPasswordProvidedException\",       \"status\": \"400\",       \"detail\": \"The password provided was invalid for this account.\"     }   ] } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import account_account_api
from pterodactyl_client.model.email_updateemail_request import EmailUpdateemailRequest
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
    api_instance = account_account_api.AccountAccountApi(api_client)
    accept = "application/json" # str | 
    email_updateemail_request = EmailUpdateemailRequest(None) # EmailUpdateemailRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ /email ] Update email
        api_response = api_instance.__email_updateemail(accept, email_updateemail_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling AccountAccountApi->__email_updateemail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **email_updateemail_request** | [**EmailUpdateemailRequest**](EmailUpdateemailRequest.md)|  |

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

# **__password_updatepassword**
> bool, date, datetime, dict, float, int, list, str, none_type __password_updatepassword(accept, password_updatepassword_request)

[ /password ] Update password

Updates the password of the account  ## Fields | Name                  | Required? | Type   | Description          | Rules | |-----------------------|-----------|--------|----------------------|-------| | current_password      | required  | string | Existing password    |       | | password              | required  | string | New password         |       | | password_confirmation | required  | string | Confirm new password |       |  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import account_account_api
from pterodactyl_client.model.password_updatepassword_request import PasswordUpdatepasswordRequest
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
    api_instance = account_account_api.AccountAccountApi(api_client)
    accept = "application/json" # str | 
    password_updatepassword_request = PasswordUpdatepasswordRequest(None) # PasswordUpdatepasswordRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ /password ] Update password
        api_response = api_instance.__password_updatepassword(accept, password_updatepassword_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling AccountAccountApi->__password_updatepassword: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **password_updatepassword_request** | [**PasswordUpdatepasswordRequest**](PasswordUpdatepasswordRequest.md)|  |

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

# **__two_factor2_f_adetails**
> bool, date, datetime, dict, float, int, list, str, none_type __two_factor2_f_adetails(accept, content_type)

[ /two-factor ] 2FA details

Generates a TOTP QR code image to allow the setup of 2FA  <!-- RESPONSE 200 --> {   \"data\": {     \"image_url_data\": \"otpauth://totp/Pterodactyl:example%40example.com?secret=LGYOWJEGVRPPGPWATP5ZHOYC7DHAYQ6S&issuer=Pterodactyl\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import account_account_api
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
    api_instance = account_account_api.AccountAccountApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /two-factor ] 2FA details
        api_response = api_instance.__two_factor2_f_adetails(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling AccountAccountApi->__two_factor2_f_adetails: %s\n" % e)
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

# **__two_factor_disable2_fa**
> bool, date, datetime, dict, float, int, list, str, none_type __two_factor_disable2_fa(accept)

[ /two-factor ] Disable 2FA

Disables TOTP 2FA on the account  ## Fields | Name     | Required? | Type   | Description       | Rules | |----------|-----------|--------|-------------------|-------| | password | required  | string | Existing password |       |  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->  <!-- RESPONSE 400 --> // Incorrect password {   \"errors\": [     {       \"code\": \"BadRequestHttpException\",       \"status\": \"400\",       \"detail\": \"An error was encountered while processing this request.\"     }   ] } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import account_account_api
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
    api_instance = account_account_api.AccountAccountApi(api_client)
    accept = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /two-factor ] Disable 2FA
        api_response = api_instance.__two_factor_disable2_fa(accept)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling AccountAccountApi->__two_factor_disable2_fa: %s\n" % e)
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

# **__two_factor_enable2_fa**
> bool, date, datetime, dict, float, int, list, str, none_type __two_factor_enable2_fa(accept, two_factor_enable2_fa_request)

[ /two-factor ] Enable 2FA

Enables TOTP 2FA using the QR code generated by the GET request  Uses code generated from `GET /account/two-factor`  ## Fields | Name    | Required? | Type   | Description       | Rules | |---------|-----------|--------|-------------------|-------| | code    | required  | string | TOTP Code         |       |  <!-- RESPONSE 200 --> {   \"object\": \"recovery_tokens\",   \"attributes\": {     \"tokens\": [       \"MpBjHH8O08\",       \"D9H0hktN6L\",       \"ho8KiUpeV8\",       \"06vZEfrYPf\",       \"nFRySZ2ryh\",       \"7K1cTrhGoV\",       \"n6xpwwlJfv\",       \"hAmyCsZxYO\",       \"5FiMKFyNpH\",       \"IViSFoRFvW\"     ]   } } <!-- ENDRESPONSE -->  <!-- RESPONSE 400 --> {   \"errors\": [     {       \"code\": \"TwoFactorAuthenticationTokenInvalid\",       \"status\": \"400\",       \"detail\": \"The token provided is not valid.\"     }   ] } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import account_account_api
from pterodactyl_client.model.two_factor_enable2_fa_request import TwoFactorEnable2FARequest
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
    api_instance = account_account_api.AccountAccountApi(api_client)
    accept = "application/json" # str | 
    two_factor_enable2_fa_request = TwoFactorEnable2FARequest(None) # TwoFactorEnable2FARequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ /two-factor ] Enable 2FA
        api_response = api_instance.__two_factor_enable2_fa(accept, two_factor_enable2_fa_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling AccountAccountApi->__two_factor_enable2_fa: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **two_factor_enable2_fa_request** | [**TwoFactorEnable2FARequest**](TwoFactorEnable2FARequest.md)|  |

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

