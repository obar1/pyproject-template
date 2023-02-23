"""SomeException:"""

import logging


class SomeException(Exception):
    def __init__(self, message: str, errors=None):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)

        self.errors = errors
        if message == "CONFIG_FILE not set in os env":
            logging.error("CONFIG_FILE not set in os env")
            logging.info(
                """Ex:
export CONFIG_FILE='./repo/map.yaml'
"""
            )
        elif message.startswith("ConfigNotImplementedError"):
            logging.error("CONFIG_FILE has a type not implemented yet")
            logging.info(
                """Ex:
type: map
repo:
  path: .
  sorted : true
"""
            )
        else:
            logging.error("Help")
            logging.info("Help")
            
