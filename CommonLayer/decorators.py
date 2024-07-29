from DataAccessLayer.user_data_access import UserDataAccess
import functools
import time
from datetime import datetime


class Decorator:
    def __init__(self):
        self.user_data_access = UserDataAccess()

    def execution_time_log(self, main_function):
        @functools.wraps(main_function)
        def wrapper(*args, **kwargs):
            start_time = time.time()

            call_time = datetime.now()
            call_time_epoch = str(call_time.timestamp())

            result = main_function(*args, **kwargs)

            end_time = time.time()
            execution_time = end_time - start_time
            self.user_data_access.record_execution_time(main_function.__name__, execution_time, call_time_epoch)
            return result

        return wrapper
