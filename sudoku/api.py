import requests
import json
from . import (
    API_URL, EXAMPLE_JSON, COLUMN_OUT_OF_RANGE, ROW_OUT_OF_RANGE,
    VALUE_OUT_OF_RANGE, RESPONSE_INVALID, SIZE_INVALID, NO_SQUARES)


def mocked_requests_get(*args, **_):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

        def raise_for_status(self):
            pass

    if args[0] == API_URL:
        with open(EXAMPLE_JSON, 'r') as f:
            return MockResponse(json.load(f), 200)


def parse_api_response(response):
    result = [[' ' for i in range(9)] for j in range(9)]
    squares = response['squares']
    for square in squares:
        x = square['x']
        y = square['y']
        result[x][y] = str(square['value'])
    flat_matrix = [column for row in result for column in row]

    return ''.join(flat_matrix)


def validate_response(response):
    if response['response'] is False:
        raise Exception(RESPONSE_INVALID)

    if response['size'] != '9':
        raise Exception(SIZE_INVALID)

    if not response['squares']:
        raise Exception(NO_SQUARES)

    for square in response['squares']:
        if not 0 <= square['x'] <= 8:
            raise Exception(ROW_OUT_OF_RANGE)
        if not 0 <= square['y'] <= 8:
            raise Exception(COLUMN_OUT_OF_RANGE)
        if not 1 <= square['value'] <= 9:
            raise Exception(VALUE_OUT_OF_RANGE)


def fetch_board():
    response = requests.get(API_URL)
    response.raise_for_status()
    validate_response(response.json())
    return parse_api_response(response.json())
