#!/usr/bin/env python3
"""
Unit tests for GithubOrgClient functionality.
"""
import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient"""

    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test GithubOrgClient.org method."""
        endpoint = f'https://api.github.com/orgs/{org_name}'
        client = GithubOrgClient(org_name)
        client.org()
        mock_get_json.assert_called_once_with(endpoint)

    @parameterized.expand([
        ('random_url', {'repos_url': 'http://some_url.com'}),
    ])
    def test_public_repos_url(self, name, result):
        """Test GithubOrgClient._public_repos_url property."""
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value=result)):
            response = GithubOrgClient(name)._public_repos_url
            self.assertEqual(response, result.get('repos_url'))

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test GithubOrgClient.public_repos method."""
        payload = [{"name": "Google"}, {"name": "TT"}]
        mock_get_json.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "world"
            response = GithubOrgClient('test').public_repos()

            self.assertEqual(response, ["Google", "TT"])
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, key, expectation):
        """Test GithubOrgClient.has_license static method."""
        result = GithubOrgClient.has_license(repo, key)
        self.assertEqual(result, expectation)


@parameterized_class(['org_payload', 'repos_payload',
                      'expected_repos', 'apache2_repos'], TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        cls.get_patcher = patch('requests.get', side_effect=[
            cls.org_payload, cls.repos_payload
        ])
        cls.mocked_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test GithubOrgClient.public_repos with integration."""
        pass

    def test_public_repos_with_license(self):
        """Test GithubOrgClient.public_repos_with_license with integration."""
        pass


if __name__ == '__main__':
    unittest.main()
