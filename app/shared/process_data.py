import pandas as pd
import pandas_ta as ta

class ProcessData():
    def __init__(self, data, range) -> None:
        self.data = data
        self.range = range

    def process(self):
        for collection in self.data:
            dt = pd.DataFrame(collection['mb_candles'])
            for item_range in self.range:
                dt.ta.sma(close='close', length=item_range, append=True)

            return dt
