#!/usr/bin/env python3
'''Test the client module'''
from parameterized import parameterized, parameterized_class
from unittest import TestCase
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(TestCase):
    '''Test GithubOrgClient'''

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json', return_value={'blanco': 'negro'})
    def test_org(self, name, mock):
        '''Test GithubOrgClient.org'''
        test_obj = GithubOrgClient(name)
        self.assertEqual(test_obj.org, mock.return_value)
        mock.assert_called_once()

    def test_public_repos_url(self):
        '''Test GithubOrgClient._public_repos_url'''
        g = GithubOrgClient
        test_obj = g('braap')

        with patch.object(g, 'org', new_callable=PropertyMock) as org:
            org.return_value = {'repos_url': 'negro'}
            url = test_obj._public_repos_url
            self.assertEqual(url, org.return_value['repos_url'])
            org.assert_called_once()

    @patch('client.get_json', return_value=[{'name': 'negro'}])
    def test_public_repos(self, mock):
        '''Test GithubOrgClient.public_repos'''
        g = GithubOrgClient
        p = PropertyMock
        test_obj = g('braap 2')
        with patch.object(g, '_public_repos_url', new_callable=p) as url:
            url.return_value = 'negro'
            self.assertIn(url.return_value, test_obj.public_repos())
            mock.assert_called_once()
            url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, license, key, returns):
        '''Test GithubOrgClient.has_license'''
        test_obj = GithubOrgClient('braap the third')
        self.assertEqual(test_obj.has_license(license, key), returns)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    [(
        TEST_PAYLOAD[0][0],
        TEST_PAYLOAD[0][1],
        TEST_PAYLOAD[0][2],
        TEST_PAYLOAD[0][3]
    )]
)
class TestIntegrationGithubOrgClient(TestCase):
    '''Integration test for GithubOrgClient'''

    @classmethod
    def setUpClass(cls):
        '''Set up class for the integration test'''

        def patched_requests(*args):
            '''The patched requests function'''

            class PatchedResponse:
                '''Patched responses for the patched requests'''
                def __init__(self, json_data):
                    self.json_data = json_data

                def json(self):
                    return self.json_data
            if args[0] == "https://api.github.com/orgs/google":
                return PatchedResponse(TEST_PAYLOAD[0][0])
            if args[0] == TEST_PAYLOAD[0][0]["repos_url"]:
                return PatchedResponse(TEST_PAYLOAD[0][1])

        cls.get_patcher = patch('requests.get', side_effect=patched_requests)
        cls.get_patcher.start()
        cls.g = GithubOrgClient('google')

    @classmethod
    def tearDownClass(cls):
        '''Closes all opened changes'''
        cls.get_patcher.stop()

    def test_public_repos(self):
        '''Tests GithubOrgClient.public_repos'''
        self.assertEqual(self.g.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        '''Test GithubOrgClient.public_repos with attatched license'''
        self.assertEqual(
            self.g.public_repos(license="apache-2.0"),
            self.apache2_repos
        )
