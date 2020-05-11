# hydra_client.DefaultApi

All URIs are relative to *https://hydra.nixos.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_jobset**](DefaultApi.md#create_jobset) | **PUT** /jobset/{project-id}/{jobset-id} | Creates a jobset in an existing project
[**create_project**](DefaultApi.md#create_project) | **PUT** /project/{id} | Create a project
[**get_build**](DefaultApi.md#get_build) | **GET** /build/{build-id} | Retrieves a single build of a jobset by id
[**get_evaluation**](DefaultApi.md#get_evaluation) | **GET** /eval/{build-id} | Retrieves evaluations identified by build id
[**get_job_sets**](DefaultApi.md#get_job_sets) | **GET** /api/jobsets | retrieve a jobset overview for a project
[**get_jobset**](DefaultApi.md#get_jobset) | **GET** /jobset/{project-id}/{jobset-id} | Retrieves a jobset designated by project and jobset id
[**get_jobset_evals**](DefaultApi.md#get_jobset_evals) | **GET** /jobset/{project-id}/{jobset-id}/evals | Retrieves all evaluations of a jobset
[**get_project**](DefaultApi.md#get_project) | **GET** /project/{id} | Retrieves a project designated by name
[**get_projects**](DefaultApi.md#get_projects) | **GET** / | Retrieves all projects
[**login**](DefaultApi.md#login) | **POST** /login | Log in using username/password credentials
[**search**](DefaultApi.md#search) | **GET** /search | search for evaluations
[**trigger_job_set**](DefaultApi.md#trigger_job_set) | **PUT** /api/push | trigger jobsets


# **create_jobset**
> InlineResponse2003 create_jobset(project_id, jobset_id, inline_object2)

Creates a jobset in an existing project

### Example

```python
from __future__ import print_function
import time
import hydra_client
from hydra_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = hydra_client.DefaultApi()
project_id = 'project_id_example' # str | name of the project to create the jobset in
jobset_id = 'jobset_id_example' # str | name of the jobset to create
inline_object2 = hydra_client.InlineObject2() # InlineObject2 | 

try:
    # Creates a jobset in an existing project
    api_response = api_instance.create_jobset(project_id, jobset_id, inline_object2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_jobset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| name of the project to create the jobset in | 
 **jobset_id** | **str**| name of the jobset to create | 
 **inline_object2** | [**InlineObject2**](InlineObject2.md)|  | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | jobset creation response |  -  |
**200** | jobset creation response when jobset exists already |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project**
> InlineResponse2002 create_project(id, inline_object1)

Create a project

### Example

```python
from __future__ import print_function
import time
import hydra_client
from hydra_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = hydra_client.DefaultApi()
id = 'id_example' # str | project identifier
inline_object1 = hydra_client.InlineObject1() # InlineObject1 | 

try:
    # Create a project
    api_response = api_instance.create_project(id, inline_object1)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| project identifier | 
 **inline_object1** | [**InlineObject1**](InlineObject1.md)|  | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | request unauthorized |  -  |
**200** | projects exists |  -  |
**201** | successful project creation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_build**
> Build get_build(build_id)

Retrieves a single build of a jobset by id

### Example

```python
from __future__ import print_function
import time
import hydra_client
from hydra_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = hydra_client.DefaultApi()
build_id = 56 # int | build identifier

try:
    # Retrieves a single build of a jobset by id
    api_response = api_instance.get_build(build_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_id** | **int**| build identifier | 

### Return type

[**Build**](Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | build |  -  |
**404** | build couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_evaluation**
> JobsetEval get_evaluation(build_id)

Retrieves evaluations identified by build id

### Example

```python
from __future__ import print_function
import time
import hydra_client
from hydra_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = hydra_client.DefaultApi()
build_id = 56 # int | build identifier

try:
    # Retrieves evaluations identified by build id
    api_response = api_instance.get_evaluation(build_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_evaluation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **build_id** | **int**| build identifier | 

### Return type

[**JobsetEval**](JobsetEval.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | evaluation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_sets**
> list[object] get_job_sets(project=project)

retrieve a jobset overview for a project

### Example

```python
from __future__ import print_function
import time
import hydra_client
from hydra_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = hydra_client.DefaultApi()
project = 'project_example' # str | name of the project (optional)

try:
    # retrieve a jobset overview for a project
    api_response = api_instance.get_job_sets(project=project)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_job_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| name of the project | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | jobset overview |  -  |
**404** | project could not be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jobset**
> Jobset get_jobset(project_id, jobset_id)

Retrieves a jobset designated by project and jobset id

### Example

```python
from __future__ import print_function
import time
import hydra_client
from hydra_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = hydra_client.DefaultApi()
project_id = 'project_id_example' # str | name of the project the jobset belongs to
jobset_id = 'jobset_id_example' # str | name of the jobset to retrieve

try:
    # Retrieves a jobset designated by project and jobset id
    api_response = api_instance.get_jobset(project_id, jobset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_jobset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| name of the project the jobset belongs to | 
 **jobset_id** | **str**| name of the jobset to retrieve | 

### Return type

[**Jobset**](Jobset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | jobset response |  -  |
**404** | jobset couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jobset_evals**
> list[Evaluations] get_jobset_evals(project_id, jobset_id)

Retrieves all evaluations of a jobset

### Example

```python
from __future__ import print_function
import time
import hydra_client
from hydra_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = hydra_client.DefaultApi()
project_id = 'project_id_example' # str | project identifier
jobset_id = 'jobset_id_example' # str | jobset identifier

try:
    # Retrieves all evaluations of a jobset
    api_response = api_instance.get_jobset_evals(project_id, jobset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_jobset_evals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| project identifier | 
 **jobset_id** | **str**| jobset identifier | 

### Return type

[**list[Evaluations]**](Evaluations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | evaluations |  -  |
**404** | jobset couldn&#39;t be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> Project get_project(id)

Retrieves a project designated by name

### Example

```python
from __future__ import print_function
import time
import hydra_client
from hydra_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = hydra_client.DefaultApi()
id = 'id_example' # str | project identifier

try:
    # Retrieves a project designated by name
    api_response = api_instance.get_project(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| project identifier | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | project response |  -  |
**404** | project could not be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects**
> list[Project] get_projects()

Retrieves all projects

Retrieves a list of all projects.

### Example

```python
from __future__ import print_function
import time
import hydra_client
from hydra_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = hydra_client.DefaultApi()

try:
    # Retrieves all projects
    api_response = api_instance.get_projects()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_projects: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Project]**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all configured projects |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> InlineResponse200 login(inline_object)

Log in using username/password credentials

### Example

```python
from __future__ import print_function
import time
import hydra_client
from hydra_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = hydra_client.DefaultApi()
inline_object = hydra_client.InlineObject() # InlineObject | 

try:
    # Log in using username/password credentials
    api_response = api_instance.login(inline_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object** | [**InlineObject**](InlineObject.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful login |  -  |
**403** | login failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> SearchResult search(query=query)

search for evaluations

search for evaluations by name

### Example

```python
from __future__ import print_function
import time
import hydra_client
from hydra_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = hydra_client.DefaultApi()
query = 'query_example' # str | string to search for (optional)

try:
    # search for evaluations
    api_response = api_instance.search(query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| string to search for | [optional] 

### Return type

[**SearchResult**](SearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | search response |  -  |
**500** | Empty search term or other internal error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_job_set**
> InlineResponse2001 trigger_job_set(jobsets=jobsets)

trigger jobsets

### Example

```python
from __future__ import print_function
import time
import hydra_client
from hydra_client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = hydra_client.DefaultApi()
jobsets = 'jobsets_example' # str | project and jobset formatted as \"<project>:<jobset>\" to evaluate (optional)

try:
    # trigger jobsets
    api_response = api_instance.trigger_job_set(jobsets=jobsets)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->trigger_job_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobsets** | **str**| project and jobset formatted as \&quot;&lt;project&gt;:&lt;jobset&gt;\&quot; to evaluate | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | jobset trigger response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

