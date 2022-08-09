from http import HTTPStatus
import json


def response_ok(payload: str) -> dict:
    return response_from(HTTPStatus.OK, payload)


def response_bad_request(payload: str) -> dict:
    return response_from(HTTPStatus.BAD_REQUEST, payload)


def response_internal_server_error(payload: str) -> dict:
    return response_from(HTTPStatus.INTERNAL_SERVER_ERROR, payload)


def response_from(http_status: tuple, payload: str) -> dict:
    message = {
        'message': payload
    }
    response = {
        'statusCode': http_status.value,
        'body': json.dumps(message, default=str)
    }
    return response
