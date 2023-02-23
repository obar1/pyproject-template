import logging

from models.section import Section
from tests.mocke.persist_fs import PersistFS as persist_fs


def test_write(get_config_map, http_url):
    actual = Section(get_config_map, http_url, persist_fs)
    logging.info(actual)


def test_build_from_dir(get_config_map, dir_name):
    actual = Section.build_from_dir(get_config_map, persist_fs, dir_name)
    logging.info(actual)
