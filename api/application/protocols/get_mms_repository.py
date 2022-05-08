from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Dict

class GetMMSRepository(ABC):

    @abstractmethod
    def get_mms_by_parameters(self, pair: str, from_date: datetime, to_date: datetime, range: int) -> List[Dict[float, int]]:
        pass
