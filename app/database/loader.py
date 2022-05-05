from pymongo import MongoClient
from config.settings import Settings
from shared.system_exiter import SystemExiter


class Loader():
    def __init__(self, data) -> None:
        client = MongoClient(Settings.MONGO_URI)
        self.client = client
        self.data = data

    def load_data(self):
        try:
            self.client.mb.sma.insert_many(self.data)
        except Exception as e:
            SystemExiter.Instance().exit(e)
