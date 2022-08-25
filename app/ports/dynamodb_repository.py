import boto3
import aws_lambda_powertools as PowerToolsLog

dynamo_resource = None


class DynamoDBRepository:
    def __init__(self, _logger: PowerToolsLog.Logger, table_name: str):
        global dynamo_resource
        self.logger = _logger
        if dynamo_resource is None:
            dynamo_resource = boto3.resource(
                "dynamodb", region_name="sa-east-1"
            )
        self.dynamo_table = dynamo_resource.Table(table_name)

    def table(self):
        return self.dynamo_table
