import logging
from functools import wraps

class ApplicationLogger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, log_path: str = './logs/logs.log'):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler = logging.FileHandler(log_path, encoding = 'utf-8')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def log_debug(self, message):
        self.logger.debug(message)

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_critical(self, message):
        self.logger.critical(message)

def log_result_and_type(logger=None, message=None):
    if logger is None:
        logger = ApplicationLogger()

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            result_type = type(result).__name__
            log_message = f'Result of {func.__name__}: {result} (Type: {result_type})'
            if message:
                log_message += f' - {message}'
            logger.log_debug(log_message)
            return result
        return wrapper
    return decorator