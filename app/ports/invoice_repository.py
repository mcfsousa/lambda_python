import boto3
from aws_lambda_powertools import Logger

dynamo_resource = None


class InvoiceRepository:
    def __init__(self, _logger: Logger):
        global dynamo_resource
        self.logger = _logger
        if dynamo_resource is None:
            dynamo_resource = boto3.resource("dynamodb", region_name="sa-east-1")
        self.dynamo_table = dynamo_resource.Table("invoice")
        
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
                'invoice_id': invoice_id,
                'customer_id': customer_id,
                'invoice_quantiyy': invoice_quantity,
                'invoice_unit_price': str(invoice_unit_price),
                'invoice_total_price': str(invoice_total_price),
                'invoice_comment': invoice_comment_aux
            }
            result = self.dynamo_table.put_item(Item=item)
            self.logger.info({
                "DynamoDb item updated": item,
                "result": result})
        except Exception as error:
            self.logger.exception({
                "DynamoDb item failed": item})
            raise error
