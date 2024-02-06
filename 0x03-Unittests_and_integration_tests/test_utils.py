#!/usr/bin/env python3
""" A script to unit test for utils.access_nested_map
"""

import unittest
from unittest import mock
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ A class to test utils.access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),

        ])
    def test_access_nested_map(self, dict, path, expected):
        """Test the access of a nested map."""
        result = access_nested_map(dict, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self,
                                         dict,
                                         path,
                                         expected,
                                         ):
        with self.assertRaises(expected):
            access_nested_map(dict, path)


class TestGetJson(unittest.TestCase):
    """ mock requests"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @mock.patch('requests.get')
    def test_get_json(self,  test_url, test_payload, mock_get):
        """ test that utils.get_json returns the expected result. """
        mock_get.return_value.json.return_value = test_payload
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """to mock a_method. Test that when calling a_property twice,
    """
    def test_memoize(self):
        """to mock a_method. Test that when calling a_property twice"""

        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mck:
            inst = TestClass()
            inst.a_property
            inst.a_property

            mck.assert_called_once()
