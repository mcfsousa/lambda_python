import aws_lambda_powertools as PowerToolsLog
from . import invoicedata as DomainTypes
import ports.invoice_repository as Repository


def process(logger: PowerToolsLog.Logger, invoice: DomainTypes.InvoiceData) -> dict:
    total_price = round(invoice.invoice_unit_price * invoice.invoice_quantity, 2)
    invoice_repository = Repository.InvoiceRepository(logger)

    invoice_repository.update_invoice(
        invoice.invoice_id,
        invoice.customer_id,
        invoice.invoice_quantity,
        invoice.invoice_unit_price,
        total_price,
        invoice.invoice_comment,
    )

    return {"message": "Invoice successfully updated", "invoice_id": invoice.invoice_id}
