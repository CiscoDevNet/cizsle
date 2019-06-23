"""MongoDB database interface."""


import mongoengine
import pymongo.database

import cizsle.config


# Initialize pymongo and mongoengine
client = mongoengine.connect(
    cizsle.config.MONGO_DATABASE,
    host=cizsle.config.MONGO_URL,
)
assert isinstance(client, pymongo.MongoClient)


# Initialize database connection object
db = client[cizsle.config.MONGO_DATABASE]
assert isinstance(db, pymongo.database.Database)
