from aws_lambda_powertools import Tracer
from adapters import api_handler

tracer = Tracer()


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    return api_handler.update_invoice(event, context)
