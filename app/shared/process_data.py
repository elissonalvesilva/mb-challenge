import pandas as pd
import pandas_ta as ta

class ProcessData():
    def __init__(self, data, range) -> None:
        self.data = data
        self.range = range

    def process(self):
        response = []
        for collection in self.data:
            dt = pd.DataFrame(collection['mb_candles'])
            dt.set_index('date')
            for item_range in self.range:
                dt.ta.sma(close='close', length=item_range, append=True)
                dt[f'SMA_{item_range}'] = dt[f'SMA_{item_range}'].fillna(0)
            dt['pair'] = collection['mb_meta']['pair']
            response.append({ 'mb_meta': collection['mb_meta'], 'dt': dt })

        return response
