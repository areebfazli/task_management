import unittest
import json
from app import app, db 

class APITestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # Use an in-memory database for testing
        self.app = app.test_client()
        with app.app_context():  # Create an application context
            db.create_all()

    def tearDown(self):
        with app.app_context():  # Create an application context
            db.session.remove()
            db.drop_all()

    def test_create_task(self):
        data = {'title': 'Test Task', 'description': 'This is a test task'}
        response = self.app.post('/tasks', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
