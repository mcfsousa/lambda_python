import json
from aws_lambda_powertools import Tracer
from adapters import api_handler

tracer = Tracer()


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    return api_handler.update_invoice(event, context)


body = {
    "invoice_id": 1,
    "customer_id": 2,
    "invoice_quantity": 10,
    "invoice_unit_price": 1.542348,
    "invoice_comment": "test"
}
event = {
  "body": json.dumps(body),
  "resource": "/invoice",
  "path": "/invoice",
  "httpMethod": "POST",
  "headers": {},
  "multiValueHeaders": {},
  "queryStringParameters": {},
  "multiValueQueryStringParameters": {},
  "pathParameters": {},
  "stageVariables": {},
  "requestContext": {
    "resourceId": "43svgo",
    "resourcePath": "/invoice",
    "operationName": "CreatePet",
    "httpMethod": "POST",
    "extendedRequestId": "V7cHmHvmmjQFQvw=",
    "requestTime": "27/Jul/2022:13:41:42 +0000",
    "path": "/test/invoice",
    "accountId": "074512587423",
    "protocol": "HTTP/1.1",
    "stage": "test",
    "domainPrefix": "testPrefix",
    "requestTimeEpoch": 1658929302876,
    "requestId": "f3a3c25a-f244-44ab-8f54-27e28e261ed9",
    "identity": {
      "cognitoIdentityPoolId": "null",
      "cognitoIdentityId": "null",
      "apiKey": "test-invoke-api-key",
      "principalOrgId": "null",
      "cognitoAuthenticationType": "null",
      "userArn": "arn:aws:iam::074512587423:user/Milton",
      "apiKeyId": "test-invoke-api-key-id",
      "userAgent": "aws-internal/3 aws-sdk-java/1.12.239 Linux/5.4.196-119.356.amzn2int.x86_64 OpenJDK_64-Bit_Server_VM/25.332-b08 java/1.8.0_332 vendor/Oracle_Corporation cfg/retry-mode/standard",
      "accountId": "074512587423",
      "caller": "AIDARCWKL3KP7SL5QLBTO",
      "sourceIp": "test-invoke-source-ip",
      "accessKey": "ASIARCWKL3KPT5NCPOX6",
      "cognitoAuthenticationProvider": "null",
      "user": "AIDARCWKL3KP7SL5QLBTO"
    },
    "domainName": "testPrefix.testDomainName",
    "apiId": "pv2x85rd3b"
  },
  "isBase64Encoded": False
}

lambda_handler(event = event,context=None)