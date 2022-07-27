import boto3
from aws_lambda_powertools import Logger

dynamodbclient = boto3.client('dynamodb')


class InvoiceRepository:
    def __init__(self, logger: Logger):
        self.logger = logger
        
    def update_invoice(self,
                       invoice_id,
                       customer_id,
                       invoice_quantity,
                       invoice_unit_price,
                       invoice_total_price,
                       invoice_comment):
        try:
            invoice_comment_aux = ""
            if invoice_comment:
                invoice_comment_aux = invoice_comment
                
            item = {
                'invoice_id': {'N', str(invoice_id)},
                'customer_id': {'N', str(customer_id)},
                'invoice_quantiyy': {'N', str(invoice_quantity)},
                'invoice_unit_price': {'N', str(invoice_unit_price)},
                'invoice_total_price': {'N', str(invoice_total_price)},
                'invoice_comment': {'S', invoice_comment_aux}
            }
            dynamodbclient.put_item(TableName='invoice', Item=item)
        except Exception as error:
            self.logger.error('Error inserting invoice')
            raise error
