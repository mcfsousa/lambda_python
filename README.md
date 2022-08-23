# lambda_python
Lambda python


This repository contains the code that implements a AWS Lambda in Python as ilustrated in the picture bellow:
![Lambda](./images/lambda_gateway.png)


It ilustrates some practices that should be considered when developing an AWS Lambda, such as:
1. Choosing an architectural pattern
2. Defining how to implement desirable features like log, trace, validation, exception handling, etc

A sample of the payload received by the AWS Lambda can be found in the [testfile](./app/tests//test_lambda_function.py). It's an API Gateway payload.

The API Gateway payload must contain, in the body property, a json with some specific fields as described in the [jsonschema](./app/adapters/input_schema.json).

The DynamoDb table expected to exist in order for the sample works can also be found in the [testfile](./app/tests//test_lambda_function.py).

The librarys needed to execute can be found at the [requirements.txt](./app/requirements.txt) file.

It uses code style [Black](https://medium.com/ki-labs-engineering/any-code-style-you-like-as-long-its-black-7a3cc4edd90).
