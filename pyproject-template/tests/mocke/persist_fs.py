"""
PersistFS:
fs handling ops
"""
# pylint: disable=W1203,C0116,R0903,C0114

import logging
from typing import List

from repository.persist_fs import PersistFS as _PersistFS


class PersistFS(_PersistFS):
    """persist_fs."""

    relative_path_starts_with = "../"
    HTTPS_ = ":§§"

    @classmethod
    def list_dirs(cls, get_repo_path) -> List[str]:
        return ["https:§§cloud.google.com§docs", "https:§§cloud.google.com§products"]

    @classmethod
    def get_dir_name(cls, filename):
        logging.info(f"get_dir_name {filename}")
        return filename

    @classmethod
    def load_file(cls, config_file):
        if config_file.endswith("unsupported_map.yaml"):
            return {"type": "not_a_map", "lib": {"path": "./repo"}}
        if config_file.endswith("map.yaml"):
            return {
                "type": "map",
                "repo": {"path": "./repo", "map_md": "map.md", "sorted": True},
            }
        raise ValueError(f"{config_file} not supported")

    @classmethod
    def write_file(cls, file_name, txt):
        logging.info(f"write_file {file_name} {txt}")

    @classmethod
    def make_dirs(cls, path):
        logging.info(f"make_dirs {path}")

    @classmethod
    def read_file(cls, filename) -> List[str]:
        if filename.endswith("readme.md"):
            return """
        # https:§§cloud.google.com§docs\n
                \n
        > https://cloud.google.com/docs\n

https://cloud.google.com/products\n
                """.split(
                "\n"
            )
        raise ValueError(f"{filename} not supported")
