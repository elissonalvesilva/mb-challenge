from typing import Dict, List, Optional, Union

from presentation.protocols.response import Response


class OK(Response):
    def __init__(self, body: Optional[Union[Dict, List, str]]) -> None:
        super().__init__(200, body)


class BadRequest(Response):
    def __init__(self,  body: Optional[Union[Dict, List, str]]) -> None:
        super().__init__(400, body)


class NotFound(Response):
    def __init__(self,  body: Optional[Union[Dict, List, str]]) -> None:
        super().__init__(404, body)


class InternalError(Response):
    def __init__(self,  body: Optional[Union[Dict, List, str]]) -> None:
        super().__init__(500, body)
