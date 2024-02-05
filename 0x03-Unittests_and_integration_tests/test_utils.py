#!/usr/bin/env python3
''' This module contains the unit tests for the utils module. '''
from nose.tools import assert_equal
from parameterized import parameterized, parameterized_class
import unittest
from unittest.mock import patch, Mock

from utils import (
    get_json,
    access_nested_map,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([({"a": 1}, ("a",), 1),
                           ({"a": {"b": 2}}, ("a",), {"b": 2}),
                           ({"a": {"b": 2}}, ("a", "b"), 2),])
    def test_access_nested_map(self, nested_map, path, expected):
        assert_equal(access_nested_map(nested_map, path), expected)


if __name__ == "__main__":
    unittest.main()
