# Build

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**starttime** | **int** | time when build started | [optional] 
**stoptime** | **int** | time when build ended | [optional] 
**timestamp** | **int** | time when the build was first created | [optional] 
**jobsetevals** | **list[int]** | list of evaluations this build is part of | [optional] 
**finished** | **bool** | true when the build is finished | [optional] 
**nixname** | **str** | name from the build&#39;s derivation | [optional] 
**buildstatus** | **int** | Indicates the build status:&lt;/br&gt; &lt;ul&gt;  &lt;li&gt;0 : succeeded&lt;/li&gt;  &lt;li&gt;1 : failed&lt;/li&gt;  &lt;li&gt;2 : dependency failed&lt;/li&gt;  &lt;li&gt;3 : aborted&lt;/li&gt;  &lt;li&gt;4 : canceled by the user&lt;/li&gt;  &lt;li&gt;6 : failed with output&lt;/li&gt;  &lt;li&gt;7 : timed out&lt;/li&gt;  &lt;li&gt;9 : aborted&lt;/li&gt;  &lt;li&gt;10 : log size limit exceeded&lt;/li&gt;  &lt;li&gt;11 : output size limit exceeded&lt;/li&gt;  &lt;li&gt;*  : failed&lt;/li&gt; &lt;/ul&gt; &lt;strong&gt;Note:&lt;/strong&gt;buildstatus should only be &#x60;null&#x60; if &#x60;finished&#x60; is false.  | [optional] 
**jobset** | **str** | jobset this build belongs to | [optional] 
**priority** | **int** | determines the priority with which this build will be executed (higher value means higher priority) | [optional] 
**job** | **str** | nix attribute from the nixexprpath | [optional] 
**drvpath** | **str** | filename of the drv | [optional] 
**system** | **str** | system this build was done for | [optional] 
**project** | **str** | project this build belongs to | [optional] 
**buildproducts** | [**dict(str, BuildProduct)**](BuildProduct.md) |  | [optional] 
**buildoutputs** | [**dict(str, BuildOutput)**](BuildOutput.md) |  | [optional] 
**buildmetrics** | [**BuildBuildmetrics**](BuildBuildmetrics.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


