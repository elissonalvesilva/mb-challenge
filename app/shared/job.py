from shared.output_formatter import OutputFormatter
from shared.process_data import ProcessData
from shared.request import Request
from shared.formatter import Formatter
import time
from shared.writer import Writer

class Job():
    def __init__(self,
        action,
        pair,
        url,
        table_name,
        range = [20, 50, 200]
    ) -> None:
        self.action = action
        self.pair = pair
        self.url = url
        self.execution_time = -1
        self.executed = False
        self.table_name = table_name
        self.range = range

    def execute(self, method, retries):
        test = False
        count_retries = 0
        while test is False:
            test = True
            try:
                return getattr(self, method)()
            except Exception as e:
                test = False
                count_retries +=1
                if count_retries > retries:
                    Writer.Instance().url_to_retry(self.url)
                    return e
                else:
                    time.sleep(2)



    def execute_with_params(self, method, data):
        return getattr(self, method)(data)

    def results(self):
        response = Request().get_result(self.url)
        return Formatter(
            self.action,
            self.table_name,
            self.pair,
            data=response.json()
        )

    def process_results(self, results):
        process_data = ProcessData(results, self.range)
        processed_data = process_data.process()
        response = []
        for data in processed_data:
            single_moving_average_formatted = OutputFormatter(
                data['dt']
            ).to_json_collections()
            response.extend(single_moving_average_formatted)

        return response


