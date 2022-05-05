from datetime import datetime, timedelta
from pymongo import MongoClient
from shared.file_manager import FileManager
from config.settings import Settings


def get_date_range(start_date, end_date):
    date_list = []
    current_date = start_date
    stop_date = end_date
    while current_date >= stop_date:
        date_list.append(stop_date.strftime('%Y-%m-%d'))
        stop_date = stop_date + timedelta(days=1)

    return date_list


start_date = datetime.now()
end_date = datetime.now() - timedelta(days=365)


list_date = get_date_range(start_date, end_date)

if __name__ == "__main__":
    client = MongoClient(Settings.MONGO_URI)

    response = client.mb.sma.aggregate([
        {
            '$match': {
            '$and': [
                {
                "date": {
                    '$gte': end_date
                }
                },
                {
                "date": {
                    '$lte': start_date
                }
                }
            ],

            }
        },
        { '$group': {
            '_id': '$pair',
            'dates': { '$push': { '$dateToString': { 'date': '$date', 'format': '%Y-%m-%d' }}},
        }},
        { '$project': {
            'missingDates': { '$setDifference': [list_date, '$dates'] },
            'pair': '$pair'
        }}
    ])

    response = list(response)
    print()
    filepath = Settings.PROJECT_FOLDER + '/' + Settings.WORKDIRECTORY_TO_RESULTS
    FileManager.create_if_dont_exist(filepath)
    FileManager.write_json_to_file(filepath, start_date.strftime('%Y-%m-%d') + '_' + Settings.UNPROCESSED_FILENAME, response)
    print('CREATE UNPROCESSED DAYS')
