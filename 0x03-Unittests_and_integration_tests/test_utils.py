#!/usr/bin/env python3
"""
Unit tests with parameterization for access_nested_map, get_json, and memoize.
"""
import unittest
from unittest import mock
from unittest.mock import patch
import requests
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map function"""

    @parameterized.expand([
        # Test accessing a key in a simple dictionary.
        ({"a": 1}, ("a",), 1),

        # Test accessing a key in a nested dictionary.
        ({"a": {"b": 2}}, ("a",), {"b": 2}),

        # Test accessing a nested key in a dictionary.
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, returned):
        """Test access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), returned)

    @parameterized.expand([
        # Test accessing a non-existent key in a dictionary.
        ({}, ("a",), "a"),

        # Test accessing a non-existent nested key in a dictionary.
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path, ret_error):
        """Test access_nested_map KeyError"""
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
            self.assertEqual(ret_error, str(error.exception))


class TestGetJson(unittest.TestCase):
    """Test get_json function"""

    @parameterized.expand([
        # Test getting JSON data from a URL.
        ("http://example.com", {"payload": True}),

        # Test getting JSON data from another URL.
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """Test get_json with mock requests.get"""
        response = mock.Mock()
        response.json.return_value = payload

        with mock.patch('requests.get', return_value=response):
            request = get_json(url)
            self.assertEqual(request, payload)
            response.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """Test memoize decorator"""

    def test_memoize(self):
        """Test memoize decorator"""
        class TestClass:
            """Test class"""

            def a_method(self):
                """Test method"""
                return 42

            @memoize
            def a_property(self):
                """Memoized property"""
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as patched:
            test_class = TestClass()
            returned = test_class.a_property
            returned = test_class.a_property

            self.assertEqual(returned, 42)
            patched.assert_called_once()


if __name__ == '__main__':
    unittest.main()
