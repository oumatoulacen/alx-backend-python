#!/usr/bin/env python3
"""Tests for github org client
"""

import unittest
from parameterized import parameterized, parameterized_class
from unittest import mock
from unittest.mock import PropertyMock, patch, Mock
import requests
import client
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """ test that the has_license method returns the correct value."""
        self.assertEqual(GithubOrgClient.has_license(repo, license_key), expected)

@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos')
    , TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''Integration test for GithubOrgClient
    '''
    @classmethod
    def setUpClass(cls):
        '''set up class
        '''
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Configure side_effect for mock_get
        def get_side_effect(url, *args, **kwargs):
            if url == "https://api.github.com/orgs/test_org":
                return Mock(json=lambda: cls.org_payload)
            elif url == cls.org_payload["repos_url"]:
                return Mock(json=lambda: cls.repos_payload)
            return Mock(json=lambda: {})

        cls.mock_get.side_effect = get_side_effect


    @classmethod
    def tearDownClass(cls):
        '''tear down class
        '''
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test the public_repos method."""
        client = GithubOrgClient("test_org")
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)
