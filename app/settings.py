from dotenv import load_dotenv
import os

# load_dotenv()

# Read the Mongo_DB_URI environment variable

MONGO_DB_URI = os.getenv('MONGO_DB_URI', None)
print(f'URI: {MONGO_DB_URI}')