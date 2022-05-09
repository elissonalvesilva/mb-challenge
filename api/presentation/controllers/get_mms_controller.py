from datetime import datetime
from api.presentation.helpers.http import OK, BadRequest, InternalError, NotFound
from api.presentation.errors.exceptions import DatabaseException, EmptyFromDateException, EmptyPairException, FromDateIsGreatherThanToDateException, InvalidRangeException, NotAllowedRangeDate
from api.presentation.controllers.base_controller import BaseController
from api.presentation.protocols.request import Request
from api.presentation.protocols.response import Response
from api.domain.use_cases.get_mms import GetMMS


class GetMMSController(BaseController):
    def __init__(self, get_mms_service: GetMMS) -> None:
        self.get_mms_service = get_mms_service

    def handler(self, request: Request) -> Response:
        param = request.param
        query_string = request.query
        pair = param
        from_date = query_string.get('from', None)
        to_date = query_string.get('to', None)
        range = query_string.get('range', None)

        try:
            from_date = self._to_timestamp(from_date)
            from_date = datetime.fromtimestamp(from_date)

            if to_date:
                to_date = datetime.fromtimestamp(self._to_timestamp(to_date))
            else:
                to_date = datetime.now() - datetime.timedelta(days=1)

            if range:
                range = int(range)
            else:
                range = 20

            self._validate(from_date, to_date, pair, range)
            response = self.get_mms_service.get_mms(pair, from_date, to_date, range)
            if response == None:
                return NotFound('Not found pair with this params')

            return OK(response)
        except EmptyPairException as e:
            return BadRequest(e)
        except EmptyFromDateException as e:
            return BadRequest(e)
        except FromDateIsGreatherThanToDateException as e:
            return BadRequest(e)
        except InvalidRangeException as e:
            return BadRequest(e)

        except NotAllowedRangeDate as e:
            return BadRequest(e)
        except DatabaseException as e:
            return InternalError(e)

    def _to_timestamp(self, date):
        if type(date) != str:
            date = date.strftime("%Y-%m-%d")
            element = datetime.strptime(date,"%Y-%m-%d")
            timestamp = int(datetime.timestamp(element))
        else:
            timestamp = int(date)
        return timestamp

    def _validate(self, from_date, to_date, pair, range):
        if pair == None:
            raise EmptyPairException('Must be pass a pair param in url')

        if from_date == None:
            raise EmptyFromDateException('from param must be pass')

        if from_date > to_date:
            raise FromDateIsGreatherThanToDateException('invalid range date. From must be less than to')

        if not range in [20, 50, 200]:
            raise InvalidRangeException('invalid days range')

