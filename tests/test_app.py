import unittest
import pytest

from hNews.app import app #pylint: disable=import-error

class BasicTestCase(unittest.TestCase):
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'<html><h1>Hello new world</h1></html>')

    def test_other(self):
            tester = app.test_client(self)
            response = tester.get('a', content_type='html/text')
            self.assertEqual(response.status_code, 404)
            self.assertTrue(b'does not exist' in response.data)

if __name__ == '__main__':
    unittest.main()