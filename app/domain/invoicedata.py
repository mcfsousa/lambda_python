from aws_lambda_powertools.utilities.parser import BaseModel
from typing import Optional


class InvoiceData(BaseModel):
    invoice_id: int
    customer_id: int
    invoice_quantity: int
    invoice_unit_price: float
    invoice_comment: Optional[str]