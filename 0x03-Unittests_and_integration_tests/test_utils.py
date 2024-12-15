#!/usr/bin/env python3
"""Tests for utils.py, run with `python -m unittest -v test_utils`.
"""

from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
import requests


class TestAccessNestedMap(TestCase):
    """Tests for access_nested_map function.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map with different inputs.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access_nested_map with invalid path.
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(TestCase):
    """Tests for get_json function.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Test get_json with different inputs.
        """
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)
            mock_get.assert_called_once_with(test_url)


class TestMemoize(TestCase):
    """Tests for memoize decorator.
    """
    def test_memoize(self):
        """Test memoize decorator.
        """
        class MyClass:
            """Simple class to test memoize decorator.
            """
            def a_method(self):
                '''a method'''
                return 42

            @memoize
            def a_property(self):
                '''a property'''
                return self.a_method()

        with patch.object(MyClass, 'a_method') as mock_method:
            mock_method.return_value = 42
            my_object = MyClass()
            self.assertEqual(my_object.a_property, 42)
            self.assertEqual(my_object.a_property, 42)
            mock_method.assert_called_once()
