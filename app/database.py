from pymongo.mongo_client import MongoClient
from pymongo.errors import InvalidURI, ConnectionFailure
from pymongo.database import Database
from settings import MONGO_DB_SETTINGS
from utils.logger import log_result_and_type, ApplicationLogger
from abc import ABC, abstractmethod

class DBBaseConnectionInfo(ABC):
    @abstractmethod
    def get_info(self):
        raise NotImplementedError

class MongoUsernamePasswordConnection(DBBaseConnectionInfo):
    def __init__(self, username: str, password: str, host: str, port: int, db_name: str = None):
        self._username = username
        self._password = password
        self._host = host
        self._port = port
        self._db_name = db_name
    
    def get_info(self)->str:
        if self._db_name is None:
            return f"mongodb://{self._username}:{self._password}@{self._host}:{self._port}/"
        return f"mongodb://{self._username}:{self._password}@{self._host}:{self._port}/{self._db_name}"
        
class MongoURIConnection(DBBaseConnectionInfo):
    def __init__(self, uri: str):
        self.uri = uri
    
    def get_info(self)->str:
        return self.uri
        

class MongoDBConnection:
    """This class is responsible for managing the connection to a MongoDB server."""
    
    def __init__(self, connection_info: DBBaseConnectionInfo, db_name: str = 'demo_db'):
        self.connection_string = connection_info.get_info()
        self.client: MongoClient = None
        self.db_name = db_name
        self.db: Database = None
    
    def connect(self) -> Database:
        '''This method try to connect to a database '''
        if not self.connection_string:
            raise ValueError('Connection String is required')
        
        if not self.client and not self.is_connected():
            try:
                self.client = MongoClient(self.connection_string)
                self.db = self.client[self.db_name]
                
            except Exception as e:
                ApplicationLogger().log_error(f'Error in MongoDBConnection.connect: {str(e)}')
                ApplicationLogger().log_error(f'Error in MongoDBConnection.connect: {self.connection_string}')
                raise InvalidURI(f"Invalid connection string: {str(e)}")
            
        return self.db
    
    def is_connected(self):
        '''Returns True if the connection and False if not connected'''
        try:
            if self.client is None or not self.client.server_info():
                return False
            return True
        
        except Exception as e:
            ApplicationLogger().log_error(f'MongoDBConnection.is_connected: {str(e)}')
            raise ConnectionFailure('Failed to connect to MongoDBserver')
            
    def disconnect(self):
        '''Check whether if there is a connection to MongoDB then close it'''
        try:
            if self.client and self.is_connected():
                self.client.close()
        except Exception as e:
            ApplicationLogger().log_error(f'Exception MongoDBConnection.disconnect has been raised: {str(e)}')
            raise ConnectionFailure()
        finally:
            MongoClient(self.connection_string).close()

    @property
    def database(self)->Database:
        '''This property returns the database object of type pymongo.Database for the db_name'''
        try:
            if self.is_connected():
                return self.db
            return None
        
        except Exception as e:
            ApplicationLogger().log_error(f'Error getting database {str(e)}')
            raise ConnectionFailure(f'Exception raised while trying to get the database: {str(e)}')
    
    def collection_names(self):
        '''Get the collection names of the connected database'''
        try:
            if self.database:
                return self.database.collection_names()
            return None
        except Exception as e:
            ApplicationLogger().log_error(f'Failed to get collection names due to exception: {str(e)}')
                
        
        
                
                