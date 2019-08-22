import unittest
import json
from parameterized import parameterized
from requests.exceptions import RequestException
import sudoku
from .. import (
    API_BOARD, API_URL, EXAMPLE_JSON, COLUMN_OUT_OF_RANGE, ROW_OUT_OF_RANGE,
    VALUE_OUT_OF_RANGE, RESPONSE_INVALID, SIZE_INVALID, NO_SQUARES)
from ..api import (
    fetch_board, parse_api_response, mocked_requests_get, validate_response)


class TestSudokuApi(unittest.TestCase):

    def test_parse_api_response(self):
        response = None
        with open(EXAMPLE_JSON, 'r') as f:
            response = json.load(f)
        parsed = parse_api_response(response)
        expected = API_BOARD
        self.assertEqual(parsed, expected)

    @unittest.mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_fetch_board(self, mocked_request):
        response = fetch_board()
        mocked_request.assert_called_with(API_URL)
        self.assertEqual(response, API_BOARD)

    @parameterized.expand([
        ('{"response": false}', RESPONSE_INVALID),
        ('{"response": true, "size": "7"}', SIZE_INVALID),
        ('{"response": true, "size": "9", "squares":[] }', NO_SQUARES),
        ('{"response": true, "size": "9", '
            '"squares":[{"x":9,"y":3,"value":7}]}', ROW_OUT_OF_RANGE),
        ('{"response": true, "size": "9", '
            '"squares":[{"x":3,"y":9,"value":7}]}', COLUMN_OUT_OF_RANGE),
        ('{"response": true, "size": "9",'
            '"squares":[{"x":3,"y":3,"value":10}]}', VALUE_OUT_OF_RANGE)
    ])
    def test_incorrect_response(self, response, message):
        with self.assertRaises(Exception) as e:
            validate_response(json.loads(response))
        self.assertEqual(str(e.exception), message)

    def test_correct_strucutre(self):
        try:
            fetch_board()
        except Exception as e:
            self.fail('Incorrect structure: ' + str(e))

    def test_404_api_connection(self):
        original_URL = sudoku.api.API_URL
        sudoku.api.API_URL = 'http://www.cs.utep.edu/cheon/ws/UNO/new/'
        with self.assertRaises(RequestException):
            fetch_board()
        sudoku.api.API_URL = original_URL
