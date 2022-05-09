from datetime import datetime
from typing import List, Union
from api.presentation.errors.exceptions import DatabaseException, NotAllowedRangeDate

from api.domain.use_cases.get_mms import GetMMS
from api.domain.protocols.mms_response import MMSResponse
from api.application.protocols.get_mms_repository import GetMMSRepository


class DbGetMMS(GetMMS):
    def __init__(self, get_mms_repository: GetMMSRepository) -> None:
        super().__init__()
        self.get_mms_repository = get_mms_repository

    def get_mms(self, pair: str, from_date: datetime, to_date: datetime, range: int) -> Union[List[MMSResponse], None]:
        try:
            if self._is_date_greather_than_365_days(from_date) == True:
                raise NotAllowedRangeDate('from cant be greater than 365 days')

            mms = self.get_mms_repository.get_mms_by_parameters(pair, from_date, to_date, range)
            if len(mms) > 0:
                return mms
            else:
                return None
        except Exception as e:
            raise DatabaseException(e)

    def _is_date_greather_than_365_days(self, date_to_compare):
        current_date_timestamp = datetime.now()

        difference = current_date_timestamp - date_to_compare

        if difference.days > 365:
            return True
        return False
