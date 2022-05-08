from main.factories.application.db_get_mms_factory import make_get_mms
from presentation.controllers.base_controller import BaseController
from presentation.controllers.get_mms_controller import GetMMSController


def make_mms_controller() -> BaseController:
    mms = make_get_mms()
    return GetMMSController(mms)
