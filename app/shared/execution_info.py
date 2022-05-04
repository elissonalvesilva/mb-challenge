from datetime import datetime

from config.settings import Settings


class ExecutionInfo:
    """
    Encapsulates the script execution info.
    """

    def __init__(self, script_phase):
        self.script_phase = script_phase
        self.start_execution = datetime.now()
        self.execution_data = {}

    def start_info(self):
        start_execution = datetime.now()
        print(f'<<<<<<<<<<<<<<< START {self.script_phase} >>>>>>>>>>>>>>>>>>>')
        print(f'started at {start_execution}')

    def end_info(self):
        print(f'<<<<<<<<<<<<<<< END {self.script_phase} >>>>>>>>>>>>>>>>>>>')
        print(f'|\tACTION_TYPE {self.execution_data["action-type"]}\t|')
        print(f'|\tSTART_DATE {self.execution_data["start-date"]}\t|')
        print(f'|\tEND_DATE {self.execution_data["end-date"]}\t|')
        print(f'|\tELAPSED_MINUTES {self.execution_data["elapsed-seconds"]}\t|')
        print(f'|\tSTART_EXECUTION {self.execution_data["start-execution"]}\t|')
        print(f'|\tEND_EXECUTION {self.execution_data["end-execution"]}\t|')
        print(f'|\tSCRIPT_PHASE {self.execution_data["script-phase"]}\t|')
        print('\n')

    def end(self):
        end_execution = datetime.now()
        elapsed_seconds = self._calculate_elapsed_seconds(self.start_execution, end_execution)
        action_type = 'RETRY PAIRS' if Settings.IS_RETRY == True else 'FULL'
        self.execution_data = {'elapsed-seconds': elapsed_seconds,
                        'start-execution': self.start_execution.strftime("%Y-%m-%dT%H:%M:%S"),
                        'end-execution': end_execution.strftime("%Y-%m-%dT%H:%M:%S"),
                        'script-phase': self.script_phase,
                        'start-date': Settings.START_DATE,
                        'end-date': Settings.END_DATE,
                        'action-type': action_type
                        }

    def _calculate_elapsed_seconds(self, start_execution, end_execution):
        elapsed_time = end_execution - start_execution
        elapsed_seconds = int(elapsed_time.total_seconds())
        elapsed_seconds = elapsed_seconds/60.0
        return elapsed_seconds
