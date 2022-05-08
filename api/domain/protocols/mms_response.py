from domain.protocols.base_response import BaseResponse


class MMSResponse(BaseResponse):
    def __init__(self, timestamp: int, mms: float) -> None:
        self.timestamp = timestamp
        self.mms = mms

    def to_json(self):
        return {
            'timestamp': self.timestamp,
            'mms': self.mms
        }

