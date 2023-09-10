# nordpool_client.AuctionsApi

All URIs are relative to *http://{{ssourl}}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auctions_auction_id_external_get**](AuctionsApi.md#auctions_auction_id_external_get) | **GET** /auctions/{auctionIdExternal} | Auctions Contracts
[**auctions_auction_id_external_orders_get**](AuctionsApi.md#auctions_auction_id_external_orders_get) | **GET** /auctions/{auctionIdExternal}/orders | Auctions Orders
[**auctions_auction_id_external_portfoliovolumes_get**](AuctionsApi.md#auctions_auction_id_external_portfoliovolumes_get) | **GET** /auctions/{auctionIdExternal}/portfoliovolumes | Auctions Portfolio Volumes
[**auctions_auction_id_external_prices_get**](AuctionsApi.md#auctions_auction_id_external_prices_get) | **GET** /auctions/{auctionIdExternal}/prices | Auctions Prices
[**auctions_auction_id_external_trades_get**](AuctionsApi.md#auctions_auction_id_external_trades_get) | **GET** /auctions/{auctionIdExternal}/trades | Auctions Trades
[**auctions_get**](AuctionsApi.md#auctions_get) | **GET** /auctions | Auctions by closeBidding
[**blockorders_order_id_get**](AuctionsApi.md#blockorders_order_id_get) | **GET** /blockorders/{orderId} | BlockOrder by Id
[**blockorders_order_id_patch**](AuctionsApi.md#blockorders_order_id_patch) | **PATCH** /blockorders/{orderId} | BlockOrder modify
[**blockorders_post**](AuctionsApi.md#blockorders_post) | **POST** /blockorders | BlockOrder submit
[**connect_token_post**](AuctionsApi.md#connect_token_post) | **POST** /connect/token | Token auction
[**curveorders_order_id_get**](AuctionsApi.md#curveorders_order_id_get) | **GET** /curveorders/{orderId} | CurveOrder By Id
[**curveorders_order_id_patch**](AuctionsApi.md#curveorders_order_id_patch) | **PATCH** /curveorders/{orderId} | CurveOrder modify
[**curveorders_post**](AuctionsApi.md#curveorders_post) | **POST** /curveorders | CurveOrder submit

# **auctions_auction_id_external_get**
> auctions_auction_id_external_get(auction_id_external)

Auctions Contracts

### Example
```python
from __future__ import print_function
import time
import nordpool_client
from nordpool_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = nordpool_client.AuctionsApi()
auction_id_external = 'auction_id_external_example' # str | 

try:
    # Auctions Contracts
    api_instance.auctions_auction_id_external_get(auction_id_external)
except ApiException as e:
    print("Exception when calling AuctionsApi->auctions_auction_id_external_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auction_id_external** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auctions_auction_id_external_orders_get**
> auctions_auction_id_external_orders_get(auction_id_external)

Auctions Orders

### Example
```python
from __future__ import print_function
import time
import nordpool_client
from nordpool_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = nordpool_client.AuctionsApi()
auction_id_external = 'auction_id_external_example' # str | 

try:
    # Auctions Orders
    api_instance.auctions_auction_id_external_orders_get(auction_id_external)
except ApiException as e:
    print("Exception when calling AuctionsApi->auctions_auction_id_external_orders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auction_id_external** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auctions_auction_id_external_portfoliovolumes_get**
> auctions_auction_id_external_portfoliovolumes_get(auction_id_external)

Auctions Portfolio Volumes

### Example
```python
from __future__ import print_function
import time
import nordpool_client
from nordpool_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = nordpool_client.AuctionsApi()
auction_id_external = 'auction_id_external_example' # str | 

try:
    # Auctions Portfolio Volumes
    api_instance.auctions_auction_id_external_portfoliovolumes_get(auction_id_external)
except ApiException as e:
    print("Exception when calling AuctionsApi->auctions_auction_id_external_portfoliovolumes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auction_id_external** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auctions_auction_id_external_prices_get**
> auctions_auction_id_external_prices_get(auction_id_external)

Auctions Prices

### Example
```python
from __future__ import print_function
import time
import nordpool_client
from nordpool_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = nordpool_client.AuctionsApi()
auction_id_external = 'auction_id_external_example' # str | 

try:
    # Auctions Prices
    api_instance.auctions_auction_id_external_prices_get(auction_id_external)
except ApiException as e:
    print("Exception when calling AuctionsApi->auctions_auction_id_external_prices_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auction_id_external** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auctions_auction_id_external_trades_get**
> auctions_auction_id_external_trades_get(auction_id_external)

Auctions Trades

### Example
```python
from __future__ import print_function
import time
import nordpool_client
from nordpool_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = nordpool_client.AuctionsApi()
auction_id_external = 'auction_id_external_example' # str | 

try:
    # Auctions Trades
    api_instance.auctions_auction_id_external_trades_get(auction_id_external)
except ApiException as e:
    print("Exception when calling AuctionsApi->auctions_auction_id_external_trades_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auction_id_external** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auctions_get**
> auctions_get(accept=accept, close_bidding_from=close_bidding_from, close_bidding_to=close_bidding_to)

Auctions by closeBidding

### Example
```python
from __future__ import print_function
import time
import nordpool_client
from nordpool_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = nordpool_client.AuctionsApi()
accept = 'accept_example' # str |  (optional)
close_bidding_from = 'close_bidding_from_example' # str |  (optional)
close_bidding_to = 'close_bidding_to_example' # str |  (optional)

try:
    # Auctions by closeBidding
    api_instance.auctions_get(accept=accept, close_bidding_from=close_bidding_from, close_bidding_to=close_bidding_to)
except ApiException as e:
    print("Exception when calling AuctionsApi->auctions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  | [optional] 
 **close_bidding_from** | **str**|  | [optional] 
 **close_bidding_to** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **blockorders_order_id_get**
> blockorders_order_id_get(order_id)

BlockOrder by Id

### Example
```python
from __future__ import print_function
import time
import nordpool_client
from nordpool_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = nordpool_client.AuctionsApi()
order_id = 'order_id_example' # str | 

try:
    # BlockOrder by Id
    api_instance.blockorders_order_id_get(order_id)
except ApiException as e:
    print("Exception when calling AuctionsApi->blockorders_order_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **blockorders_order_id_patch**
> blockorders_order_id_patch(order_id, body=body)

BlockOrder modify

### Example
```python
from __future__ import print_function
import time
import nordpool_client
from nordpool_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = nordpool_client.AuctionsApi()
order_id = 'order_id_example' # str | 
body = nordpool_client.BlockordersOrderIdBody() # BlockordersOrderIdBody |  (optional)

try:
    # BlockOrder modify
    api_instance.blockorders_order_id_patch(order_id, body=body)
except ApiException as e:
    print("Exception when calling AuctionsApi->blockorders_order_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**|  | 
 **body** | [**BlockordersOrderIdBody**](BlockordersOrderIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **blockorders_post**
> blockorders_post(body=body, content_type=content_type)

BlockOrder submit

### Example
```python
from __future__ import print_function
import time
import nordpool_client
from nordpool_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = nordpool_client.AuctionsApi()
body = nordpool_client.BlockordersBody() # BlockordersBody |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # BlockOrder submit
    api_instance.blockorders_post(body=body, content_type=content_type)
except ApiException as e:
    print("Exception when calling AuctionsApi->blockorders_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BlockordersBody**](BlockordersBody.md)|  | [optional] 
 **content_type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connect_token_post**
> connect_token_post(grant_type=grant_type, scope=scope, username=username, password=password, authorization=authorization, content_type=content_type)

Token auction

### Example
```python
from __future__ import print_function
import time
import nordpool_client
from nordpool_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = nordpool_client.AuctionsApi()
grant_type = 'grant_type_example' # str |  (optional)
scope = 'scope_example' # str |  (optional)
username = 'username_example' # str |  (optional)
password = 'password_example' # str |  (optional)
authorization = 'authorization_example' # str |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # Token auction
    api_instance.connect_token_post(grant_type=grant_type, scope=scope, username=username, password=password, authorization=authorization, content_type=content_type)
except ApiException as e:
    print("Exception when calling AuctionsApi->connect_token_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**|  | [optional] 
 **scope** | **str**|  | [optional] 
 **username** | **str**|  | [optional] 
 **password** | **str**|  | [optional] 
 **authorization** | **str**|  | [optional] 
 **content_type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **curveorders_order_id_get**
> curveorders_order_id_get(order_id)

CurveOrder By Id

### Example
```python
from __future__ import print_function
import time
import nordpool_client
from nordpool_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = nordpool_client.AuctionsApi()
order_id = 'order_id_example' # str | 

try:
    # CurveOrder By Id
    api_instance.curveorders_order_id_get(order_id)
except ApiException as e:
    print("Exception when calling AuctionsApi->curveorders_order_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **curveorders_order_id_patch**
> curveorders_order_id_patch(order_id, body=body)

CurveOrder modify

### Example
```python
from __future__ import print_function
import time
import nordpool_client
from nordpool_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = nordpool_client.AuctionsApi()
order_id = 'order_id_example' # str | 
body = nordpool_client.CurveordersOrderIdBody() # CurveordersOrderIdBody |  (optional)

try:
    # CurveOrder modify
    api_instance.curveorders_order_id_patch(order_id, body=body)
except ApiException as e:
    print("Exception when calling AuctionsApi->curveorders_order_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**|  | 
 **body** | [**CurveordersOrderIdBody**](CurveordersOrderIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **curveorders_post**
> curveorders_post(body=body, content_type=content_type)

CurveOrder submit

### Example
```python
from __future__ import print_function
import time
import nordpool_client
from nordpool_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = nordpool_client.AuctionsApi()
body = nordpool_client.CurveordersBody() # CurveordersBody |  (optional)
content_type = 'content_type_example' # str |  (optional)

try:
    # CurveOrder submit
    api_instance.curveorders_post(body=body, content_type=content_type)
except ApiException as e:
    print("Exception when calling AuctionsApi->curveorders_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CurveordersBody**](CurveordersBody.md)|  | [optional] 
 **content_type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

