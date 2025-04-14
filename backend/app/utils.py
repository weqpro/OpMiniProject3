from enum import Enum


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MissingEnviromentVariableError(Exception):
    """if env variable was not found"""

    pass


class AidRequestStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progres"
    COMPLETED = "completed"
