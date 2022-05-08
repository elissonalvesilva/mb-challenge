class EmptyPairException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class FromDateIsGreatherThanToDateException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class InvalidRangeException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class EmptyFromDateException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class NotAllowedRangeDate(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class DatabaseException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message
