import os


# Read the Mongo_DB_URI environment variable
MONGO_DB_URI = os.getenv('MONGO_DB_URI', None)
