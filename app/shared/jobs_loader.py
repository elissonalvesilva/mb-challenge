import json
import calendar
import time

from shared.singleton import Singleton
from config import settings
from shared.job import Job


@Singleton
class JobsLoader():
    def __init__(self) -> None:
        self.loaded_jobs = {}
        self.from_date = calendar.timegm(time.gmtime())
        self.to_date = calendar.timegm(time.gmtime())

    def set_range(self, from_date, to_date = calendar.timegm(time.gmtime())):
        self.from_date = from_date
        self.to_date = to_date

    def load_jobs(self):
        loaded_jobs_definitions = self._load_jobs_definitions()
        for job_definition in loaded_jobs_definitions:
            new_job = self._create_job_definition(job_definition)
            self.loaded_jobs[new_job.pair] = new_job

    def _load_jobs_definitions(self):
        loaded_jobs_definitions = []
        file_content = self._read_jobs_definitions_file(settings.DEFINITION_FILE)
        loaded_jobs_definitions += (self._parse_jobs_definitions(file_content))

        self._validate_jobs()
        return loaded_jobs_definitions

    def _read_jobs_definitions_file(self, filename):
        file_pointer = open(filename, 'r', encoding='utf-8')
        file_content = file_pointer.read()
        file_content = self._remove_new_lines(file_content)
        file_pointer.close()
        return file_content

    def _remove_new_lines(self, content):
        return content.replace('\n', '')

    def _parse_jobs_definitions(self, definitions):
        return json.loads(definitions)

    def _create_job_definition(self, job_definition):
        action = job_definition.get('action', None)
        pair = job_definition.get('pair', None)
        url = self._make_url(job_definition.get('url', None))
        table_name = job_definition.get('table_name', None)
        range = job_definition.get('range', None)
        job = Job(action, pair, url, table_name, range)
        return job

    def _validate_jobs(self) -> None:
        for job in list(self.loaded_jobs.keys()):
            if self.loaded_jobs[job].action == 'create' and self.loaded_jobs[job].table_name == None:
                raise "Error"

    def _make_url(self, url):
        if url == None:
            raise "Error"
        if self.to_date == None:
            self.to_date = calendar.timegm(time.gmtime())

        url = url + '?from=' + str(self.from_date) + '&to='+ str(self.to_date)
        return url