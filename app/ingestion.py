import time
import datetime

from shared.jobs_loader import JobsLoader
from shared.jobs_manager import JobsManager

if __name__ == "__main__":
    s = '12/12/2022'
    JobsLoader.Instance().load_jobs()
    jobs_loader = JobsLoader.Instance()
    jobs_loader.set_range(time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple()))
    loaded_jobs = jobs_loader.loaded_jobs

    job_manager = JobsManager(loaded_jobs)
    results = job_manager.run()
    print(results)
