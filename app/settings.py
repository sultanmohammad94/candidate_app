import os
from urllib.parse import quote_plus

# Read the .env environment variables
username: str = os.environ['MONGO_INITDB_ROOT_USERNAME']
password: str = os.environ['MONGO_INITDB_ROOT_PASSWORD']
host:str = os.environ['MONGO_DB_HOST']
port: int = os.environ['MONGO_DB_PORT']

# Constructing the URI
uri = f"mongodb://{username}:{password}@{host}:{port}/"

MONGO_DB_SETTINGS = {
    "MONGO_DB_URI": uri,
    'MONGO_INITDB_ROOT_USERNAME': os.getenv('MONGO_INITDB_ROOT_USERNAME', None),
    'MONGO_INITDB_ROOT_PASSWORD': os.getenv('MONGO_INITDB_ROOT_PASSWORD', None),
    'DEFAULT_DB_NAME': os.getenv('MONGODB_DB_NAME', None),    
    'MONGODB_USER': quote_plus(os.getenv('MONGODB_USER', None)),
    'MONGODB_PASSWORD': quote_plus(os.getenv('MONGODB_PASSWORD', None)),
    "MONGO_DB_HOST": os.getenv('MONGO_DB_HOST', None),
    "MONGO_DB_PORT": int(os.getenv('MONGO_DB_PORT', 0)),
}