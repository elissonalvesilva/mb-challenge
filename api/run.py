from datetime import datetime, timedelta
from config.settings import Settings
from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/<pair>/mms', methods=['GET'])
def get_mms(pair):
    args = request.args
    from_date = args.get('from')
    to_date = args.get('to')
    range = args.get('range')


    if from_date:
        from_date = to_timestamp(from_date)
        can_able_start_date(from_date)
        from_date = datetime.fromtimestamp(from_date)
    else:
        print('error')

    if to_date:
        to_date = datetime.fromtimestamp(to_timestamp(to_date))
    else:
        to_date = datetime.now() - timedelta(days=1)

    if range:
        range = int(range)
    else:
        range = 20

    if from_is_greater_than_to(from_date, to_date) == True:
        print('ERROR')

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

    return jsonify(response)


def to_timestamp(date):
    if type(date) != str:
        date = date.strftime("%Y-%m-%d")
        element = datetime.strptime(date,"%Y-%m-%d")
        timestamp = int(datetime.timestamp(element))
    else:
        timestamp = int(date)
    return timestamp

def from_is_greater_than_to(from_date, to_date):
    if from_date > to_date:
        return True
    return False

def can_able_start_date(date):
    current_date_timestamp = datetime.now()
    date_to_compare = datetime.fromtimestamp(date)

    difference = current_date_timestamp - date_to_compare

    if difference.days > 365:
        print('ERRROR')




