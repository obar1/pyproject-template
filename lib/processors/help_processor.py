"""RefreshMapProcessor:
refresh sections in map
"""

import logging
import os

VERSION = "__version__ = "

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # This is your Project Root


class HelpProcessor:
    """HelpProcessor"""

    def __init__(self, supported_processor):
        self.supported_processor = supported_processor

    @property
    def get_version(self) -> str:
        """read file and return the version"""
        change_log_relative_path = "../../changelog.md"
        change_log_path = os.path.abspath(
            os.path.join(ROOT_DIR, change_log_relative_path)
        )
        with open(change_log_path, mode="r", encoding="UTF-8") as file_change_log:
            txt = file_change_log.readlines()
            version = max(sorted(filter(lambda f: VERSION in f, txt)))
            logging.info(f"v. {version}")
            return version.strip()

    def process(self):
        """Get version."""
        return f"""{self.supported_processor}
{self.get_version}"""
