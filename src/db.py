from pymongo import MongoClient
import os

class MongoDB:
    def __init__(self):
        # Use environment variable for MongoDB URI, fallback to localhost
        mongo_uri = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/')
        self.client = MongoClient(mongo_uri)
        self.db = self.client['telegram_bot_db']  # Database name

    def get_collection(self, name):
        return self.db[name]