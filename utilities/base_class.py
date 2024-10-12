from selenium.webdriver.support import expected_conditions as EC

import pytest
import inspect
import logging

@pytest.mark.usefixtures('setup')
class BaseClass:
    def get_logger(self):
        logger = logging.getLogger(inspect.stack()[1][3])
        file_handler = logging.FileHandler('logs/log_file.log')
        formatter = logging.Formatter(
            '%(asctime)s : %(levelname)s : %(name)s : %(message)s'
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.DEBUG)
        return logger
