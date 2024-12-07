import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.app.post('/login', data={'username': '692919155', 'password': '0213546879bB'})
        self.assertIn(b'Login failed!', response.data)

if __name__ == '__main__':
    unittest.main()
```