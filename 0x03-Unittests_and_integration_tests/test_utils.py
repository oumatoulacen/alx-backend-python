#!/usr/bin/env python3
''' This module contains the unit tests for the utils module. '''
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized, param
from utils import *


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
        ({"a": {"b": 2}}, ("a", "c")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


# patch here is simulating the behavior of the requests.get function in the
# get_json function and represents the response object that the requests.get
# function returns as mock_requests_get
class TestGetJson(unittest.TestCase):

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_requests_get):
        '''Set up the mock response'''
        mock_response = Mock()
        responce_dict = test_payload
        mock_response.json.return_value = responce_dict
        mock_requests_get.return_value = mock_response

        # Call the function under test
        result = get_json(test_url)

        # Assertions
        # Check if requests.get was called with the correct URL
        mock_requests_get.assert_called_once_with(test_url)

        # Check if the result matches the expected payload
        self.assertEqual(result, responce_dict)


if __name__ == "__main__":
    unittest.main()
