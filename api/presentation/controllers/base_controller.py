from abc import ABC, abstractmethod

from api.presentation.protocols.response import Response
from api.presentation.protocols.request import Request

class BaseController(ABC):

    @abstractmethod
    def handler(self, request: Request) -> Response:
        pass
