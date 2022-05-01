from datetime import datetime

class Formatter():
    def __init__(self, action, table_name, pair, data) -> None:
        self.action = action
        self.table_name = table_name
        self.pair = pair
        self.data = data

    def to_json_collections(self):
        if self.data != {}:
            removed_params = self._remove_parameters()
            candles = self._extract_essecial_parameters(removed_params)
            response_data = self._append_params_output_formatter(candles)
            return response_data
        return []

    def _remove_parameters(self):
        removed_params = self.data
        del removed_params['status_code']
        del removed_params['status_message']
        del removed_params['server_unix_timestamp']
        return removed_params

    def _extract_essecial_parameters(self, data):
        essencial_params = []
        for item in data['candles']:
            date = datetime.fromtimestamp(item['timestamp'])
            date = date.strftime("%Y-%m-%d")
            essencial_params.append({
                'close': item['close'],
                'date': date
            })
        del self.data
        return essencial_params

    def _append_params_output_formatter(self, candles):
        date = datetime.now()
        response = {
            'mb_candles': candles,
            'mb_meta': {
                'pair': self.pair,
                'timestamp': date.strftime('%Y-%M-%d'),
            }
        }
        return response

