from decouple import config

class Settings:
    #DATABASE ENV
    MONGO_URI = config('MONGO_URI')
