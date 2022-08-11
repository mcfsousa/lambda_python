import json
import unittest
import boto3
import moto
import lambda_function


class InvoiceTest(unittest.TestCase):
    def create_table(self):
        table_key_schema = [{"AttributeName": "invoice_id", "KeyType": "HASH"}]
        table_attribute_definitions = [
            {"AttributeName": "invoice_id", "AttributeType": "N"}
        ]
        boto3.setup_default_session()
        client = boto3.client("dynamodb", region_name="sa-east-1")
        client.create_table(
            TableName="invoice",
            KeySchema=table_key_schema,
            AttributeDefinitions=table_attribute_definitions,
            BillingMode="PAY_PER_REQUEST",
        )

    def create_payload(self, body: dict):
        return {
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
                    "userAgent": (
                        "aws-internal/3 aws-sdk-java/1.12.239"
                        " Linux/5.4.196-119.356.amzn2int.x86_64"
                        " OpenJDK_64-Bit_Server_VM/25.332-b08 java/1.8.0_332"
                        " vendor/Oracle_Corporation cfg/retry-mode/standard"
                    ),
                    "accountId": "074512587423",
                    "caller": "AIDARCWKL3KP7SL5QLBTO",
                    "sourceIp": "test-invoke-source-ip",
                    "accessKey": "ASIARCWKL3KPT5NCPOX6",
                    "cognitoAuthenticationProvider": "null",
                    "user": "AIDARCWKL3KP7SL5QLBTO",
                },
                "domainName": "testPrefix.testDomainName",
                "apiId": "pv2x85rd3b",
            },
            "isBase64Encoded": False,
        }

    @moto.mock_dynamodb
    def test_lambda_function_success(self):
        self.create_table()

        body = {
            "invoice_id": 1,
            "customer_id": 2,
            "invoice_quantity": 10,
            "invoice_unit_price": 1.542348,
            "invoice_comment": "test",
        }
        payload = self.create_payload(body)

        response = lambda_function.lambda_handler(event=payload, context=None)
        response_success = {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": (
                '{"message":"Invoice successfully updated","invoice_id":1}'
            ),
            "isBase64Encoded": False,
        }
        assert response == response_success

    @moto.mock_dynamodb
    def test_lambda_function_invalid_payload(self):
        self.create_table()
        body = {
            "invoice_id": "1X",
            "customer_id": 2,
            "invoice_quantity": 10,
            "invoice_unit_price": 1.542348,
            "invoice_comment": "test",
        }
        payload = self.create_payload(body)
        response = lambda_function.lambda_handler(event=payload, context=None)
        bad_request = {
            "statusCode": 400,
            "body": (
                '{"message": "Failed schema validation. Error:'
                " data.invoice_id must be integer, Path: ['data',"
                " 'invoice_id'], Data: 1X\"}"
            ),
        }
        assert response == bad_request

    @moto.mock_dynamodb
    def test_lambda_function_internal_error(self):
        body = {
            "invoice_id": 1,
            "customer_id": 2,
            "invoice_quantity": 10,
            "invoice_unit_price": 1.542348,
            "invoice_comment": "test",
        }

        payload = self.create_payload(body)

        response = lambda_function.lambda_handler(event=payload, context=None)
        internal_error = {
            "statusCode": 500,
            "body": '{"message": "Error updating invoice"}',
        }
        assert response == internal_error
