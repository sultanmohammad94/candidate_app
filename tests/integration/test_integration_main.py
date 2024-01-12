import unittest
from fastapi.testclient import TestClient
from main import app, get_db
from database import MongoDBConnection, MongoURIConnection
from settings import MONGO_DB_SETTINGS
from utils.logger import ApplicationLogger
from pymongo import MongoClient

class TestAppIntegration(unittest.TestCase):
    
    def setUp(self):
        """Run before each test."""
        self.client = TestClient(app)
        self.db = get_db()
        self.mongo_uri = MONGO_DB_SETTINGS.get("MONGO_DB_URI")
    
    def test_server_health(self):
        response = self.client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"message": "Server is running"}
    
    def test_database_connectivity(self):
        try:
            uri = MONGO_DB_SETTINGS.get("MONGO_DB_URI")
            connection_info = MongoURIConnection(uri)
            client = MongoDBConnection(connection_info, db_name='test_db')
            database = client.connect()
            ApplicationLogger().log_info(f'Connected to the {database.name} Database')
            
            self.assertIsNotNone(database)
            self.assertEqual(database.name, client.database.name)
            ApplicationLogger().log_info(f'Mongo_URI: {self.mongo_uri}')
            
        except Exception as e:
            ApplicationLogger().log_error(f'test_database_connectivity: {str(e)}')
            assert False, f"Failed to connect to the database: {str(e)}"
    
    def tearDown(self):
        """Run after each test."""
        self.client = None

if __name__ == '__main__':
    unittest.main()