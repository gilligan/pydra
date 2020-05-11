# InlineObject2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | a description of the jobset | [optional] 
**checkinterval** | **int** | interval (in seconds) in which to check for evaluation | [optional] 
**enabled** | **bool** | when true the jobset gets scheduled for evaluation | [optional] 
**visible** | **bool** | when true the jobset is visible in the web frontend | [optional] 
**keepnr** | **int** | number or evaluations to keep | [optional] 
**nixexprinput** | **str** | the name of the jobset input which contains the nixexprpath | [optional] 
**nixexprpath** | **str** | the path to the file to evaluate | [optional] 
**inputs** | [**dict(str, JobsetInput)**](JobsetInput.md) | inputs for this jobset | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


