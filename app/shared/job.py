from shared.request import Request

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
        return getattr(self, method)()

    def results(self):
        response = Request.Instance().get_result(self.url)
        return response.json()
