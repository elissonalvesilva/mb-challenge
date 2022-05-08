from abc import ABC

from typing import Dict, List, Optional, Union

class Response(ABC):
    def __init__(self, status_code: int, body: Optional[Union[Dict, List, str]]) -> None:
        self.status_code = status_code
        self.body = body
