from application.use_cases.db_get_mms import DbGetMMS
from main.factories.infrastructure.database.mongodb.mms_implementation import make_mms_implementation
from domain.use_cases.get_mms import GetMMS


def make_get_mms() -> GetMMS:
    repository = make_mms_implementation()
    return DbGetMMS(repository)
