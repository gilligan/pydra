# pydra
Specification of the Hydra REST API

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import hydra_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import hydra_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import hydra_client
from hydra_client.rest import ApiException
from pprint import pprint


# Defining host is optional and default to https://hydra.nixos.org
configuration.host = "https://hydra.nixos.org"
# Create an instance of the API class
api_instance = hydra_client.DefaultApi(hydra_client.ApiClient(configuration))
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

## Documentation for API Endpoints

All URIs are relative to *https://hydra.nixos.org*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**create_jobset**](docs/DefaultApi.md#create_jobset) | **PUT** /jobset/{project-id}/{jobset-id} | Creates a jobset in an existing project
*DefaultApi* | [**create_project**](docs/DefaultApi.md#create_project) | **PUT** /project/{id} | Create a project
*DefaultApi* | [**get_build**](docs/DefaultApi.md#get_build) | **GET** /build/{build-id} | Retrieves a single build of a jobset by id
*DefaultApi* | [**get_evaluation**](docs/DefaultApi.md#get_evaluation) | **GET** /eval/{build-id} | Retrieves evaluations identified by build id
*DefaultApi* | [**get_job_sets**](docs/DefaultApi.md#get_job_sets) | **GET** /api/jobsets | retrieve a jobset overview for a project
*DefaultApi* | [**get_jobset**](docs/DefaultApi.md#get_jobset) | **GET** /jobset/{project-id}/{jobset-id} | Retrieves a jobset designated by project and jobset id
*DefaultApi* | [**get_jobset_evals**](docs/DefaultApi.md#get_jobset_evals) | **GET** /jobset/{project-id}/{jobset-id}/evals | Retrieves all evaluations of a jobset
*DefaultApi* | [**get_project**](docs/DefaultApi.md#get_project) | **GET** /project/{id} | Retrieves a project designated by name
*DefaultApi* | [**get_projects**](docs/DefaultApi.md#get_projects) | **GET** / | Retrieves all projects
*DefaultApi* | [**login**](docs/DefaultApi.md#login) | **POST** /login | Log in using username/password credentials
*DefaultApi* | [**search**](docs/DefaultApi.md#search) | **GET** /search | search for evaluations
*DefaultApi* | [**trigger_job_set**](docs/DefaultApi.md#trigger_job_set) | **PUT** /api/push | trigger jobsets


## Documentation For Models

 - [Build](docs/Build.md)
 - [BuildBuildmetrics](docs/BuildBuildmetrics.md)
 - [BuildOutput](docs/BuildOutput.md)
 - [BuildProduct](docs/BuildProduct.md)
 - [Error](docs/Error.md)
 - [Evaluations](docs/Evaluations.md)
 - [InlineObject](docs/InlineObject.md)
 - [InlineObject1](docs/InlineObject1.md)
 - [InlineObject2](docs/InlineObject2.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse201](docs/InlineResponse201.md)
 - [InlineResponse2011](docs/InlineResponse2011.md)
 - [InlineResponse500](docs/InlineResponse500.md)
 - [Jobset](docs/Jobset.md)
 - [JobsetEval](docs/JobsetEval.md)
 - [JobsetEvalInput](docs/JobsetEvalInput.md)
 - [JobsetInput](docs/JobsetInput.md)
 - [Project](docs/Project.md)
 - [SearchResult](docs/SearchResult.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author




