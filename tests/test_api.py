import unittest
import pytest
import requests

from hNews.app import app #pylint: disable=import-error

class BasicTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_top_stories(self):
        response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')
        self.assertEqual(response.status_code, 200)


    def test_specific_item(self):
        itemNum = 8863
        response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{itemNum}.json?print=pretty')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()