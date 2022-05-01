import requests

from shared.singleton import Singleton


@Singleton
class Request():
    def get_result(self, url):
        result = requests.get(url)
        return result
