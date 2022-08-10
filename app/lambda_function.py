import aws_lambda_powertools as PowerToolsTrace
import adapters.input_handler as Adapter

tracer = PowerToolsTrace.Tracer()


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    return Adapter.update_invoice(event, context)
