from shared.singleton import Singleton
from config.settings import Settings


@Singleton
class SystemConfigure():

    def configure_system(self, args):
        self.args = args
        Settings.START_DATE = self.args.start_date
        Settings.END_DATE = self.args.end_date

        self._config_general_variables()
        self._config_directories()
        self._config_jobs_to_retry()

    def _config_general_variables(self):
        if len(self.args.pairs_retry) > 0:
            Settings.IS_RETRY = self.args.retry

    def _config_directories(self):
        Settings.WORKDIRECTORY_TO_RESULTS =  Settings.WORKDIRECTORY_TO_RESULTS + '/{date}'

    def _config_jobs_to_retry(self):
        if Settings.IS_RETRY == True and len(self.args.pairs_retry) > 0:
            Settings.PAIRS_TO_RETRY.extend(self.args.pairs_retry)


