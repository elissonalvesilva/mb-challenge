import requests

from shared.singleton import Singleton


@Singleton
class Request():
    def get_result(self, url):
        try:
            result = requests.get(url)
            result.raise_for_status()
            return result
        except requests.exceptions.RequestException as err:
            raise err
