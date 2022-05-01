from config.settings import WORKDIRECTORY_TO_RESULTS
from shared.file_manager import FileManager
from shared.singleton import Singleton


@Singleton
class Writer:
    """
    Writes the resultant KPIs to files.
    """

    def __init__(self):
        pass

    def run(self, collections):
        for collection in collections:
            filepath = WORKDIRECTORY_TO_RESULTS
            filepath = filepath.format(date=collection['mb_meta']['timestamp'][0:10])
            FileManager.create_if_dont_exist(filepath)
            FileManager.write_json_to_file(filepath, collection['mb_meta']['pair'], collection)
