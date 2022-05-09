import pytest
from datetime import datetime, timedelta

from api.application.use_cases.db_get_mms import DbGetMMS
from api.presentation.errors.exceptions import DatabaseException, NotAllowedRangeDate


@pytest.fixture
def make_request_parameters():
    return {
        'pair': 'BRTLHC',
        'from_date': datetime.now() - timedelta(days=50),
        'to_date': datetime.now() - timedelta(days=1),
        'range': 50
    }


def make_sut(mocker):
    mock_cls = mocker.patch("api.application.protocols.get_mms_repository.GetMMSRepository")
    sut = DbGetMMS(mock_cls)
    return sut


def test_get_mms_by_parameters_called_once(make_request_parameters, mocker):
    sut = make_sut(mocker)

    get_mms_by_parameters_mock = mocker.patch("api.application.protocols.get_mms_repository.GetMMSRepository.get_mms_by_parameters")
    params = make_request_parameters
    sut.get_mms(params['pair'], params['from_date'], params['to_date'], params['range'])

    assert get_mms_by_parameters_mock.call_count == 1


def test_get_mms_by_parameters_throws(make_request_parameters, mocker):
    sut = make_sut(mocker)

    get_mms_by_parameters_mock = mocker.patch("api.application.protocols.get_mms_repository.GetMMSRepository.get_mms_by_parameters")
    get_mms_by_parameters_mock.side_effect = Exception('Error from database')
    params = make_request_parameters
    with pytest.raises(DatabaseException) as exception:
        response = sut.get_mms(params['pair'], params['from_date'], params['to_date'], params['range'])

        assert get_mms_by_parameters_mock.call_count == 1
        assert isinstance(response) == DatabaseException
        assert exception.value.message == 'Error from database'


def test_is_date_greather_than_365_days_called_once(make_request_parameters, mocker):
    sut = make_sut(mocker)

    _is_date_greather_than_365_days_mock = mocker.patch("api.application.use_cases.db_get_mms.DbGetMMS._is_date_greather_than_365_days")
    params = make_request_parameters
    sut.get_mms(params['pair'], params['from_date'], params['to_date'], params['range'])

    assert _is_date_greather_than_365_days_mock.call_count == 1

