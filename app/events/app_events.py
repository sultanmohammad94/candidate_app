from abc import ABC, abstractmethod
from fastapi import FastAPI
from database import MongoDBConnection, MongoHandler

class ApplicationEvents:
    """This class represents the application events."""
    
    @abstractmethod
    async def handle(self):
        '''An abstract method that handles the application event'''
        raise NotImplementedError


class StartUpEvent(ApplicationEvents):
    """This class is responsible for handling the start up events."""
    
    def __init__(self, connection: MongoDBConnection):
        self._event_name = 'startup'
        self._connection = connection
    
    @property
    def name(self):
        '''Get the name of the event'''
        return self._event_name

    async def handle(self):
        '''Handle the startup event and create the Database and collections'''
        try:
            # Connecting to the database
            mongo_handler = MongoHandler(db_name='db', connection= self._connection)
            if self._connection.is_connected():
                # Creating the Database and Collections
                mongo_handler.create_database()
                
                # Creating the Collections
                mongo_handler.create_collection('users')
                mongo_handler.create_collection('candidates')
                print(f'Startup Event completed Successfully')
                
        except Exception as e:
            print(f'Startup Handler failed to handle with exception: {e}')
            
            
class ShutdownEvent(ApplicationEvents):
    """This class is responsible for handling the start up events."""
    
    def __init__(self, connection: MongoDBConnection):
        self._event_name = 'shutdown'
        self.connection = connection
    
    @property
    def name(self):
        '''Get the name of the event'''
        return self._event_name

    async def handle(self):
        '''Handle the shutdown event of the Application'''
        try:
            self.connection.close()
            print(f'Shutdown Event completed Successfully')
            
        except Exception as e:
            print(f'Shutdown Handler failed to handle with exception: {e}')
        finally:
            self.connection.client.close()