#!/usr/bin/env python3
''' This module contains the unit tests for the utils module. '''
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
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
        mock_response.json.return_value = test_payload
        mock_requests_get.return_value = mock_response

        # Call the function under test
        result = get_json(test_url)

        # Assertions
        # Check if requests.get was called with the correct URL
        mock_requests_get.assert_called_once_with(test_url)

        # Check if the result matches the expected payload
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    '''Test the memoize decorator.'''
    def test_memoize(self):
        '''Test that the memoize decorator works as expected.'''
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # Mock a_method using patch
        with patch.object(TestClass, 'a_method', return_value=42) as mock_a_mthd:
            test_instance = TestClass()
            test_instance.a_property
            test_instance.a_property

            mock_a_mthd.assert_called_once()


if __name__ == "__main__":
    unittest.main()
