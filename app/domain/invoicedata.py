import aws_lambda_powertools.utilities.parser as PowerToolsParser
import typing


class InvoiceData(PowerToolsParser.BaseModel):
    invoice_id: int
    customer_id: int
    invoice_quantity: int
    invoice_unit_price: float
    invoice_comment: typing.Optional[str]
