from pymongo import MongoClient
from config.settings import Settings


class Loader():
    def __init__(self, data) -> None:
        client = MongoClient(Settings.MONGO_URI)
        self.client = client
        self.data = data

    def load_data(self):
        self.client.mb.sma.insert_many(self.data)

