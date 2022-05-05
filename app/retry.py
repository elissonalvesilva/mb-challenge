from datetime import datetime
import os
from app.shared.system_exiter import SystemExiter;
from shared.file_manager import FileManager
from config.settings import Settings
import re
from urllib.parse import urlparse, parse_qs

def timestamp_to_str_date(timestamp_str):
    return datetime.fromtimestamp(int(timestamp_str)).strftime('%Y-%m-%d')

if __name__ == "__main__":
    filepath = Settings.PROJECT_FOLDER + Settings.WORKDIRECTORY_TO_RETRY
    retries_urls = FileManager.read_from_string_file(filepath, Settings.RETRY_FILENAME)
    pairs = []
    from_date = None
    to_date = None
    if retries_urls == None:
        SystemExiter.Instance().exit('Not found urls to retry')

    for retry_url in retries_urls:
        url_parsed = urlparse(retry_url)
        query_string = parse_qs(url_parsed.query)
        pair = re.search('/v4/(.*)/candles', url_parsed.path).group(1)
        from_date = timestamp_to_str_date(query_string['from'][0])
        to_date = timestamp_to_str_date(query_string['to'][0])
        pairs.append(pair)

    pairs = ','.join(pairs)

    FileManager.clear_file(filepath + '/' + Settings.RETRY_FILENAME)

    os.system(f'python app/ingestion.py -sd {from_date} -ed {to_date} -r -pr {pairs}')



