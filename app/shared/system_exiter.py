

import os

from shared.singleton import Singleton


@Singleton
class SystemExiter:
    def __init__(self):
        pass

    def exit(self, message):
        print(message)
        os._exit(1)
