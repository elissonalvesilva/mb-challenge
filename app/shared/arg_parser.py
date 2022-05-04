import argparse
from datetime import date, timedelta, datetime

from shared.singleton import Singleton
from shared.system_exiter import SystemExiter


@Singleton
class ArgsParser:
    """
    Parse the arguments from the console.
    """

    def parse_arguments(self):
        # configure argument parser
        parser = argparse.ArgumentParser(
            description='Ingestion Script')

        parser.add_argument(
            '-sd', '--start-date', type=str, default=None, metavar='DATE',
            help='Date (start) to run script for (yyyy-mm-dd). Default: Yesterday')

        parser.add_argument(
            '-ed', '--end-date', type=str, default=None, metavar='DATE',
            help='Date (end) to run script for (yyyy-mm-dd). Default: Equal to start-date')

        parser.add_argument(
            '-r', '--retry', action='store_true',
            help='Boolean flag to retry script by pair')

        parser.add_argument(
            '-pr', '--pairs-retry', type=str, default=None,
            help='Pairs to retry separated by comma. Default: None')


        # parse arguments
        args = parser.parse_args()

        # check dates
        if args.start_date:
            args.start_date = self._to_timestamp(self._check_date_format(args.start_date))
        else:
            args.start_date = self._to_timestamp(date.today() - timedelta(days=1))

        if args.end_date:
            args.end_date = self._to_timestamp(self._check_date_format(args.end_date))
        else:
            args.end_date = args.start_date


        if args.start_date > args.end_date:
            SystemExiter.Instance().exit('Error: Start date (' + str(args.start_date) +
                                         ') must be smaller than or equal end date (' +
                                         str(args.end_date) + ').')

        # create pair
        if args.retry == True and args.pairs_retry != None:
            if ',' in args.pairs_retry:
                args.pairs_retry = args.pairs_retry.split(',')
            else:
                args.pairs_retry = [args.pairs_retry]
        else:
            args.pairs_retry = []

        return args

    def _check_date_format(self, date):
        try:
            return datetime.strptime(date, "%Y-%m-%d").date()
        except ValueError:
            SystemExiter.Instance().exit("Error: argument date: invalid format: '%s' (use yyyy-mm-dd)\n" % date)


    def _to_timestamp(self, date):
        if type(date) != str:
            date = date.strftime("%Y-%m-%d")
            element = datetime.strptime(date,"%Y-%m-%d")
            timestamp = int(datetime.timestamp(element))
        else:
            element = datetime.strptime(date,"%Y-%m-%d")
            timestamp = int(datetime.timestamp(element))

        return timestamp
