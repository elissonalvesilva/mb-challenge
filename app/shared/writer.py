from config.settings import Settings
from shared.file_manager import FileManager
from shared.singleton import Singleton


@Singleton
class Writer:
    """
    Writes the results.
    """

    def __init__(self):
        pass


    def url_to_retry(self, url_to_retry):
        filepath = Settings.WORKDIRECTORY_TO_RETRY
        FileManager.create_if_dont_exist(filepath)
        FileManager.write_string_to_file(filepath, 'retries', url_to_retry)
