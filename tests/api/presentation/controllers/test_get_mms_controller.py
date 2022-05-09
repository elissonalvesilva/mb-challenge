import pytest
from datetime import datetime, timedelta

from api.presentation.controllers.get_mms_controller import GetMMSController
from api.presentation.errors.exceptions import DatabaseException, EmptyFromDateException, EmptyPairException, FromDateIsGreatherThanToDateException, InvalidRangeException, NotAllowedRangeDate
from api.presentation.helpers.http import OK, BadRequest, InternalError, NotFound
from api.presentation.protocols.request import Request


@pytest.fixture
def make_request_parameters():
    return {
        'pair': 'BRTLHC',
        'from_date': datetime.now() - timedelta(days=50),
        'to_date': datetime.now() - timedelta(days=1),
        'range': 50
    }


def make_sut(mocker):
    mock_cls = mocker.patch("api.domain.use_cases.get_mms.GetMMS")
    sut = GetMMSController(mock_cls)
    return sut


test_data = [
    (datetime(2020, 12, 1), datetime(2021, 12, 1), None, 20, EmptyPairException),
    (None, datetime(2021, 12, 1), 'PAIR', 20, EmptyFromDateException),
    (datetime(2021, 12, 1), datetime(2020, 12, 1), 'PAIR', 20, FromDateIsGreatherThanToDateException),
    (datetime(2020, 12, 1), datetime(2021, 12, 1), 'PAIR', 300, InvalidRangeException),
]
@pytest.mark.parametrize("from_date, to_date, pair, range, expected", test_data)
def test_validate(mocker, from_date, to_date, pair, range, expected):
    sut = make_sut(mocker)

    with pytest.raises(expected):
        sut._validate(from_date, to_date, pair, range)


test_mms = [
    ('1638774611', '1651821011', 'PAIR', 20, None, None, NotFound),
    ('1638774611', '1651821011', 'PAIR', 20, [{}], EmptyPairException('Error'), BadRequest),
    ('1638774611', '1651821011', 'PAIR', 20, [{}], EmptyFromDateException('Error'), BadRequest),
    ('1638774611', '1651821011', 'PAIR', 20, [{}], FromDateIsGreatherThanToDateException('Error'), BadRequest),
    ('1638774611', '1651821011', 'PAIR', 20, [{}], InvalidRangeException('Error'), BadRequest),
    ('1638774611', '1651821011', 'PAIR', 20, [{}], NotAllowedRangeDate('Error'), BadRequest),
    ('1638774611', '1651821011', 'PAIR', 20, [{}], DatabaseException('Error'), InternalError),
    ('1638774611', '1651821011', 'PAIR', 20, [{ 'timestamp': 123, 'mms': 123.456 }], None, OK),
]
@pytest.mark.parametrize("from_date, to_date, pair, range, return_value, exception, expected", test_mms)
def test_get_mms(mocker, from_date, to_date, pair, range, return_value, exception, expected):
    sut = make_sut(mocker)

    get_mms_mock = mocker.patch("api.domain.use_cases.get_mms.GetMMS.get_mms")
    if exception:
        get_mms_mock.side_effect = exception
    else:
        get_mms_mock.return_value = return_value

    args = {}
    args['from'] = from_date
    args['to'] = to_date
    args['range'] = range

    request = Request(param=pair, query=args)
    result = sut.handler(request)

    assert type(result) == expected


