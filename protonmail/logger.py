import logging
import os
from logging.handlers import RotatingFileHandler
from .utils import Singleton


import time


class CustomLogger(Singleton):
    def __init__(self):
        self.__log_dir_path = None
        self.__logger = None

    @property
    def logger(self):
        return self.__logger

    def set_log_path(self, log_dir_path):
        if self.__log_dir_path is None:
            self.__log_dir_path = log_dir_path
            self.__create_logger()

    def __create_logger(self):
        """Create the logger."""
        FORMATTER = logging.Formatter(
            "%(asctime)s — %(filename)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s" # noqa
        )
        FORMATTER.converter = time.gmtime

        if not os.path.isdir(self.__log_dir_path):
            os.makedirs(self.__log_dir_path)

        LOGFILE = os.path.join(self.__log_dir_path, "proton-client.log")

        self.__logger = logging.getLogger("proton-client")

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(FORMATTER)

        logging_level = logging.INFO

        self.__logger.setLevel(logging_level)
        # Starts a new file at 3MB size limit
        file_handler = RotatingFileHandler(
            LOGFILE, maxBytes=3145728, backupCount=3
        )
        file_handler.setFormatter(FORMATTER)
        self.__logger.addHandler(file_handler)
