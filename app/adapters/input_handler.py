import json

import aws_lambda_powertools as PowerToolsLog
import aws_lambda_powertools.event_handler as PowerToolsEvent
import aws_lambda_powertools.utilities.validation as PowerToolsValidation
import aws_lambda_powertools.utilities.validation.envelopes as PowerToolsValidationEnvelope
import aws_lambda_powertools.utilities.parser as PowerToolsParse

from . import response
import domain.invoicedata as DomainTypes
import domain.lambda_domain as DomainRules

logger = PowerToolsLog.Logger(service="InvoiceUpdate")
apigateway = PowerToolsEvent.ApiGatewayResolver()


def update_invoice(event, context):
    try:
        logger.set_correlation_id(event["requestContext"]["requestId"])
        logger.info({"Event": event})
        input_schema = get_schema("adapters/input_schema.json")
        PowerToolsValidation.validate(
            event=event,
            schema=input_schema,
            envelope=PowerToolsValidationEnvelope.API_GATEWAY_REST,
        )

    except Exception as error:
        logger.exception("Erro de validacao dos dados")
        return response.response_bad_request(error)

    try:
        return_value = apigateway.resolve(event, context)
        logger.info(return_value)
        return return_value
    except Exception as error:
        logger.exception("Erro interno")
        return response.response_internal_server_error("Error updating invoice")


@apigateway.post("/invoice")
def process_request():
    invoice = PowerToolsParse.parse(
        event=apigateway.current_event.json_body, model=DomainTypes.InvoiceData
    )
    return DomainRules.process(logger, invoice)


def get_schema(schema_name: str) -> dict:
    with open(schema_name, "r") as file:
        return json.load(file)
