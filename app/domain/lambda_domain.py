from aws_lambda_powertools import Logger
from . import invoicedata
from ports.invoice_repository import InvoiceRepository


def process(logger: Logger, invoice: invoicedata.InvoiceData) -> dict:
    total_price = round(
        invoice.invoice_unit_price * invoice.invoice_quantity,
        2
    )
    invoice_repository = InvoiceRepository(logger)
    
    invoice_repository.update_invoice(
        invoice.invoice_id,
        invoice.customer_id,
        invoice.invoice_quantity,
        invoice.invoice_unit_price,
        total_price,
        invoice.invoice_comment
    )
    
    return {
        "message": "Invoice successfully updated",
        "invoice_id": invoice.invoice_id
    }
    