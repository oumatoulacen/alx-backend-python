#!/usr/bin/env python3
"""Tests for utils.py
"""

from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map

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

    def test_access_nested_map_exception(self):
        """Test access_nested_map with invalid path.
        """
        with self.assertRaises(KeyError):
            access_nested_map({"a": 1}, ("a", "b"))
