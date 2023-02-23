"""AFactory:
factory with implemented functionality
"""

import logging

from lib.configs.config import ConfigMap
from lib.exceptions.some_exception import SomeException
from lib.processors.create_section_processor import CreateSectionProcessor
from lib.processors.help_processor import HelpProcessor


class AFactory:
    """AFactory class."""

    SUPPORTED_PROCESSOR = [
        "create_section",
        "help",
    ]

    def __init__(self, config_map: ConfigMap, persist_fs):
        self.config_map = config_map
        self.persist_fs = persist_fs

    def get_processor(self, args):
        """get the processor"""
        logging.info(f"args {args}")
        try:
            cmd = args[1]
            if cmd == "create_section":
                return self.create_section_processor(args[2])
            if cmd == "help":
                return self.help_processor()
            logging.info(self.SUPPORTED_PROCESSOR)
        except:
            raise SomeException(f"help")

    def create_section_processor(self, http_url):
        """create_section_processor"""
        return CreateSectionProcessor(self.config_map, self.persist_fs, http_url)

    def help_processor(self):
        """version_processor"""
        return HelpProcessor(self.SUPPORTED_PROCESSOR)
