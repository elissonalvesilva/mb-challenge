from pymongo import MongoClient
from config.settings import MONGO_URI

class Loader():
    def __init__(self, data) -> None:
        client = MongoClient(MONGO_URI)
        self.client = client
        self.data = data

    def load_data(self):
        self.client.mb.sma.insert_many(self.data)

