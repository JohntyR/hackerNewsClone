import unittest
import pytest

from hNews.app import app #pylint: disable=import-error

class BasicTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_front_page(self):
        response = self.app.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_other(self):
            response = self.app.get('/a', content_type='html/text')
            self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()