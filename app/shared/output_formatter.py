from datetime import datetime

class OutputFormatter():
    def __init__(self, data) -> None:
        self.data = data

    def to_json_collections(self):
        if len(self.data) > 0:
            self._remove_parameters_from_dataframe(self.data)
            formatted_data = self._format_response()
            return formatted_data
        return []

    def _remove_parameters_from_dataframe(self, dataframe):
        del dataframe['close']
        return dataframe

    def _format_response(self):
        return self.data.to_dict('records')
