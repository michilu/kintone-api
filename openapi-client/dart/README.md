# openapi
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Dart package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Build package: org.openapitools.codegen.languages.DartClientCodegen
For more information, please visit [https://github.com/michilu/proto-api](https://github.com/michilu/proto-api)

## Requirements

Dart 2.0 or later

## Installation & Usage

### Github
If this Dart package is published to Github, add the following dependency to your pubspec.yaml
```
dependencies:
  openapi:
    git: https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```

### Local
To use the package in your local drive, add the following dependency to your pubspec.yaml
```
dependencies:
  openapi:
    path: /path/to/openapi
```

## Tests

TODO

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```dart
import 'package:openapi/api.dart';

// TODO Configure API key authorization: ApiKeyAuth
//defaultApiClient.getAuthentication<ApiKeyAuth>('ApiKeyAuth').apiKey = 'YOUR_API_KEY';
// uncomment below to setup prefix (e.g. Bearer) for API key, if needed
//defaultApiClient.getAuthentication<ApiKeyAuth>('ApiKeyAuth').apiKeyPrefix = 'Bearer';
// TODO Configure OAuth2 access token for authorization: OAuth2
//defaultApiClient.getAuthentication<OAuth>('OAuth2').accessToken = 'YOUR_ACCESS_TOKEN';

var api_instance = ExampleServiceApi();
var id = id_example; // String | 
var body = V1ExampleServiceQueryRequest(); // V1ExampleServiceQueryRequest | 

try {
    var result = api_instance.exampleServiceQuery(id, body);
    print(result);
} catch (e) {
    print("Exception when calling ExampleServiceApi->exampleServiceQuery: $e\n");
}

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ExampleServiceApi* | [**exampleServiceQuery**](doc//ExampleServiceApi.md#exampleservicequery) | **POST** /v1/example/{id} | 
*HealthCheckServiceApi* | [**healthCheckServiceHealthCheck**](doc//HealthCheckServiceApi.md#healthcheckservicehealthcheck) | **GET** /healthCheck | 


## Documentation For Models

 - [ProtobufAny](doc//ProtobufAny.md)
 - [Protov1Response](doc//Protov1Response.md)
 - [RpcCode](doc//RpcCode.md)
 - [RuntimeError](doc//RuntimeError.md)
 - [V1ExampleServiceQueryRequest](doc//V1ExampleServiceQueryRequest.md)
 - [V1ExampleServiceQueryResponse](doc//V1ExampleServiceQueryResponse.md)
 - [V1HealthCheckServiceHealthCheckResponse](doc//V1HealthCheckServiceHealthCheckResponse.md)


## Documentation For Authorization


## ApiKeyAuth

- **Type**: API key
- **API key parameter name**: X-API-Key
- **Location**: HTTP header

## OAuth2

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: https://example.com/oauth/authorize
- **Scopes**: 
 - **admin**: Grants read and write access to administrative information
 - **read**: Grants read access
 - **write**: Grants write access


## Author

none@example.com

