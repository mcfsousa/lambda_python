import json

from aws_lambda_powertools import Logger
from aws_lambda_powertools.event_handler import ApiGatewayResolver
from aws_lambda_powertools.utilities.validation import envelopes, validate
from aws_lambda_powertools.utilities.parser import parse

from . import response
from domain.invoicedata import InvoiceData
from domain.lambda_domain import process

logger = Logger(service="InvoiceUpdate")
apigateway = ApiGatewayResolver()


def update_invoice(event, context):
    try:
        logger.set_correlation_id(
            event["requestContext"]["requestId"])
        logger.info({
            "Event": event})
        input_schema = get_schema("adapters/input_schema.json")
        validate(
            event = event,
            schema=input_schema,
            envelope=envelopes.API_GATEWAY_REST)
        
    except Exception as error:       
        logger.exception("Erro de validacao dos dados")
        return response.response_bad_request(error)
        
    try:
        return_value = apigateway.resolve(event, context)
        logger.info(return_value)
        return return_value
    except Exception as error:
        logger.exception("Erro interno")
        return response.response_internal_server_error(
            "Error updating invoice"
        )


@apigateway.post("/invoice")
def process_request():
    invoice = parse(
        event=apigateway.current_event.json_body,
        model=InvoiceData)
    return process(
        logger,
        invoice
    )


def get_schema(schema_name: str) -> dict:
    with open(schema_name, 'r') as file:
        return json.load(file)
