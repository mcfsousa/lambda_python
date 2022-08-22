import json
import cachetools.func

import aws_lambda_powertools as PowerToolsLog
import aws_lambda_powertools.event_handler as PowerToolsEvent
import aws_lambda_powertools.utilities.validation as PowerToolsValidation
import aws_lambda_powertools.utilities.validation.envelopes as Envelopes
import aws_lambda_powertools.utilities.parser as PowerToolsParse

import adapters.response as Response
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
            envelope=Envelopes.API_GATEWAY_REST,
        )

    except Exception as error:
        logger.exception("Erro de validacao dos dados")
        return Response.bad_request(error)

    try:
        return_value = apigateway.resolve(event, context)
        logger.info(return_value)
        return return_value
    except Exception:
        logger.exception("Erro interno")
        return Response.internal_server_error("Error updating invoice")


@apigateway.post("/invoice")
def process_request():
    invoice = PowerToolsParse.parse(
        event=apigateway.current_event.json_body, model=DomainTypes.InvoiceData
    )
    return DomainRules.process(logger, invoice)


@cachetools.func.ttl_cache(maxsize=10240, ttl=3600)
def get_schema(schema_name: str) -> dict:
    with open(schema_name, "r") as file:
        return json.load(file)
