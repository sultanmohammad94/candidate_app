import pytest
from pymongo import MongoClient
from app.database import MongoDBConnection, MongoHandler
from app.settings import MONGO_DB_URI

@pytest.fixture(scope="module")
def connection():
    connection_string = MONGO_DB_URI
    connection = MongoDBConnection(connection_string)
    yield connection
    connection.disconnect()


@pytest.fixture(scope="module")
def handler(connection):
    db_name = "test_db"
    handler = MongoHandler(db_name, connection)
    yield handler
    collection = handler.get_collection("test_collection")
    if collection:
        collection.drop()


def test_connection(connection):
    client = connection.connect()
    assert isinstance(client, MongoClient)
    assert connection.is_connected()


def test_create_database(handler):
    database = handler.create_database()
    assert database is not None
    assert isinstance(database, MongoClient)


def test_create_collection(handler):
    collection_name = "test_collection"
    collection = handler.create_collection(collection_name)
    assert collection is not None
    assert collection_name in handler.connection.client[handler.db_name].list_collection_names()


def test_get_collection(handler):
    collection_name = "test_collection"
    collection = handler.create_collection(collection_name)
    retrieved_collection = handler.get_collection(collection_name)
    assert retrieved_collection is not None
    assert retrieved_collection.name == collection_name
