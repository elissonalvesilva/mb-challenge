from decouple import config

class Settings:
    #DATABASE ENV
    MONGO_URI = config('MONGO_URI')

    # APPLICATION ENV
    API_PORT = config('API_PORT')
    API_HOST = config('API_HOST')
