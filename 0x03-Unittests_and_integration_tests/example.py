from unittest import TestCase
import unittest
from parameterized import parameterized

# Test
import requests
from functools import wraps
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)
# ....


# def add(a, b):
#     return a + b

# # simple unit tests for the add function
# class TestAdd(TestCase):
#     '''Test the add function.'''
#     @parameterized.expand([
#         (1, 2, 3),
#         (1, 1, 2),
#         (1, 0, 1),
#         (0, 0, 0),
#         (-1, -1, -2),
#         (-1, 1, 0),
#         (-1, 0, -1),
#         (1, -1, 0),
#         (0, -1, -1),
#         (0, 1, 1),
#         (0, -1, -1),
#     ])
#     def test_add(self, a, b, c):
#         '''Test that the add function adds two numbers.'''
#         self.assertEqual(add(a, b), c)



# if __name__ == "__main__":
#     unittest.main()



# test acces_nested_map
def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    """Access nested map with key path.
    Parameters
    ----------
    nested_map: Mapping
        A nested map
    path: Sequence
        a sequence of key representing a path to the value
    Example
    -------
    >>> nested_map = {"a": {"b": {"c": 1}}}
    >>> access_nested_map(nested_map, ["a", "b", "c"])
    1
    """
    for key in path:
        if not isinstance(nested_map, Mapping):
            raise KeyError(key)
        nested_map = nested_map[key]

    return nested_map


res = access_nested_map(nested_map={"a": 1}, path=("a",))
print(res)

print('________________________________________________________________')
res = access_nested_map(nested_map={"a": {"b": 2}}, path=("a",))
print(res)

print('________________________________________________________________')
res = access_nested_map(nested_map={"a": {"b": 2}}, path=("a", "b")
)
print(res)


#import unittest
# from collections.abc import Mapping
# from typing import Any, Sequence

# class TestAccessNestedMap(unittest.TestCase):
#     def test_access_nested_map(self):
#         nested_map = {"a": {"b": {"c": 1}}}
#         path = ["a", "b", "c"]
#         result = access_nested_map(nested_map, path)
#         self.assertEqual(result, 1)

#     def test_access_nested_map_key_error(self):
#         nested_map = {"a": {"b": {"c": 1}}}
#         path = ["a", "b", "d"]  # 'd' doesn't exist in the nested_map
#         with self.assertRaises(KeyError):
#             access_nested_map(nested_map, path)

# if __name__ == '__main__':
#     unittest.main()