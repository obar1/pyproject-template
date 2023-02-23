import logging
from typing import List

from lib.models.readme_md import ReadMeMD
from lib.models.section import Section
from lib.tests.mocke.persist_fs import PersistFS as persist_fs


def test_refresh_links(get_config_map, http_url):
    section = Section(get_config_map, http_url, persist_fs)
    readmemd = ReadMeMD(get_config_map, section, persist_fs)
    txt: List[str] = readmemd.read()
    logging.info(txt)
    readmemd.refresh_links(txt)
