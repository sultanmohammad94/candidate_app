import unittest
from unittest.mock import patch, MagicMock
from pymongo import MongoClient
from utils.logger import log_result_and_type
from database import MongoDBConnection, MongoURIConnection
from settings import MONGO_DB_SETTINGS

class TestMongoDBConnection(unittest.TestCase):
    
    def setUp(self):
        """Run before each test."""
        uri = MONGO_DB_SETTINGS.get("MONGO_DB_URI")
        connection_info = MongoURIConnection(uri)
        # Construct the MongoDB connection URI
        self.client: MongoDBConnection = MongoDBConnection(connection_info)
    
    def test_connect_to_database(self):
        database = self.client.connect()
        self.assertIsNotNone(database)
    
    def test_connect_using_uri(self):
        uri = MONGO_DB_SETTINGS.get("MONGO_DB_URI")
        connection_info = MongoURIConnection(uri)
        # Construct the MongoDB connection URI
        self.client: MongoDBConnection = MongoDBConnection(connection_info)
        self.assertIsNotNone(self.client)
    
    @patch('database.MongoDBConnection.is_connected')
    def test_is_not_connected_on_start(self, mock_is_connected):
        mock_is_connected.return_value = False
        self.assertEqual(self.client.is_connected(), False)
    
    @patch('database.MongoDBConnection.is_connected')
    def test_is_connected(self, mock_is_connected):
        mock_is_connected.return_value = True
        self.assertEqual(self.client.is_connected(), True)
    
    @patch('database.MongoDBConnection.disconnect')
    def test_disconnect(self, mock_close):
        self.client.disconnect()
        mock_close.assert_called_once()
    
    def tearDown(self) -> None:
        self.client = None

if __name__ == '__main__':
    unittest.main()