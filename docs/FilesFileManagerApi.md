# pterodactyl_client.FilesFileManagerApi

All URIs are relative to *https://example.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**__compress_compressfile**](FilesFileManagerApi.md#__compress_compressfile) | **POST** /client/servers/1a7ce997/files/compress | [ /compress ] Compress file
[**__contents_getfilecontents**](FilesFileManagerApi.md#__contents_getfilecontents) | **GET** /client/servers/1a7ce997/files/contents | [ /contents ] Get file contents
[**__copy_copyfile**](FilesFileManagerApi.md#__copy_copyfile) | **POST** /client/servers/1a7ce997/files/copy | [ /copy ] Copy file
[**__create_folder_createfolder**](FilesFileManagerApi.md#__create_folder_createfolder) | **POST** /client/servers/1a7ce997/files/create-folder | [ /create-folder ] Create folder
[**__decompress_decompressfile**](FilesFileManagerApi.md#__decompress_decompressfile) | **POST** /client/servers/1a7ce997/files/decompress | [ /decompress ] Decompress file
[**__delete_deletefile**](FilesFileManagerApi.md#__delete_deletefile) | **POST** /client/servers/1a7ce997/files/delete | [ /delete] Delete file
[**__download_downloadfile**](FilesFileManagerApi.md#__download_downloadfile) | **GET** /client/servers/1a7ce997/files/download | [ /download ] Download file
[**__list_listfiles**](FilesFileManagerApi.md#__list_listfiles) | **GET** /client/servers/1a7ce997/files/list | [ /list ] List files
[**__rename_renamefile**](FilesFileManagerApi.md#__rename_renamefile) | **PUT** /client/servers/1a7ce997/files/rename | [ /rename ] Rename file
[**__upload_uploadfile**](FilesFileManagerApi.md#__upload_uploadfile) | **GET** /client/servers/1a7ce997/files/upload | [ /upload ] Upload file
[**__write_writefile**](FilesFileManagerApi.md#__write_writefile) | **POST** /client/servers/1a7ce997/files/write | [ /write ] Write file


# **__compress_compressfile**
> bool, date, datetime, dict, float, int, list, str, none_type __compress_compressfile(accept, compress_compressfile_request)

[ /compress ] Compress file

Compresses the specified file  <!-- RESPONSE 200 --> {   \"object\": \"file_object\",   \"attributes\": {     \"name\": \"archive-2020-08-23T220805Z.tar.gz\",     \"mode\": \"-rw-------\",     \"size\": 0,     \"is_file\": true,     \"is_symlink\": false,     \"is_editable\": false,     \"mimetype\": \"application/tar+gzip\",     \"created_at\": \"2020-08-23T22:08:05+00:00\",     \"modified_at\": \"2020-08-23T22:08:05+00:00\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import files_file_manager_api
from pterodactyl_client.model.compress_compressfile_request import CompressCompressfileRequest
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
    api_instance = files_file_manager_api.FilesFileManagerApi(api_client)
    accept = "application/json" # str | 
    compress_compressfile_request = CompressCompressfileRequest(None) # CompressCompressfileRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ /compress ] Compress file
        api_response = api_instance.__compress_compressfile(accept, compress_compressfile_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling FilesFileManagerApi->__compress_compressfile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **compress_compressfile_request** | [**CompressCompressfileRequest**](CompressCompressfileRequest.md)|  |

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

# **__contents_getfilecontents**
> bool, date, datetime, dict, float, int, list, str, none_type __contents_getfilecontents(accept, content_type)

[ /contents ] Get file contents

Displays the contents of the specified file  ## Available parameters | Parameter | Description                          | |-----------|--------------------------------------| | file      | URL encoded path to the desired file |  <!-- RESPONSE 200 --> # This is the main configuration file for Paper. # As you can see, there's tons to configure. Some options may impact gameplay, so use # with caution, and make sure you know what each option does before configuring. #  # If you need help with the configuration or have any questions related to Paper, # join us in our Discord or IRC channel. #  # Discord: https://paperdiscord.emc.gs # IRC: #paper @ irc.spi.gt ( http://irc.spi.gt/iris/?channels=paper ) # Website: https://papermc.io/  # Docs: https://paper.readthedocs.org/   verbose: false config-version: 20 settings:   load-permissions-yml-before-plugins: true   bungee-online-mode: true   region-file-cache-size: 256   incoming-packet-spam-threshold: 300   save-player-data: true   use-alternative-luck-formula: false   suggest-player-names-when-null-tab-completions: true   enable-player-collisions: true   save-empty-scoreboard-teams: false   velocity-support:     enabled: false     online-mode: false     secret: ''   async-chunks:     enable: true     load-threads: -1   watchdog:     early-warning-every: 5000     early-warning-delay: 10000   spam-limiter:     tab-spam-increment: 1     tab-spam-limit: 500   book-size:     page-max: 2560     total-multiplier: 0.98 messages:   no-permission: '&cI''m sorry, but you do not have permission to perform this command.     Please contact the server administrators if you believe that this is in error.'   kick:     authentication-servers-down: ''     connection-throttle: Connection throttled! Please wait before reconnecting.     flying-player: Flying is not enabled on this server     flying-vehicle: Flying is not enabled on this server timings:   enabled: true   verbose: true   server-name-privacy: false   hidden-config-entries:   - database   - settings.bungeecord-addresses   history-interval: 300   history-length: 3600   server-name: Unknown Server world-settings:   default:     per-player-mob-spawns: false     optimize-explosions: false     portal-search-radius: 128     disable-teleportation-suffocation-check: false     fixed-chunk-inhabited-time: -1     use-vanilla-world-scoreboard-name-coloring: false     remove-corrupt-tile-entities: false     enable-treasure-maps: true     treasure-maps-return-already-discovered: false     experience-merge-max-value: -1     prevent-moving-into-unloaded-chunks: false     max-auto-save-chunks-per-tick: 24     falling-block-height-nerf: 0     tnt-entity-height-nerf: 0     filter-nbt-data-from-spawn-eggs-and-related: true     max-entity-collisions: 8     disable-creeper-lingering-effect: false     duplicate-uuid-resolver: saferegen     duplicate-uuid-saferegen-delete-range: 32     prevent-tnt-from-moving-in-water: false     disable-thunder: false     skeleton-horse-thunder-spawn-chance: 0.01     disable-ice-and-snow: false     count-all-mobs-for-spawning: false     keep-spawn-loaded-range: 10     keep-spawn-loaded: true     auto-save-interval: -1     armor-stands-do-collision-entity-lookups: true     non-player-arrow-despawn-rate: -1     creative-arrow-despawn-rate: -1     nether-ceiling-void-damage-height: 0     grass-spread-tick-rate: 1     water-over-lava-flow-speed: 5     bed-search-radius: 1     fix-zero-tick-instant-grow-farms: true     use-faster-eigencraft-redstone: false     allow-non-player-entities-on-scoreboards: false     disable-explosion-knockback: false     container-update-tick-rate: 1     parrots-are-unaffected-by-player-movement: false     armor-stands-tick: true     spawner-nerfed-mobs-should-jump: false     entities-target-with-follow-range: false     allow-leashing-undead-horse: false     baby-zombie-movement-modifier: 0.5     mob-spawner-tick-rate: 1     all-chunks-are-slime-chunks: false     game-mechanics:       scan-for-legacy-ender-dragon: true       disable-pillager-patrols: false       disable-relative-projectile-velocity: false       disable-chest-cat-detection: false       shield-blocking-delay: 5       disable-end-credits: false       disable-player-crits: false       disable-sprint-interruption-on-attack: false       disable-unloaded-chunk-enderpearl-exploit: true     max-growth-height:       cactus: 3       reeds: 3     fishing-time-range:       MinimumTicks: 100       MaximumTicks: 600     despawn-ranges:       soft: 32       hard: 128     lightning-strike-distance-limit:       sound: -1       impact-sound: -1       flash: -1     frosted-ice:       enabled: true       delay:         min: 20         max: 40     lootables:       auto-replenish: false       restrict-player-reloot: true       reset-seed-on-fill: true       max-refills: -1       refresh-min: 12h       refresh-max: 2d     alt-item-despawn-rate:       enabled: false       items:         COBBLESTONE: 300     hopper:       cooldown-when-full: true       disable-move-event: false     anti-xray:       enabled: false       engine-mode: 1       chunk-edge-mode: 2       max-chunk-section-index: 3       update-radius: 2       hidden-blocks:       - gold_ore       - iron_ore       - coal_ore       - lapis_ore       - mossy_cobblestone       - obsidian       - chest       - diamond_ore       - redstone_ore       - clay       - emerald_ore       - ender_chest       replacement-blocks:       - stone       - oak_planks     generator-settings:       flat-bedrock: false     squid-spawn-height:       maximum: 0.0 <!-- ENDRESPONSE --> 

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import files_file_manager_api
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
    api_instance = files_file_manager_api.FilesFileManagerApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 
    file = "/paper.yml" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # [ /contents ] Get file contents
        api_response = api_instance.__contents_getfilecontents(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling FilesFileManagerApi->__contents_getfilecontents: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # [ /contents ] Get file contents
        api_response = api_instance.__contents_getfilecontents(accept, content_type, file=file)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling FilesFileManagerApi->__contents_getfilecontents: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **content_type** | **str**|  |
 **file** | **str**|  | [optional]

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

# **__copy_copyfile**
> bool, date, datetime, dict, float, int, list, str, none_type __copy_copyfile(accept, copy_copyfile_request)

[ /copy ] Copy file

Copies the specified file  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import files_file_manager_api
from pterodactyl_client.model.copy_copyfile_request import CopyCopyfileRequest
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
    api_instance = files_file_manager_api.FilesFileManagerApi(api_client)
    accept = "application/json" # str | 
    copy_copyfile_request = CopyCopyfileRequest(None) # CopyCopyfileRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ /copy ] Copy file
        api_response = api_instance.__copy_copyfile(accept, copy_copyfile_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling FilesFileManagerApi->__copy_copyfile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **copy_copyfile_request** | [**CopyCopyfileRequest**](CopyCopyfileRequest.md)|  |

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

# **__create_folder_createfolder**
> bool, date, datetime, dict, float, int, list, str, none_type __create_folder_createfolder(accept, create_folder_createfolder_request)

[ /create-folder ] Create folder

Creates the specified folder in the specified directory  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import files_file_manager_api
from pterodactyl_client.model.create_folder_createfolder_request import CreateFolderCreatefolderRequest
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
    api_instance = files_file_manager_api.FilesFileManagerApi(api_client)
    accept = "application/json" # str | 
    create_folder_createfolder_request = CreateFolderCreatefolderRequest(None) # CreateFolderCreatefolderRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ /create-folder ] Create folder
        api_response = api_instance.__create_folder_createfolder(accept, create_folder_createfolder_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling FilesFileManagerApi->__create_folder_createfolder: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **create_folder_createfolder_request** | [**CreateFolderCreatefolderRequest**](CreateFolderCreatefolderRequest.md)|  |

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

# **__decompress_decompressfile**
> bool, date, datetime, dict, float, int, list, str, none_type __decompress_decompressfile(accept, decompress_decompressfile_request)

[ /decompress ] Decompress file

Decompresses the selected file  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import files_file_manager_api
from pterodactyl_client.model.decompress_decompressfile_request import DecompressDecompressfileRequest
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
    api_instance = files_file_manager_api.FilesFileManagerApi(api_client)
    accept = "application/json" # str | 
    decompress_decompressfile_request = DecompressDecompressfileRequest(None) # DecompressDecompressfileRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ /decompress ] Decompress file
        api_response = api_instance.__decompress_decompressfile(accept, decompress_decompressfile_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling FilesFileManagerApi->__decompress_decompressfile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **decompress_decompressfile_request** | [**DecompressDecompressfileRequest**](DecompressDecompressfileRequest.md)|  |

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

# **__delete_deletefile**
> bool, date, datetime, dict, float, int, list, str, none_type __delete_deletefile(accept, delete_deletefile_request)

[ /delete] Delete file

Deletes the specified file(s) or folder(s)  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import files_file_manager_api
from pterodactyl_client.model.delete_deletefile_request import DeleteDeletefileRequest
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
    api_instance = files_file_manager_api.FilesFileManagerApi(api_client)
    accept = "application/json" # str | 
    delete_deletefile_request = DeleteDeletefileRequest(None) # DeleteDeletefileRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ /delete] Delete file
        api_response = api_instance.__delete_deletefile(accept, delete_deletefile_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling FilesFileManagerApi->__delete_deletefile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **delete_deletefile_request** | [**DeleteDeletefileRequest**](DeleteDeletefileRequest.md)|  |

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

# **__download_downloadfile**
> bool, date, datetime, dict, float, int, list, str, none_type __download_downloadfile(accept, content_type)

[ /download ] Download file

Generates a one-time link to download the specified file  ## Available parameters | Parameter | Description                  | |-----------|------------------------------| | file      | URL encoded path to the desired file |  <!-- RESPONSE 200 --> {   \"object\": \"signed_url\",   \"attributes\": {     \"url\": \"https://pterodactyl.file.properties:8080/download/file?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImp0aSI6IjdkYzAxNzVjODU4MTE5MDRlMjJjNTcxNjBhMjkwMjgwZGFjMDMzM2I2ZmJhMTE3YTI4YjdhMDM5Y2U1OTg0YzcifQ.eyJpc3MiOiJodHRwczpcL1wvcHRlcm9kYWN0eWwuZmlsZS5wcm9wZXJ0aWVzIiwiYXVkIjoiaHR0cHM6XC9cL3B0ZXJvZGFjdHlsLmZpbGUucHJvcGVydGllczo4MDgwIiwianRpIjoiN2RjMDE3NWM4NTgxMTkwNGUyMmM1NzE2MGEyOTAyODBkYWMwMzMzYjZmYmExMTdhMjhiN2EwMzljZTU5ODRjNyIsImlhdCI6MTU5NDY0ODEwMCwibmJmIjoxNTk0NjQ3ODAwLCJleHAiOjE1OTQ2NDkwMDAsImZpbGVfcGF0aCI6IlwvZXVsYS50eHQiLCJzZXJ2ZXJfdXVpZCI6IjFhN2NlOTk3LTI1OWItNDUyZS04YjRlLWNlY2M0NjQxNDJjYSIsInVuaXF1ZV9pZCI6IlNvWUdIamNaNmhKUVlieHUifQ.h4eBmxDXf-4GAwVuAWZFU5QTqd62jw7HTre4aKQGpvw\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import files_file_manager_api
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
    api_instance = files_file_manager_api.FilesFileManagerApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 
    file = "/eula.txt" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # [ /download ] Download file
        api_response = api_instance.__download_downloadfile(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling FilesFileManagerApi->__download_downloadfile: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # [ /download ] Download file
        api_response = api_instance.__download_downloadfile(accept, content_type, file=file)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling FilesFileManagerApi->__download_downloadfile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **content_type** | **str**|  |
 **file** | **str**|  | [optional]

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

# **__list_listfiles**
> bool, date, datetime, dict, float, int, list, str, none_type __list_listfiles(accept, content_type)

[ /list ] List files

Lists all files of the server  ## Available parameters | Parameter | Description                         | |-----------|-------------------------------------| | directory | URL encoded path to list files from |  <!-- RESPONSE 200 --> {   \"object\": \"list\",   \"data\": [     {       \"object\": \"file_object\",       \"attributes\": {         \"name\": \"cache\",         \"mode\": \"drwxr-xr-x\",         \"size\": 4096,         \"is_file\": false,         \"is_symlink\": false,         \"is_editable\": false,         \"mimetype\": \"inode/directory\",         \"created_at\": \"2020-07-13T12:41:55+00:00\",         \"modified_at\": \"2019-12-25T05:20:36+00:00\"       }     },     {       \"object\": \"file_object\",       \"attributes\": {         \"name\": \"logs\",         \"mode\": \"drwxr-xr-x\",         \"size\": 4096,         \"is_file\": false,         \"is_symlink\": false,         \"is_editable\": false,         \"mimetype\": \"inode/directory\",         \"created_at\": \"2020-07-13T12:42:02+00:00\",         \"modified_at\": \"2020-07-13T12:42:02+00:00\"       }     },     {       \"object\": \"file_object\",       \"attributes\": {         \"name\": \"plugins\",         \"mode\": \"drwxr-xr-x\",         \"size\": 4096,         \"is_file\": false,         \"is_symlink\": false,         \"is_editable\": false,         \"mimetype\": \"inode/directory\",         \"created_at\": \"2020-07-13T12:41:55+00:00\",         \"modified_at\": \"2019-12-25T05:21:07+00:00\"       }     },     {       \"object\": \"file_object\",       \"attributes\": {         \"name\": \"world\",         \"mode\": \"drwxr-xr-x\",         \"size\": 4096,         \"is_file\": false,         \"is_symlink\": false,         \"is_editable\": false,         \"mimetype\": \"inode/directory\",         \"created_at\": \"2020-07-13T13:26:22+00:00\",         \"modified_at\": \"2020-07-13T13:26:22+00:00\"       }     },     {       \"object\": \"file_object\",       \"attributes\": {         \"name\": \"world_nether\",         \"mode\": \"drwxr-xr-x\",         \"size\": 4096,         \"is_file\": false,         \"is_symlink\": false,         \"is_editable\": false,         \"mimetype\": \"inode/directory\",         \"created_at\": \"2020-07-13T12:41:55+00:00\",         \"modified_at\": \"2019-12-25T05:21:15+00:00\"       }     },     {       \"object\": \"file_object\",       \"attributes\": {         \"name\": \"world_the_end\",         \"mode\": \"drwxr-xr-x\",         \"size\": 4096,         \"is_file\": false,         \"is_symlink\": false,         \"is_editable\": false,         \"mimetype\": \"inode/directory\",         \"created_at\": \"2020-07-13T12:41:55+00:00\",         \"modified_at\": \"2019-12-25T05:21:15+00:00\"       }     },     {       \"object\": \"file_object\",       \"attributes\": {         \"name\": \"whitelist.json\",         \"mode\": \"-rw-r--r--\",         \"size\": 2,         \"is_file\": true,         \"is_symlink\": false,         \"is_editable\": true,         \"mimetype\": \"application/json\",         \"created_at\": \"2020-07-13T12:41:55+00:00\",         \"modified_at\": \"2019-12-25T05:21:07+00:00\"       }     },     {       \"object\": \"file_object\",       \"attributes\": {         \"name\": \"version_history.json\",         \"mode\": \"-rw-r--r--\",         \"size\": 46,         \"is_file\": true,         \"is_symlink\": false,         \"is_editable\": true,         \"mimetype\": \"application/json\",         \"created_at\": \"2020-07-13T12:41:55+00:00\",         \"modified_at\": \"2019-12-25T05:21:08+00:00\"       }     },     {       \"object\": \"file_object\",       \"attributes\": {         \"name\": \"usercache.json\",         \"mode\": \"-rw-r--r--\",         \"size\": 2,         \"is_file\": true,         \"is_symlink\": false,         \"is_editable\": true,         \"mimetype\": \"application/json\",         \"created_at\": \"2020-07-13T12:42:03+00:00\",         \"modified_at\": \"2020-07-13T12:42:03+00:00\"       }     },     {       \"object\": \"file_object\",       \"attributes\": {         \"name\": \"spigot.yml\",         \"mode\": \"-rw-r--r--\",         \"size\": 3567,         \"is_file\": true,         \"is_symlink\": false,         \"is_editable\": true,         \"mimetype\": \"text/plain\",         \"created_at\": \"2020-07-13T12:41:55+00:00\",         \"modified_at\": \"2020-06-12T21:44:42+00:00\"       }     },     {       \"object\": \"file_object\",       \"attributes\": {         \"name\": \"server.properties\",         \"mode\": \"-rw-r--r--\",         \"size\": 955,         \"is_file\": true,         \"is_symlink\": false,         \"is_editable\": true,         \"mimetype\": \"text/plain\",         \"created_at\": \"2020-07-13T12:41:59+00:00\",         \"modified_at\": \"2020-07-13T12:41:59+00:00\"       }     },     {       \"object\": \"file_object\",       \"attributes\": {         \"name\": \"server.jar\",         \"mode\": \"-rw-r--r--\",         \"size\": 36175593,         \"is_file\": true,         \"is_symlink\": false,         \"is_editable\": false,         \"mimetype\": \"application/jar\",         \"created_at\": \"2020-07-13T12:41:55+00:00\",         \"modified_at\": \"2020-06-12T22:38:46+00:00\"       }     },     {       \"object\": \"file_object\",       \"attributes\": {         \"name\": \"permissions.yml\",         \"mode\": \"-rw-r--r--\",         \"size\": 0,         \"is_file\": true,         \"is_symlink\": false,         \"is_editable\": true,         \"mimetype\": \"inode/x-empty\",         \"created_at\": \"2020-07-13T12:41:55+00:00\",         \"modified_at\": \"2019-12-25T05:21:08+00:00\"       }     },     {       \"object\": \"file_object\",       \"attributes\": {         \"name\": \"paper.yml\",         \"mode\": \"-rw-r--r--\",         \"size\": 5310,         \"is_file\": true,         \"is_symlink\": false,         \"is_editable\": true,         \"mimetype\": \"text/plain\",         \"created_at\": \"2020-07-13T12:41:55+00:00\",         \"modified_at\": \"2020-06-12T21:44:42+00:00\"       }     },     {       \"object\": \"file_object\",       \"attributes\": {         \"name\": \"ops.json\",         \"mode\": \"-rw-r--r--\",         \"size\": 2,         \"is_file\": true,         \"is_symlink\": false,         \"is_editable\": true,         \"mimetype\": \"application/json\",         \"created_at\": \"2020-07-13T12:42:03+00:00\",         \"modified_at\": \"2020-07-13T12:42:03+00:00\"       }     },     {       \"object\": \"file_object\",       \"attributes\": {         \"name\": \"hs_err_pid25.log\",         \"mode\": \"-rw-r--r--\",         \"size\": 57099,         \"is_file\": true,         \"is_symlink\": false,         \"is_editable\": true,         \"mimetype\": \"text/plain\",         \"created_at\": \"2020-07-13T12:41:55+00:00\",         \"modified_at\": \"2020-06-12T20:36:55+00:00\"       }     },     {       \"object\": \"file_object\",       \"attributes\": {         \"name\": \"help.yml\",         \"mode\": \"-rw-r--r--\",         \"size\": 2576,         \"is_file\": true,         \"is_symlink\": false,         \"is_editable\": true,         \"mimetype\": \"text/plain\",         \"created_at\": \"2020-07-13T12:41:55+00:00\",         \"modified_at\": \"2019-12-25T05:21:07+00:00\"       }     },     {       \"object\": \"file_object\",       \"attributes\": {         \"name\": \"eula.txt\",         \"mode\": \"-rw-r--r--\",         \"size\": 250,         \"is_file\": true,         \"is_symlink\": false,         \"is_editable\": true,         \"mimetype\": \"text/plain\",         \"created_at\": \"2020-07-13T12:41:55+00:00\",         \"modified_at\": \"2019-12-25T05:20:57+00:00\"       }     },     {       \"object\": \"file_object\",       \"attributes\": {         \"name\": \"commands.yml\",         \"mode\": \"-rw-r--r--\",         \"size\": 598,         \"is_file\": true,         \"is_symlink\": false,         \"is_editable\": true,         \"mimetype\": \"text/plain\",         \"created_at\": \"2020-07-13T12:41:55+00:00\",         \"modified_at\": \"2020-06-12T21:44:36+00:00\"       }     },     {       \"object\": \"file_object\",       \"attributes\": {         \"name\": \"bukkit.yml\",         \"mode\": \"-rw-r--r--\",         \"size\": 1053,         \"is_file\": true,         \"is_symlink\": false,         \"is_editable\": true,         \"mimetype\": \"text/plain\",         \"created_at\": \"2020-07-13T12:41:55+00:00\",         \"modified_at\": \"2020-06-12T21:44:36+00:00\"       }     },     {       \"object\": \"file_object\",       \"attributes\": {         \"name\": \"banned-players.json\",         \"mode\": \"-rw-r--r--\",         \"size\": 2,         \"is_file\": true,         \"is_symlink\": false,         \"is_editable\": true,         \"mimetype\": \"application/json\",         \"created_at\": \"2020-07-13T12:42:03+00:00\",         \"modified_at\": \"2020-07-13T12:42:03+00:00\"       }     },     {       \"object\": \"file_object\",       \"attributes\": {         \"name\": \"banned-ips.json\",         \"mode\": \"-rw-r--r--\",         \"size\": 2,         \"is_file\": true,         \"is_symlink\": false,         \"is_editable\": true,         \"mimetype\": \"application/json\",         \"created_at\": \"2020-07-13T12:42:03+00:00\",         \"modified_at\": \"2020-07-13T12:42:03+00:00\"       }     }   ] } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import files_file_manager_api
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
    api_instance = files_file_manager_api.FilesFileManagerApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 
    directory = "/cache" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # [ /list ] List files
        api_response = api_instance.__list_listfiles(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling FilesFileManagerApi->__list_listfiles: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # [ /list ] List files
        api_response = api_instance.__list_listfiles(accept, content_type, directory=directory)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling FilesFileManagerApi->__list_listfiles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **content_type** | **str**|  |
 **directory** | **str**|  | [optional]

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

# **__rename_renamefile**
> bool, date, datetime, dict, float, int, list, str, none_type __rename_renamefile(accept, rename_renamefile_request)

[ /rename ] Rename file

Renames the specified file(s) or folder(s)  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import files_file_manager_api
from pterodactyl_client.model.rename_renamefile_request import RenameRenamefileRequest
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
    api_instance = files_file_manager_api.FilesFileManagerApi(api_client)
    accept = "application/json" # str | 
    rename_renamefile_request = RenameRenamefileRequest(None) # RenameRenamefileRequest | 

    # example passing only required values which don't have defaults set
    try:
        # [ /rename ] Rename file
        api_response = api_instance.__rename_renamefile(accept, rename_renamefile_request)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling FilesFileManagerApi->__rename_renamefile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **rename_renamefile_request** | [**RenameRenamefileRequest**](RenameRenamefileRequest.md)|  |

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

# **__upload_uploadfile**
> bool, date, datetime, dict, float, int, list, str, none_type __upload_uploadfile(accept, content_type)

[ /upload ] Upload file

Returns a signed URL used to upload files to the server using POST  <!-- RESPONSE 200 --> {   \"object\": \"signed_url\",   \"attributes\": {     \"url\": \"https://pterodactyl.file.properties:8080/upload/file?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImp0aSI6IjdkYzAxNzVjODU4MTE5MDRlMjJjNTcxNjBhMjkwMjgwZGFjMDMzM2I2ZmJhMTE3YTI4YjdhMDM5Y2U1OTg0YzcifQ.eyJpc3MiOiJodHRwczpcL1wvcHRlcm9kYWN0eWwuZmlsZS5wcm9wZXJ0aWVzIiwiYXVkIjoiaHR0cHM6XC9cL3B0ZXJvZGFjdHlsLmZpbGUucHJvcGVydGllczo4MDgwIiwianRpIjoiN2RjMDE3NWM4NTgxMTkwNGUyMmM1NzE2MGEyOTAyODBkYWMwMzMzYjZmYmExMTdhMjhiN2EwMzljZTU5ODRjNyIsImlhdCI6MTU5ODIyMTMyMSwibmJmIjoxNTk4MjIxMDIxLCJleHAiOjE1OTgyMjIyMjEsInNlcnZlcl91dWlkIjoiMWE3Y2U5OTctMjU5Yi00NTJlLThiNGUtY2VjYzQ2NDE0MmNhIiwidW5pcXVlX2lkIjoiNmM2OFdkSkJTVzg0RlBsUiJ9.GJ5681K9ehhPCcXevyxw-RO1jhv4UWg5T8b_P7r6s8Q\"   } } <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import files_file_manager_api
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
    api_instance = files_file_manager_api.FilesFileManagerApi(api_client)
    accept = "application/json" # str | 
    content_type = "application/json" # str | 

    # example passing only required values which don't have defaults set
    try:
        # [ /upload ] Upload file
        api_response = api_instance.__upload_uploadfile(accept, content_type)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling FilesFileManagerApi->__upload_uploadfile: %s\n" % e)
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

# **__write_writefile**
> bool, date, datetime, dict, float, int, list, str, none_type __write_writefile(accept, body)

[ /write ] Write file

Writes data to the specified file  ## Available parameters | Parameter | Description                          | |-----------|--------------------------------------| | file      | URL encoded path to the desired file |  <!-- RESPONSE 204 --> // Successful <!-- ENDRESPONSE -->

### Example

* Bearer Authentication (bearer):

```python
import time
import pterodactyl_client
from pterodactyl_client.api import files_file_manager_api
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
    api_instance = files_file_manager_api.FilesFileManagerApi(api_client)
    accept = "application/json" # str | 
    body = '''#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula).
#You also agree that tacos are tasty, and the best food in the world.
#Wed Dec 25 05:20:41 UTC 2019
eula=true
''' # str | 
    file = "/eula.txt" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # [ /write ] Write file
        api_response = api_instance.__write_writefile(accept, body)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling FilesFileManagerApi->__write_writefile: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # [ /write ] Write file
        api_response = api_instance.__write_writefile(accept, body, file=file)
        pprint(api_response)
    except pterodactyl_client.ApiException as e:
        print("Exception when calling FilesFileManagerApi->__write_writefile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  |
 **body** | **str**|  |
 **file** | **str**|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

