from abc import ABC, abstractmethod

from presentation.protocols.response import Response
from presentation.protocols.request import Request

class BaseController(ABC):

    @abstractmethod
    def handler(self, request: Request) -> Response:
        pass
