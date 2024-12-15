#!/usr/bin/env python3
"""Tests for github org client
"""

import unittest
from parameterized import parameterized
from unittest import mock
from unittest.mock import PropertyMock, patch
import requests
import client
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """_class and implement the test_org method.
    """
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, input, mock):
        """ test that GithubOrgClient.org returns the correct value."""
        test_class = GithubOrgClient(input)
        test_class.org()
        mock.assert_called_once_with(f'https://api.github.com/orgs/{input}')

    def test_public_repos_url(self):
        """ test that the _public_repos_url method returns the correct value"""
        with patch(
            'client.GithubOrgClient.org',
            new_callable=PropertyMock
        ) as mock:
            mock.return_value = {'repos_url': 'test_value'}
            test_class = GithubOrgClient('test')
            self.assertEqual(test_class._public_repos_url, 'test_value')

    @patch('client.get_json')
    def test_public_repos(self, mocked_get_json):
        """ test that the public_repos method returns the correct value."""
        mocked_get_json.return_value = [
            {'name': 'repo1', 'license': {'key': 'my_license'}},
            {'name': 'repo2', 'license': {'key': 'other_license'}}
        ]
        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock
        ) as mp:
            mp.return_value = 'https://api.github.com/orgs/test/repos'
            test_class = GithubOrgClient('test')
            self.assertEqual(test_class.public_repos('my_license'), ['repo1'])
