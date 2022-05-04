from multiprocessing.pool import ThreadPool

from config.settings import JOB_RETRIES

class JobsManager():
    def __init__(self, loaded_jobs) -> None:
        self.loaded_jobs = loaded_jobs

    def run(self):
        jobs_to_run = self._generate_jobs_to_run()
        job_to_process = self._generate_job_to_process_data()
        final_results = self._get_results(jobs_to_run, job_to_process)
        return final_results

    def _generate_jobs_to_run(self):
        jobs_to_run = []
        for job_name in list(self.loaded_jobs.keys()):
            if self.loaded_jobs[job_name].executed is False:
                jobs_to_run.append(self.loaded_jobs[job_name])
        return jobs_to_run

    def _generate_job_to_process_data(self):
        processor_job_name = list(self.loaded_jobs.keys())[0]
        return self.loaded_jobs[processor_job_name]

    def _get_results(self, jobs_to_get_results, job_to_process):
        thread_pool = ThreadPool(2)

        raw_thread_results = self._get_raw_results(thread_pool, jobs_to_get_results)
        formatted_results = self._format_raw_results(raw_thread_results)

        processed_raw_thread_results = self._process_raw_results(formatted_results, thread_pool, job_to_process)
        processed_results = self._response_raw_results(processed_raw_thread_results)

        thread_pool.close()
        thread_pool.join()
        return processed_results

    def _get_raw_results(self, thread_pool, jobs_to_get_results):
        results = []
        while len(jobs_to_get_results) > 0:
            for job in jobs_to_get_results:
                results.append(thread_pool.apply_async(job.execute, ("results", JOB_RETRIES)))
                jobs_to_get_results.remove(job)
        for result in results:
            result.wait()
        return results

    def _format_raw_results(self, results):
        final_results = []
        while len(results) > 0:
            for result in results:
                query_result = result.get()
                results.remove(result)
                if not isinstance(query_result, Exception):
                    final_results.append(query_result.to_json_collections())
        return final_results

    def _process_raw_results(self, raw_results, thread_pool, process_job):
        result = thread_pool.apply_async(process_job.execute_with_params, ('process_results', raw_results))
        result.wait()
        return result

    def _response_raw_results(self, result):
        final_result = result.get()

        return final_result
