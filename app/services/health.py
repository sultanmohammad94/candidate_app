from settings import MONGO_DB_URI
from pymongo import MongoClient
import json

class HealthService:
    """This class represents the health service."""
    
    def check_server_health(self):
        '''Check the health of the server.'''
        return "Server is running"
    
    def list_dbs(self):
        client = MongoClient(MONGO_DB_URI)
        db_names = client.list_database_names()
        return json.dumps(db_names)