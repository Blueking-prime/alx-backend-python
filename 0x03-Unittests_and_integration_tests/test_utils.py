#!/usr/bin/env python3
'''Test the utils module'''
from parameterized import parameterized
from unittest import TestCase
from unittest.mock import Mock, patch
from utils import access_nested_map, get_json, memoize, requests


class TestAccessNestedMap(TestCase):
    '''Tests utils.access_nested_map'''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, map, path, expected):
        '''Test right return for access_nested_map'''
        self.assertEqual(expected, access_nested_map(map, path))

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, map, path):
        '''Test exceptions for access_nested_map'''
        with self.assertRaises(KeyError):
            access_nested_map(map, path)


class TestGetJson(TestCase):
    '''Test get json'''

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, result):
        '''Test right return for get_json'''
        with patch.object(requests, 'get', Mock) as response:
            response.json = Mock(return_value=result)
            self.assertEqual(get_json(url), result)


class TestMemoize(TestCase):
    '''Test memoize function'''

    def test_memoize(self):
        '''Test right return for memoize'''
        class TestClass:
            '''Test class'''

            def a_method(self):
                '''Test method'''
                return 42

            @memoize
            def a_property(self):
                '''Test method to test property'''
                return self.a_method()

        with patch.object(TestClass, 'a_method') as meth:
            test_obj = TestClass()
            test_obj.a_property()
            test_obj.a_property()
            meth.assert_called_once()
