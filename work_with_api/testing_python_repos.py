import unittest
import python_repos


class GitHubReposTestCase(unittest.TestCase):
    """Tests for 'python_repos.py"""

    def test_status_code(self):
        """Status code returns 200 if successful"""
        status_code = python_repos.r.status_code
        self.assertEqual(status_code, 200)

    def test_incomplete_results(self):
        """incomplete results is False"""
        incomplete_results = python_repos.response_dict['incomplete_results']
        self.assertEqual(incomplete_results, False)

    def test_repo_count(self):
        """30 repositories"""
        repos_count = len(python_repos.repo_dicts)
        self.assertEqual(repos_count, 30)


if __name__ == '__main__':
    unittest.main()
