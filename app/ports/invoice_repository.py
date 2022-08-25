import aws_lambda_powertools as PowerToolsLog

import ports.dynamodb_repository as Repository


class InvoiceRepository(Repository.DynamoDBRepository):
    def __init__(self, _logger: PowerToolsLog.Logger):
        Repository.DynamoDBRepository.__init__(self, _logger, "invoice")

    def update_invoice(
        self,
        invoice_id: int,
        customer_id: int,
        invoice_quantity: int,
        invoice_unit_price: float,
        invoice_total_price: float,
        invoice_comment: str,
    ):
        try:
            invoice_comment_aux = invoice_comment if invoice_comment else ""
            item = {
                "invoice_id": invoice_id,
                "customer_id": customer_id,
                "invoice_quantiyy": invoice_quantity,
                "invoice_unit_price": str(invoice_unit_price),
                "invoice_total_price": str(invoice_total_price),
                "invoice_comment": invoice_comment_aux,
            }
            result = self.table().put_item(Item=item)
            self.logger.info({"DynamoDb item updated": item, "result": result})
        except Exception as error:
            self.logger.exception({"DynamoDb item failed": item})
            raise error
