from fastapi import FastAPI
from database import MongoDBConnection, MongoHandler
from api.v1 import health, user
from settings import MONGO_DB_URI
from events.app_events import ShutdownEvent, StartUpEvent

try:
    # Create an instance of the FastAPI class
    app = FastAPI()
    
    # Registering the event handlers
    @app.on_event("startup")
    async def startup_event():
        try:
            with MongoDBConnection(connection_string=MONGO_DB_URI) as db_client:
            # Create a connection to the MongoDB server
                start_up_event = StartUpEvent(db_client)
                await start_up_event.handle()
                
        except Exception as e:
            print(f'Exception Raised in the Startup Event: {e} ')
            
        finally:
            db_client.close()

    @app.on_event("shutdown")
    async def shutdown_event():
        try:
            with MongoDBConnection(connection_string=MONGO_DB_URI) as db_client:
                shutdown_event = ShutdownEvent(db_client)
                await shutdown_event.handle()
                
        except Exception as e:
            print(f'Exception raised when Shutting-down the serve')
            
        finally:
            db_client.close()
        
    # Registering the Routers
    app.include_router(health.router)
    app.include_router(user.router, prefix='/v1')

except Exception as e:
    print(f'Unexpected Error: {e}')
    
    

