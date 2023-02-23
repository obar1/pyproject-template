"""Conftest module."""

import logging
import os
from unittest import mock

import pytest

from configs.config import ConfigMap
from factories.factory_provider import CONFIG_FILE
from tests.mocke.persist_fs import PersistFS as persist_fs


@pytest.fixture(scope="function", autouse=True)
def callattr_ahead_of_alltests():
    logging.info("run_pre_start")
    logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.INFO)
    yield
    logging.info("run_after_finish")


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
def get_repo_path(get_test_path):
    yield get_test_path + "/resources/repo"


@pytest.fixture
def get_map_yaml_path(get_repo_path):
    yield get_repo_path + "/map.yaml"


@pytest.fixture
def get_unsupported_map_yaml_path(get_repo_path):
    yield get_repo_path + "/unsupported_map.yaml"


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
    yield ConfigMap(get_map_yaml_path, persist_fs)


@pytest.fixture
def dir_name():
    yield "https:§§cloud.google.com§docs"


@pytest.fixture
def get_args_create_section_processor():
    yield ["runme.sh", "create_section"]


@pytest.fixture
def get_args_refresh_map_processor():
    yield ["runme.sh", "refresh_map"]


@pytest.fixture
def get_args_refresh_links_processor():
    yield ["runme.sh", "refresh_links"]


@pytest.fixture
def get_args_refresh_puml_processor():
    yield ["runme.sh", "refresh_puml"]


@pytest.fixture
def get_args_help_processor():
    yield ["runme.sh", "help"]


@pytest.fixture
def get_args_soemthing_invalid():
    return ["runme.sh", "something_invalid"]
