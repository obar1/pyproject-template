"""SectionValueError:"""
# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203
import logging


class SectionValueError(Exception):
    """SectionValueError"""

    def __init__(self, message, errors=None):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)

        self.errors = errors
        if message =="CONFIG_FILE not set in os env":
            logging.error("CONFIG_FILE not set in os env")
            logging.info("ex: export CONFIG_FILE='./repo/map.yaml'")