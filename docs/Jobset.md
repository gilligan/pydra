# Jobset

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fetcherrormsg** | **str** | contains the error message when there was a problem fetching sources for a jobset | [optional] 
**nixexprinput** | **str** | the name of the jobset input which contains the nixexprpath | [optional] 
**errormsg** | **str** | contains the stderr output of the nix-instantiate command | [optional] 
**emailoverride** | **str** | email address to send notices to instead of the package maintainer (can be a comma separated list) | [optional] 
**nixexprpath** | **str** | the path to the file to evaluate | [optional] 
**enabled** | **bool** | when set to true the jobset gets scheduled for evaluation | [optional] 
**jobsetinputs** | [**dict(str, JobsetInput)**](JobsetInput.md) | inputs configured for this jobset | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


