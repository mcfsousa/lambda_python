import http
import json


def bad_request(payload: str) -> dict:
    return response_from(http.HTTPStatus.BAD_REQUEST, payload)


def internal_server_error(payload: str) -> dict:
    return response_from(http.HTTPStatus.INTERNAL_SERVER_ERROR, payload)


def response_from(http_status: tuple, payload: str) -> dict:
    message = {"message": payload}
    response = {
        "statusCode": http_status.value,
        "body": json.dumps(message, default=str),
    }
    return response
