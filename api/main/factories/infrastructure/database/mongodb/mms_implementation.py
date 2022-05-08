from application.protocols.get_mms_repository import GetMMSRepository
from infrastructure.database.mongodb.mms_implementation import MMSImplementation


def make_mms_implementation() -> GetMMSRepository:
    return MMSImplementation()
