"""CreateSectionProcessor:
create a new new_section on fs from http address
"""
# pylint: disable=W0621,C0116,R0903,E0401,W0703,W1201,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203

from configs.config import ConfigMap
from models.readme_md import ReadMeMD
from models.section import Section


class CreateSectionProcessor:
    """CreateSectionProcessor."""

    def __init__(self, config_map: ConfigMap, persist_fs, http_url: str):
        """init"""
        self.http_url = http_url
        self.persist_fs = persist_fs
        self.config_map = config_map

    def process(self):
        """Process the new_section.
        - add new new_section
        - add def readme_md in new_section
        - add new sections to map at the end
        """
        section: Section = Section(self.config_map, self.http_url, self.persist_fs)
        section.write()
        readme_md: ReadMeMD = ReadMeMD(self.config_map, section, self.persist_fs)
        readme_md.write()
