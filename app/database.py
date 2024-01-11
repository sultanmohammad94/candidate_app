from pymongo.mongo_client import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection

class MongoDBConnection:
    """A class to manage the connection to MongoDB."""

    def __init__(self, connection_string: str):
        """Initialize the MongoDBConnection class.

        Args:
            connection_string (str): The MongoDB connection string.
        """
        self.connection_string = connection_string
        self.client = None
        
    def __enter__(self):
        self.client = MongoClient(self.connection_string)
        return self.client

    def __exit__(self, exc_type, exc_value, traceback):
        if self.client is not None:
            self.client.close()

    def connect(self)->MongoClient:
        """Establish a connection to the MongoDB server."""
        with MongoClient(self.connection_string) as client:
            self.client = client
            return self.client
            
    def ping(self):
        """Send a ping command to the MongoDB server."""
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(f'Failed to Ping The MongoDB with error {e}')
            
    def is_connected(self) -> bool:
        """Check if the connection to MongoDB is established.

        Returns:
            bool: True if connected, False otherwise.
        """
        return self.client is not None

    def disconnect(self):
        """Close the connection to the MongoDB server."""
        try:
            self.client.close()
        except Exception as e:
            print(f'Failed to close connection to MongoDB server')


class MongoHandler:
    """A class to handle MongoDB operations."""

    def __init__(self, db_name: str, connection: MongoDBConnection):
        """Initialize the MongoHandler class.

        Args:
            db_name (str): The name of the database.
            collection_name (str): The name of the collection.
            connection (MongoDBConnection): An instance of MongoDBConnection class.
        """
        self.db_name = db_name
        self.connection = connection

    def create_database(self) -> Database:
        """Create a database if it does not exist.

        Returns:
            bool: True if the database is created or already exists, False otherwise.
        """
        if not self.connection.is_connected():
                return None
        db_list = self.connection.client.list_database_names()
        database = None
        
        if self.db_name not in db_list:
            database = self.connection.client[self.db_name]
            
        return database  # Return True if the database already exists


    def create_collection(self, collection_name: str) -> Collection:
        """Create a collection if it does not exist.

        Returns:
            bool: True if the collection is created or already exists, False otherwise.
        """
        if not self.connection.is_connected():
            return None

        collection_list = self.connection.client[self.db_name].list_collection_names()
        if collection_name not in collection_list:
            database = self.connection.client[self.db_name]
            collection = database[collection_name]
            return collection
        return None

    def get_collection(self, collection_name: str)->Collection:
        """Get the specified collection.

        Args:
            collection_name (str): The name of the collection to retrieve.

        Returns:
            collection: The MongoDB collection object if connected and collection exists, None otherwise.
        """
        if not self.connection.is_connected():
            return None  # Return None if not connected to the database

        database = self.connection.client[self.db_name]
        if collection_name in database.list_collection_names():
            return database[collection_name]  # Return the collection object if it exists
        else:
            return None  # Return None if the collection does not exist
        
    
    
    