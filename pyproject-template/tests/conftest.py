"""Conftest module."""
# pylint: disable=C0116,R0903,E0401,W0703,W1201,redefined-outer-name,missing-function-docstring,E0401,C0114,W0511,W1203,C0200,C0103,W1203,W0613

import logging
import os
from unittest import mock

import pytest

from configs.config import ConfigMap
from factories.factory_provider import CONFIG_FILE
from tests.moke.persist_fs import PersistFS as persist_fs


@pytest.fixture(scope="function", autouse=True)
def callattr_ahead_of_alltests(get_resource_path, mock_settings_env_vars):
    logging.info("run_pre_start")
    logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)
    yield
    logging.info("run_after_finish")


@pytest.fixture
def wip():
    logging.warning("~" * 88)


@pytest.fixture
def http_url():
    yield "https://cloud.google.com/docs"


@pytest.fixture
def http_url_2():
    yield "https://cloud.google.com/products"


@pytest.fixture
def get_test_path():
    os_path_dirname = os.path.dirname(os.path.abspath(__file__))
    yield os_path_dirname


@pytest.fixture
def get_resource_path(get_test_path):
    yield get_test_path + "/resources"


@pytest.fixture
def get_map_yaml_path(get_resource_path):
    yield get_resource_path + "/map.yaml"


@pytest.fixture
def get_repo_path(get_resource_path):
    yield get_resource_path + "/repo"


@pytest.fixture
def get_unsupported_map_yaml_path(get_resource_path):
    yield get_resource_path + "/unsupported_map.yaml"


@pytest.fixture
def get_sample_readme_md_path(get_repo_path):
    yield get_repo_path + "/https:§§cloud.google.com§docs/readme.md"


@pytest.fixture
def mock_settings_env_vars(get_map_yaml_path):
    with mock.patch.dict(os.environ, {CONFIG_FILE: get_map_yaml_path}):
        yield


@pytest.fixture
def mock_unsupported_map_yaml_env_vars(get_unsupported_map_yaml_path):
    with mock.patch.dict(os.environ, {CONFIG_FILE: get_unsupported_map_yaml_path}):
        yield


@pytest.fixture
def get_config_map(get_map_yaml_path):
    return ConfigMap(get_map_yaml_path, persist_fs)


@pytest.fixture
def dir_name():
    return "https:§§cloud.google.com§docs"


@pytest.fixture
def get_args_create_section_processor():
    return ["runme.sh", "create_section"]


@pytest.fixture
def get_args_refresh_map_processor():
    return ["runme.sh", "refresh_map"]


@pytest.fixture
def get_args_refresh_links_processor():
    return ["runme.sh", "refresh_links"]


@pytest.fixture
def get_args_refresh_puml_processor():
    return ["runme.sh", "refresh_puml"]


@pytest.fixture
def get_args_help_processor():
    return ["runme.sh", "help"]
