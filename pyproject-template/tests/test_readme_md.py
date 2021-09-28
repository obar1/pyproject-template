# pylint: disable=W1203,C0116,R0903,C0114,C0114
import logging
from typing import List

from models.readme_md import ReadMeMD
from models.section import Section
from tests.mocke.persist_fs import PersistFS as persist_fs


def test_refresh_links(get_config_map, http_url):
    section = Section(get_config_map, http_url, persist_fs)
    readmemd = ReadMeMD(get_config_map, section, persist_fs)
    txt: List[str] = readmemd.read()
    logging.info(txt)
    readmemd.refresh_links(txt)
