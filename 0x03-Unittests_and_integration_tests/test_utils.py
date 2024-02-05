#!/usr/bin/env python3
''' This module contains the unit tests for the utils module. '''
import unittest
from parameterized import parameterized, param
from utils import *
from unittest.mock import Mock


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


class TestGetJson(unittest.TestCase):
    '''Test Case to est get_json function.'''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        '''Test get_json function'''
        api_mock = Mock()
        api_mock.get_json(test_url).return_value = test_payload
        # print(api_mock.get_json(test_url).return_value)
        self.assertTrue(api_mock.get_json(test_url), test_payload)


if __name__ == "__main__":
    unittest.main()
