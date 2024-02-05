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
# def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
#     """Access nested map with key path.
#     Parameters
#     ----------
#     nested_map: Mapping
#         A nested map
#     path: Sequence
#         a sequence of key representing a path to the value
#     Example
#     -------
#     >>> nested_map = {"a": {"b": {"c": 1}}}
#     >>> access_nested_map(nested_map, ["a", "b", "c"])
#     1
#     """
#     for key in path:
#         if not isinstance(nested_map, Mapping):
#             raise KeyError(key)
#         nested_map = nested_map[key]

#     return nested_map


# res = access_nested_map(nested_map={"a": 1}, path=("a",))
# print(res)

# print('________________________________________________________________')
# res = access_nested_map(nested_map={"a": {"b": 2}}, path=("a",))
# print(res)

# print('________________________________________________________________')
# res = access_nested_map(nested_map={"a": {"b": 2}}, path=("a", "b")
# )
# print(res)


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


#  test get_json

# def get_json(url: str) -> Dict:
#     """Get JSON from remote URL.
#     """
#     response = requests.get(url)
#     return response.json()
# getjson = get_json('https://jsonplaceholder.typicode.com/todos/2')
# print(getjson)

# print('________________________________________________________________')
# experiment memoization
def memoize(fn: Callable) -> Callable:
    """Decorator to memoize a method.
    Example
    -------
    class MyClass:
        @memoize
        def a_method(self):
            print("a_method called")
            return 42
    >>> my_object = MyClass()
    >>> my_object.a_method
    a_method called
    42
    >>> my_object.a_method
    42
    """
    attr_name = "_{}".format(fn.__name__)
    print(attr_name)
    @wraps(fn)
    def memoized(self) -> Callable[..., Any]:
        """"memoized wraps"""
        if not hasattr(self, attr_name):
            print(f'{self.__class__.__name__} has not attribute attr_name: ', attr_name)
            setattr(self, attr_name, fn(self))
        else:
            print(f'{self.__class__.__name__} has attribute attr_name: ', attr_name)
            
        return getattr(self, attr_name)
    #The property function is used to create a property object, which allows getting, setting, and deleting the value of a property.
    return property(memoized)  # type: ignore


#exapmle
class MyClass:
    @memoize
    def a_method(self):
        print("a_method called")
        return 42
my_object = MyClass()
print('--------------------------------1')

print(my_object.a_method)
print('--------------------------------2')

print(my_object.a_method)
print('--------------------------------')
