import boto3
from aws_lambda_powertools import Logger

dynamodbclient = boto3.client('dynamodb')


class InvoiceRepository:
    def __init__(self, _logger: Logger):
        self.logger = _logger
        
    def update_invoice(self,
                       invoice_id: int,
                       customer_id: int,
                       invoice_quantity: int,
                       invoice_unit_price: float,
                       invoice_total_price: float,
                       invoice_comment: str):
        try:
            invoice_comment_aux = invoice_comment if invoice_comment else "" 
            item = {
                'invoice_id': {'N', str(invoice_id)},
                'customer_id': {'N', str(customer_id)},
                'invoice_quantiyy': {'N', str(invoice_quantity)},
                'invoice_unit_price': {'N', str(invoice_unit_price)},
                'invoice_total_price': {'N', str(invoice_total_price)},
                'invoice_comment': {'S', invoice_comment_aux}
            }
            result = dynamodbclient.put_item(TableName='invoice', Item=item)
            self.logger.info({
                "DynamoDb item updated": item,
                "result": result})
        except Exception as error:
            self.logger.error({
                "DynamoDb item failed": item})
            raise error
