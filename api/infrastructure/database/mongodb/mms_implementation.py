from datetime import datetime
from typing import Dict, List
from pymongo import MongoClient

from api.application.protocols.get_mms_repository import GetMMSRepository
from api.config.settings import Settings


class MMSImplementation(GetMMSRepository):
    def __init__(self) -> None:
        super().__init__()
        self.client = MongoClient(Settings.MONGO_URI)


    def get_mms_by_parameters(self, pair: str, from_date: datetime, to_date: datetime, range: int) -> List[Dict[float, int]]:
        client = MongoClient(Settings.MONGO_URI)
        query = { '$match': { '$and': [{"date": {'$gte': from_date }}, {"date": {'$lte': to_date }}, { 'pair': pair }]}}
        project = {
            '$project': {
                '_id': False,
                'mms': f'$SMA_{range}',
                'timestamp': { '$dateToString': { 'date': '$date', 'format': '%Y-%m-%d' } },
            }
        }
        response = client.mb.sma.aggregate([query, project])

        response = list(response)

        return response
