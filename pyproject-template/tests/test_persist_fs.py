# pylint: disable=
import logging
from typing import List

from repository.persist_fs import PersistFS as persist_fs


def test_list_dirs(get_repo_path):
    actual = persist_fs.list_dirs(get_repo_path)
    logging.info(actual)


def test_read_file(get_sample_readme_md_path):
    actual: List[str] = persist_fs.read_file(get_sample_readme_md_path)
    logging.info(actual)
