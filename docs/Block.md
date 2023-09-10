# Block

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Block name (40 characters max) | 
**price** | **float** | Block price in currency assigned to order portfolio. | 
**minimum_acceptance_ratio** | **float** | Minimum acceptance ratio allows to define lowest possible acceptance degree. Valid values are 0 and up to 1, where 0 means fully curtailable and 1 means not curtailable. | 
**linked_to** | **str** | Name of the block this block is linked to. Is NULL for regular or parent block. | [optional] 
**is_spread_block** | **bool** | Specify if current block is one of Spread blocks pair. Only required for spread block. Requires field \&quot;linkedTo\&quot; to contain name of another spread block in pair. | [optional] 
**exclusive_group** | **str** | Name of Exclusive Ggroup this block belongs to. Equal to NULL if doesn&#x27;t belong to any Exclusive Group. | [optional] 
**periods** | [**list[Period]**](Period.md) | List of block periods. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

