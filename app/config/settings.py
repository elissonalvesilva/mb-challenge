from decouple import config
from urllib.parse import quote_plus

__all__ = [
    'DEFINITION_FILE',
    'WORK_DIRECTORY_TO_RESULTS',
    'get_mongodb_uri',
    'MONGO_URI',
    'JOB_RETRIES'
]

# DEFINITION FILE DIRECTORIES
PROJECT_FOLDER = config('PROJECT_FOLDER') + "/"
DEFINITION_FILE = PROJECT_FOLDER + config('MB_PATH_JOB_DEFINITIONS')
WORKDIRECTORY_TO_RESULTS = config('WORKDIRECTORY_TO_RESULTS') + '/{date}'

#DATABASE ENV
MONGO_URI = config('MONGO_URI')

# PROJECT ENV
JOB_RETRIES = int(config('JOB_RETRIES'))
