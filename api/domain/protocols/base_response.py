from abc import ABC, abstractmethod


class BaseResponse(ABC):

    @abstractmethod
    def to_json():
        pass
