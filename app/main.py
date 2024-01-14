from fastapi import FastAPI
from database import MongoDBConnection, MongoURIConnection
from settings import MONGO_DB_SETTINGS
from utils.logger import ApplicationLogger
from routes.user_routes import user_router
from routes.health_routes import health_router


# Create an instance of the FastAPI class
app = FastAPI(debug=True)

# Define a function to lazily connect to the database
def get_database():
    uri = MONGO_DB_SETTINGS.get("MONGO_DB_URI")
    connection_info = MongoURIConnection(uri)
    client = MongoDBConnection(connection_info, db_name='test_elevatus_db')
    return client.connect()

# Use a dependency to get the database connection when needed
async def get_db():
    db = get_database()
    ApplicationLogger().log_info(f'Connected to the {db.name} Database')
    
    try:
        yield db
    finally:
        # Clean up the database connection if needed
        db.close()
    

#* Add routers to the application
app.include_router(user_router)
app.include_router(health_router)
