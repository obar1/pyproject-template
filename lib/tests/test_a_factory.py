import pytest

from lib.factories.a_factory import AFactory
from lib.tests.mocke.persist_fs import PersistFS as persist_fs


def test_get_processor_pass(get_config_map, get_args_soemthing_invalid):
    assert AFactory(get_config_map, persist_fs) is not None
