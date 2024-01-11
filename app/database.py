from pymongo.mongo_client import MongoClient
from settings import MONGO_DB_URI

# Create a new client and connect to the server
CLIENT = MongoClient(MONGO_DB_URI)

# Send a ping to confirm a successful connection
try:
    CLIENT.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

