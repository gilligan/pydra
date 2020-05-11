# BuildBuildmetrics

user defined build metrics from `$out/nix-support/hydra-metrics`. The file should define metrics separated by new lines using the following format:  ``` <name> <value>[ <unit>] ``` The name and unit fields are strings, the value is a float. The unit is optional. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of the measured build metric | [optional] 
**value** | **str** | measured value | [optional] 
**unit** | **str** | unit of the measured build metric | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


