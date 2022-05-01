from multiprocessing.pool import ThreadPool

class JobsManager():
    def __init__(self, loaded_jobs) -> None:
        self.loaded_jobs = loaded_jobs

    def run(self):
        jobs_to_run = self._generate_jobs_to_run()
        final_results = self._get_results(jobs_to_run)
        return final_results

    def _generate_jobs_to_run(self):
        jobs_to_run = []
        for job_name in list(self.loaded_jobs.keys()):
            if self.loaded_jobs[job_name].executed is False:
                jobs_to_run.append(self.loaded_jobs[job_name])
        return jobs_to_run

    def _get_results(self, jobs_to_get_results):
        thread_pool = ThreadPool(1)
        raw_thread_results = self._get_raw_results(thread_pool, jobs_to_get_results)
        final_results = self._process_raw_results(raw_thread_results)
        thread_pool.close()
        thread_pool.join()
        return final_results

    def _get_raw_results(self, thread_pool, jobs_to_get_results):
        results = []
        while len(jobs_to_get_results) > 0:
            for job in jobs_to_get_results:
                results.append(thread_pool.apply_async(job.execute, ("results", 100)))
                jobs_to_get_results.remove(job)
        for result in results:
            result.wait()
        return results

    def _process_raw_results(self, results):
        final_results = []
        while len(results) > 0:
            for result in results:
                query_result = result.get()
                results.remove(result)
                # final_results += query_result.to_json_collections()
                final_results += query_result
        return final_results
