from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Union

from api.domain.protocols.mms_response import MMSResponse

class GetMMS(ABC):

    @abstractmethod
    def get_mms(self, pair: str, from_date: datetime, to_date: datetime, range: int) -> Union[List[MMSResponse], None]:
        pass
