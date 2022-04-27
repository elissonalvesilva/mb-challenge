from decouple import config

__all__ = [
    'MB_CANDLE_URL',
]

MB_CANDLE_URL = config('MB_CANDLE_URL')
MB_FAKE_URL = config('MB_FAKE_URL')
