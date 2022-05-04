import time
import datetime
from shared.system_configure import SystemConfigure
from database.loader import Loader

from shared.jobs_loader import JobsLoader
from shared.jobs_manager import JobsManager
from shared.writer import Writer
from shared.arg_parser import ArgsParser
from shared.execution_info import ExecutionInfo
class Run():
    def __init__(self) -> None:
        self.response = {}
        self.args = ArgsParser.Instance().parse_arguments()

    def run(self):
        SystemConfigure.Instance().configure_system(self.args)
        self._execute()

    def _execute(self):
        self._generate_data()
        self._load_data()

    def _generate_data(self):
        execution_info = ExecutionInfo("GENERATE DATA")
        execution_info.start_info()

        JobsLoader.Instance().load_jobs(self.args.start_date, self.args.end_date)
        jobs_loader = JobsLoader.Instance()
        loaded_jobs = jobs_loader.loaded_jobs

        job_manager = JobsManager(loaded_jobs)
        self.response = job_manager.run()
        execution_info.end()
        execution_info.end_info()


    def _load_data(self):
        execution_info = ExecutionInfo("LOAD DATA")
        execution_info.start_info()
        execution_info.end()
        execution_info.end_info()
        # Loader(self.response).load_data()


if __name__ == "__main__":
    run = Run()
    try:
        run.run()
    except Exception as e:
        print(e)
