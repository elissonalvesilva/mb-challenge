from typing import List, Dict, Optional

class Param:
    name: Dict

class Request:
    param: Optional[Param]
    query: Optional[Dict]

    def __init__(self, param: Optional[Param], query: Optional[Dict]) -> None:
        self.param = param
        self.query = query
