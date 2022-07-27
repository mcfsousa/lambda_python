from http import HTTPStatus
import json


def response_ok(payload):
    return response_from(HTTPStatus.OK, payload)


def response_bad_request(payload):
    return response_from(HTTPStatus.BAD_REQUEST, payload)


def response_internal_server_error(payload):
    return response_from(HTTPStatus.INTERNAL_SERVER_ERROR, payload)


def response_from(http_status, payload):
    response = {
        'message': payload
    }
    return {
        'statusCode': http_status.value,
        'body': json.dumps(response, default=str)
    }
